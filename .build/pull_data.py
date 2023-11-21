import sys

import pandas as pd

sys.path.append(".utils/python")
import distilldb as ddb

db = ddb.Database(config="../../../../.secrets/db.json", database = 'surveys')

with db.Session() as session:
    pd.read_sql(
        session.query(db["us_unlabelled"]).statement,
        db.engine,
    ).to_csv(".tmp/all.csv", index=None)
