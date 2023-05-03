# ---
# ---
import json, datetime


import utils

meta = utils.get_meta()

# # Setup
data = utils.load_data_partisan()

vs = [
    "norm_judges",
    "norm_polling",
    "norm_executive",
    "norm_censorship",
    "norm_loyalty",
]

data_subset = (
    data.groupby(["year", "week"])
    .agg(
        **{v: (v, lambda x: 5 - round(utils.agg_weighted_mean(x, data), 6)) for v in vs}
    )
    .reset_index()
)

data_subset["x"] = (
    data_subset["year"]
    .astype(str)
    .str.cat(data_subset["week"].astype(str), sep=" ")
    .apply(
        lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime("%Y-%m-%d")
    )
)

with open("../assets/data/demnorm-lines.json", "w") as file:
    json.dump(
        {
            "x": data_subset.to_dict(orient="list")["x"],
            **data_subset[vs].to_dict(orient="list"),
        },
        file,
        indent=4,
    )


# ------------------

data_subset = (
    data.groupby(["year", "week", "pid"])
    .agg(
        **{v: (v, lambda x: 5 - round(utils.agg_weighted_mean(x, data), 6)) for v in vs}
    )
    .reset_index()
)

data_subset["x"] = (
    data_subset["year"]
    .astype(str)
    .str.cat(data_subset["week"].astype(str), sep=" ")
    .apply(
        lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime("%Y-%m-%d")
    )
)

for v in vs:
    with open(f"../assets/data/norms/{v}.json", "w") as file:
        json.dump(
            {
                "x": data_subset[data_subset["pid"] == "dem"].to_dict(orient="list")[
                    "x"
                ],
                "Democrat": data_subset[data_subset["pid"] == "dem"].to_dict(
                    orient="list"
                )[v],
                "Republican": data_subset[data_subset["pid"] == "rep"].to_dict(
                    orient="list"
                )[v],
            },
            file,
            indent=4,
        )


## Get Norm Index
def binarize(x):
    if x > 2:
        return 0
    elif x <= 2:
        return 1


data["norm_judges"] = data["norm_judges"].apply(lambda x: binarize(x))
data["norm_polling"] = data["norm_polling"].apply(lambda x: binarize(x))
data["norm_executive"] = data["norm_executive"].apply(lambda x: binarize(x))
data["norm_censorship"] = data["norm_censorship"].apply(lambda x: binarize(x))
data["norm_loyalty"] = data["norm_loyalty"].apply(lambda x: binarize(x))
data["norm_sum"] = data[
    [
        "norm_judges",
        "norm_polling",
        "norm_executive",
        "norm_censorship",
        "norm_loyalty",
    ]
].sum(axis=1, skipna=True)

weektimes = (
    data.groupby(["year", "week"])
    .agg(
        # y = ('norm_sum', lambda x: round(np.nanmean(x), 2)),
        y_weighted=("norm_sum", lambda x: round(utils.agg_weighted_mean(x, data), 2)),
    )
    .reset_index()
)

meta["norm_week_avg"] = str(round(weektimes["y_weighted"].values[-1], 2))
meta["norm_week_avg_change"] = str(
    round(weektimes["y_weighted"].values[-2] - weektimes["y_weighted"].values[-1], 2)
)


utils.save_meta(meta)
