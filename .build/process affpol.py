# ---
# ---
import json, datetime

import numpy as np
from scipy.stats import gaussian_kde

import utils

meta = utils.get_meta()


# # Setup
data = utils.load_data_partisan()

# calculate affective polarization
data["affpol"] = np.nan
data.loc[data["pid"] == "dem", "affpol"] = (
    data.loc[data["pid"] == "dem", "democrat_therm_1"]
    - data.loc[data["pid"] == "dem", "republican_therm_1"]
)
data.loc[data["pid"] == "rep", "affpol"] = (
    data.loc[data["pid"] == "rep", "republican_therm_1"]
    - data.loc[data["pid"] == "rep", "democrat_therm_1"]
)

data = data.loc[
    data["affpol"] >= 0,
]  # <-- we dont want those with negative affpol values

# # Build Gauge Data
meta["affpol_dem_avg"] = round(
    utils.weighted_mean(*data[data["pid"] == "dem"][["affpol", "weight"]].values.T), 2
)
meta["affpol_rep_avg"] = round(
    utils.weighted_mean(*data[data["pid"] == "rep"][["affpol", "weight"]].values.T), 2
)
meta["affpol_nat_avg"] = round(
    utils.weighted_mean(*data[["affpol", "weight"]].values.T), 2
)


# # Build Histograms
# ## Democrats
# Javi @ https://stackoverflow.com/a/74349028/6794367
dems = data[data["pid"] == "dem"]
eval_points = np.linspace(0, 100, num=101)

kde_sp = gaussian_kde(
    dems["democrat_therm_1"], bw_method="scott", weights=dems["weight"]
)
y_demtherm_sp = kde_sp.pdf(eval_points)

kde_sp = gaussian_kde(
    dems["republican_therm_1"], bw_method="scott", weights=dems["weight"]
)
y_reptherm_sp = kde_sp.pdf(eval_points)

with open("../assets/data/affpol-hist-dem.json", "w") as file:
    json.dump(
        {
            "x": eval_points.tolist(),
            "demtherm": y_demtherm_sp.tolist(),
            "reptherm": y_reptherm_sp.tolist(),
            "demtherm_avg": utils.weighted_mean(
                *dems[["democrat_therm_1", "weight"]].values.T
            ),
            "reptherm_avg": utils.weighted_mean(
                *dems[["republican_therm_1", "weight"]].values.T
            ),
        },
        file,
        indent=4,
    )

# ## Republicans
reps = data[data["pid"] == "rep"]
eval_points = np.linspace(0, 100, num=101)

kde_sp = gaussian_kde(
    reps["democrat_therm_1"], bw_method="scott", weights=reps["weight"]
)
y_demtherm_sp = kde_sp.pdf(eval_points)

kde_sp = gaussian_kde(
    reps["republican_therm_1"], bw_method="scott", weights=reps["weight"]
)
y_reptherm_sp = kde_sp.pdf(eval_points)

with open("../assets/data/affpol-hist-rep.json", "w") as file:
    json.dump(
        {
            "x": eval_points.tolist(),
            "demtherm": y_demtherm_sp.tolist(),
            "reptherm": y_reptherm_sp.tolist(),
            "demtherm_avg": utils.weighted_mean(
                *reps[["democrat_therm_1", "weight"]].values.T
            ),
            "reptherm_avg": utils.weighted_mean(
                *reps[["republican_therm_1", "weight"]].values.T
            ),
        },
        file,
        indent=4,
    )

# # Build Over-Time Data (line charts)
weektimes = (
    data.groupby(["year", "week"])
    .agg(
        y=("affpol", lambda x: round(np.nanmean(x), 2)),
        y_weighted=("affpol", lambda x: round(utils.agg_weighted_mean(x, data), 2)),
    )
    .reset_index()
)

meta["thisweek"] = weektimes["y_weighted"].values[-1]
meta["lastweek"] = weektimes["y_weighted"].values[-2]
meta["twoweeksago"] = weektimes["y_weighted"].values[-3]

meta["affpol_week_avg"] = str(round(weektimes["y_weighted"].values[-1], 2))
meta["affpol_week_avg_change"] = str(
    round(weektimes["y_weighted"].values[-2] - weektimes["y_weighted"].values[-1], 2)
)

weektimes = (
    data.groupby(["year", "week", "pid"])
    .agg(
        y=("affpol", lambda x: round(np.nanmean(x), 2)),
        y_weighted=("affpol", lambda x: round(utils.agg_weighted_mean(x, data), 2)),
    )
    .reset_index()
)

weektimes["x"] = (
    weektimes["year"]
    .astype(str)
    .str.cat(weektimes["week"].astype(str), sep=" ")
    .apply(
        lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime("%Y-%m-%d")
    )
)
with open("../assets/data/affpol-time.json", "w") as file:
    json.dump(
        {
            "Democrat": {  # pid 1
                "x": weektimes[weektimes["pid"] == "dem"].to_dict(orient="list")["x"],
                "y": weektimes[weektimes["pid"] == "dem"].to_dict(orient="list")["y"],
                "y_weighted": weektimes[weektimes["pid"] == "dem"].to_dict(
                    orient="list"
                )["y_weighted"],
            },
            "Republican": {  # pid 2
                "x": weektimes[weektimes["pid"] == "rep"].to_dict(orient="list")["x"],
                "y": weektimes[weektimes["pid"] == "rep"].to_dict(orient="list")["y"],
                "y_weighted": weektimes[weektimes["pid"] == "rep"].to_dict(
                    orient="list"
                )["y_weighted"],
            },
        },
        file,
        indent=4,
    )

utils.save_meta(meta)
