import sys

sys.path.append("../../../.utils/")

import pandas as pd

import alcdb

db = alcdb.DB(config="../../../.secrets/ops.ini")

with db.Session() as session:
    links = pd.read_sql(
        session.query(db.tables["download_counts"]).statement,
        db.engine,
    )
    links = links[links["file"].str.contains("week")]
    links["week"] = links["file"].apply(
        lambda x: int(x.split("week")[-1].split(".")[0])
    )
    links["year"] = links["file"].apply(lambda x: int(x.split("_")[0].split("/")[-1]))

    links = links.sort_values(["year", "week"], ascending=False)

    # print(links)
    links[["year", "week", "file"]].to_json(
        "../_data/datalinks.json",
        orient="records",
    )
