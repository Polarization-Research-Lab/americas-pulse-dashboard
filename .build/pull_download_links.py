import sys, json

# Dependencies
import pandas as pd
import ibis

# Setup
with open('../../../../.secrets/db.json', 'r') as file:
    secrets = json.load(file)

## Connect to new elite database with updated users
conn = ibis.mysql.connect(
    host = secrets['host'],
    user = secrets['username'],
    password = secrets['password'],
    database = 'web',
)
links = conn.table("download_counts").execute()


# Get links and paste them to a data file for jekyll
links = links[links["file"].str.contains("week") & ~links["file"].str.contains("toplines")]

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
