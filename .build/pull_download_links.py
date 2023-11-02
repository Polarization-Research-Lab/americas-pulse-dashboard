import sys

import pandas as pd

sys.path.append("utils/")
import distilldb as ddb

db = ddb.Database(config="../../../../.secrets/db.json", database = "web")

with db.Session() as session:
    links = pd.read_sql(
        session.query(db["download_counts"]).statement,
        db.engine,
    )
    links = links[links["file"].str.contains("week")]
    links["week"] = links["file"].apply(
        lambda x: int(x.replace('downloads/citizens/','').split("week")[-1].split("_")[0])
    )
    links["year"] = links["file"].apply(lambda x: int(x.split("_")[0].split("/")[-1]))

    links = links.sort_values(["year", "week"], ascending=False)

    # print(links)
    links[["year", "week", "file"]].to_json(
        "../_data/datalinks.json",
        orient="records",
    )
