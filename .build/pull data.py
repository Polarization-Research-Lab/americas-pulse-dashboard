import sys

sys.path.append("../../../../.utils/")

import pandas as pd

import alcdb

db = alcdb.DB(config="../../../../.secrets/ops.ini")

with db.Session() as session:
    pd.read_sql(
        session.query(db.tables["surveys"]).statement,
        db.engine,
    ).to_csv(".tmp/all.csv", index=None)
