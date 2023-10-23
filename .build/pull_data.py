import sys

import pandas as pd

# sys.path.append("../../../utils/")
# import distilldb as ddb

import dataset as database

db = database.connect()

db = ddb.Database(config="secrets.json")

with db.Session() as session:
    pd.read_sql(
        session.query(db["surveys"]).statement,
        db.engine,
    ).to_csv(".tmp/all.csv", index=None)
