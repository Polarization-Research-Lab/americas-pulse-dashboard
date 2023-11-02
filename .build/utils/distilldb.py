'''
Name: Distilled (since it's sqlalchemy with the parts a normal person cares about distilled from the rest in one Database class)

Very basic wrapper around the sqlalchemy orm that tries to replicate the ease of use that you get with r's dbplyr. Namely:
- provide the database connection details (in this case ones that are stored in a config file)
- return a single object from which you can do everything you need to

Similar in spirit to the more developed library: [dataset](https://dataset.readthedocs.io/en/latest/install.html)

Rewrote an old version of this with help from chatgpt

I actually think it's pretty good; and it gives you all the benefits of sqlalchemy. It doesnt try to reinvent the wheel; it just makes sqlalchemy more convenient

# ToDo
- upsert function
- update the insert and update functions so that it uses primary keys rather than 'id'
- change insert and update functions so that it returns the query rather than the data, then have an "execute" function similar to ddply
'''

# Python Standard Library
import urllib, pickle, os, json

# External Dependencies
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, func
from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm, sqlalchemy.schema
from sqlalchemy.types import Integer, String, Float
from sqlalchemy.sql.expression import bindparam

Types = {
    str: String,
    int: Integer,
    float: Float,
}

# Steal a bunch of functions from sqlalchemy
func = func # <-- it's just easier to work with
update = sqlalchemy.update
sql = sqlalchemy
bindparam = bindparam

class Database:

    def __init__(self, load_meta = None, config = None, **kwargs):

        # Create the database URI
        if config is not None:
            with open(config, 'r') as file: config = json.load(file)
        else:
            config = {}
        if kwargs.get('dialect', config.get('dialect', '')) == 'sqlite':
            self.uri = f"{kwargs.get('dialect', config.get('dialect', ''))}:///{kwargs.get('database', config.get('database', ''))}"
        else:
            self.uri = f"{kwargs.get('dialect', config.get('dialect', ''))}://{kwargs.get('username', config.get('username', ''))}:{urllib.parse.quote(kwargs.get('password', config.get('password', '')))}@{kwargs.get('host', config.get('host', ''))}:{kwargs.get('port', config.get('port', ''))}/{kwargs.get('database', config.get('database', ''))}"

        # Create the SQLAlchemy engine and session
        self.engine = create_engine(self.uri)
        self.Session = sessionmaker(bind=self.engine)

        self.engine_read = create_engine(self.uri)
        self.SessionRead = sessionmaker(bind=self.engine_read)

        # Create the metadata object for table definitions
        if (load_meta is not None) and (os.path.exists(load_meta)):
            with open(load_meta, 'rb') as file:
                self.meta = pickle.load(file)
        else:
            self.meta = MetaData(); self.meta.reflect(self.engine)
            if load_meta is not None:
                self.save_meta(load_meta)

        # Create a class attribute for the ORM query function
        self.Session = sessionmaker(self.engine)
        # self.query = self.Session().query

    def __getitem__(self, table_name):
        # Get the table object from the metadata
        table = self.meta.tables.get(table_name)

        if table is None:
            raise KeyError(f"Table '{table_name}' does not exist.")

        return table

    def save_meta(self, path):
        '''For when you dont want to keep calling the db connection'''
        with open(path, 'wb') as file:
            pickle.dump(self.meta, file)

    def update_meta(self, path):
        self.meta = MetaData(); self.meta.reflect(self.engine)
        with open(path, 'wb') as file:
            pickle.dump(self.meta, file)

    def create_table(self, table_name, columns, drop_existing = False, primary_key = None, autoincrement_primary_key = True):
        table = self.meta.tables.get(table_name)

        if (table is not None) & (drop_existing == False):
            print(f"Table '{table_name}' already exist. Ignoring your request and continuing on like it didn't happen...")
        else:
            if (table is not None) & (drop_existing == True):
                table.drop(bind = self.engine)
                self.meta.remove(table)

            # Create a custom table class dynamically

            column_objs = []
            for column_name, column_val in columns.items():
                if type(column_val) == type:
                    column_objs.append(
                        Column(
                            column_name, 
                            Types[column_val],
                            **({'primary_key': True, 'autoincrement': autoincrement_primary_key} if primary_key == column_name else {})
                        )                    
                    )
                elif isinstance(column_val, dict):
                    column_objs.append(
                        Column(
                            column_name,
                            column_val['type'],
                            **{column_val[column_attrib] for column_attrib in column_val if column_attrib != 'primary_key'}
                            **({'primary_key': True, 'autoincrement': autoincrement_primary_key} if primary_key == column_name else {})
                        )
                    )

                else:
                    raise KeyError(f"Unrecognized column value: \"{column_name}\" with \"{column_val}\". Quitting...")


            table = Table(
                table_name, 
                self.meta,
                *column_objs
            )

            # Create the table in the database
            self.meta.create_all(self.engine)

    def get_shape(self, table):
        with self.Session() as session:
            rows = session.query(func.count()).select_from(self[table]).scalar()
            columns = len(self[table].c)
        return (rows, columns)

    def iterate(self, table, chunksize = 1):
        offset = 0
        for chunk in range(0, self.get_shape(table)[0], chunksize):
            yield self[table].select().limit(chunksize).offset(offset)
            offset += chunksize

    def update(self, table, values):
        # thanks to doobeh @ https://gist.github.com/doobeh/b16e800cdd51d6413c09 for this
        with self.Session() as session:
            stmt = self[table].update().\
                where(self[table].c.id == bindparam('id')).\
                values({
                    col: bindparam(col)
                    for col in values[0]
                })

            session.execute(stmt, values)
            session.commit()


    def insert(self, table, values):
        # thanks to doobeh @ https://gist.github.com/doobeh/b16e800cdd51d6413c09 for this
        with self.Session() as session:
            stmt = self[table].insert().values(values)
            session.execute(stmt)
            session.commit()

    def select(self, table, columns):
        return sqlalchemy.select(*[getattr(self[table].c, c) for c in columns]).select_from(self[table])

    def upsert(self, table, values):

        print('THIS HASNT BEEN TESTED!!!!')
        exit()
        with self.Session() as session:
            primary_key_columns = [col.name for col in self[table].primary_key]

            # Update existing items
            for value in values:
                update_values = {col: value[col] for col in value if col != 'id'}
                stmt = self[table].update().where(self[table].c.id == value['id']).values(update_values)
                session.execute(stmt)

            # Identify new items by checking for a primary key value
            new_items = [value for value in values if 'id' not in value or value['id'] is None]

            # Insert new items
            if new_items:
                stmt = self[table].insert().values(new_items)
                session.execute(stmt)

            session.commit()

# Example usage
if __name__ == '__main__':

    # Connect to Database; if using sql, use `database` to specify the file location
    db = Database(
        dialect = 'sqlite',
        database = '.ignore/test.db',
    )

    # # Create Table
    if db.meta.tables.get('table_name') is None: # <-- you dont have to do this check if you dont want to. you can just let it throw an error to avoid overwritting an existing table
        db.create_table('table_name',{
            'col1': str,
            'col2': int,
            'col4': {'type': float},
        })
        # ^ eventually we'll probably have to complicate this with something like a dictionary of dictionaries (e.g., {'col1': {'type': str, 'primary_key': False, etc}, etc) 
            # ^ or maybe instead use: "if type(value) == type: , elif isinstance(value) is dict"

    # Access table
    table = db['table_name']

    # # Add some data
    with db.Session() as session:
        row = table.insert().values([
            {'col1': 'hey', 'col2': 0, 'col4': .2},
            {'col1': 'yo', 'col2': 1, 'col4': .2},
            {'col1': 'sup', 'col2': 2, 'col4': .992},
        ])
        session.execute(row)
        session.commit()

    # # Query Table
    with db.Session() as session:
        print(
            len(session.query(table).all())
        )

