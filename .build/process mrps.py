# ---
# ---
import json
import subprocess

import pandas as pd


process = subprocess.Popen(
    [
        "Rscript",
        "main.r",
    ],
    cwd="r/",
)

process.wait()


# Maps
affpol = pd.read_csv(".tmp/affpol-mrp.csv")
affpol = affpol.groupby("region").mean()["outcome"].round(2)
affpol = affpol[affpol.index != "district of columbia"]
ranks = affpol.rank(ascending=False).astype(int)
with open("../assets/data/affpol-map.json", "w") as file:
    json.dump(
        {
            "vals": affpol.to_dict(),
            "ranks": ranks.to_dict(),
        },
        file,
        indent=2,
    )

demnorm = pd.read_csv(".tmp/normindex-mrp.csv")
demnorm = demnorm.groupby("region").mean()["outcome"].round(2)
demnorm = demnorm[demnorm.index != "district of columbia"]
ranks = demnorm.rank(ascending=False).astype(int)

with open("../assets/data/demnorm-map.json", "w") as file:
    json.dump(
        {
            "vals": demnorm.to_dict(),
            "ranks": ranks.to_dict(),
        },
        file,
        indent=2,
    )
