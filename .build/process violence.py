# ---
# ---
import json, datetime

import numpy as np
import pandas as pd

import utils

meta = utils.get_meta()

# # Setup
data = utils.load_data_partisan()
# # Violence
vs = [
    "violence1",
    "violence2",
    "violence3",
    "violence4",
    "violence5",
    "violence6",
]

vlabels = [
    "Protesting without a Permit",
    "Vandalism",
    "Assault",
    "Arson",
    "Assault with Deadly Weapon",
    "Murder",
]

# Violence Sankey
all_violence = data[vs]
survivors = None

# print(all_violence.unique())

remaining = data
sankey_params = {
    "data": [],
    "labels": {},
    "max": data.shape[0],
    "colors": {},
    "annotations": [],
}

vmeta = {}

dropped = 0
for _, v in enumerate(vs):
    init = remaining.shape[0]
    remaining = data[data[v].isna() is False]
    dropped += init - remaining.shape[0]

    # print(remaining.shape[0], '|', remaining[remaining[v] <= 2].shape[0], '|', remaining[remaining[v] >= 3].shape[0])
    vmeta[v] = {
        "supported": remaining[remaining[v] <= 2].shape[0],
        "didnt": remaining[remaining[v] >= 3].shape[0],
        "dropped": dropped,
    }


for _, v in enumerate(vs[1:]):
    sankey_params["data"].append(
        {
            "from": "Supported " + vlabels[_],
            "to": "Supported " + vlabels[_ + 1],
            "flow": vmeta[vs[_ + 1]]["supported"],
        }
    )

    sankey_params["data"].append(
        {
            "from": "Supported " + vlabels[_],
            "to": "Did not support " + vlabels[_ + 1],
            "flow": vmeta[vs[_ + 1]]["didnt"],
        }
    )

    sankey_params["data"].append(
        {
            "from": "Did not support " + vlabels[_],
            "to": "Did not support " + vlabels[_ + 1],
            "flow": vmeta[vs[_]]["dropped"] + vmeta[vs[_]]["didnt"],
        }
    )
    # print(vmeta[vs[_ + 1]]['dropped'], vmeta[vs[_]]['didnt'])

for _, v in enumerate(vs):
    didntsupp = round(
        ((vmeta[vs[_]]["dropped"] + vmeta[vs[_]]["didnt"]) / data.shape[0]) * 100, 1
    )
    # sankey_params['labels']['Did not support ' + vlabels[_]] = 'Did not support: ' + str(didntsupp) + '%'
    # sankey_params['labels']['Supported ' + vlabels[_]] = 'Supported: ' + str(round(100 - didntsupp, 1)) + '%'

    # sankey_params['labels']['Did not support ' + vlabels[_]] = '👎'
    # sankey_params['labels']['Supported ' + vlabels[_]] = '👍'

    sankey_params["annotations"].append(
        {  # 'do not support'
            "content": ["Did not support", str(didntsupp) + "%"],
            "xValue": _ + 0.4,
            "color": "white",
            "backgroundColor": "rgba(0,0,0,.7)",
            "borderColor": "rgba(0,0,0,.7)",
            "borderRadius": 10,
            "yValue": sankey_params["max"] * 0.6,
            "type": "label",
            "font": {"size": 14},
        }
    )

    sankey_params["annotations"].append(
        {  # 'do not support'
            "content": ["Support", str(round(100 - didntsupp, 1)) + "%"],
            "xValue": _,
            "color": "white",
            "backgroundColor": "rgba(0,0,0,.7)",
            "borderColor": "rgba(0,0,0,.7)",
            "borderRadius": 10,
            "yValue": -sankey_params["max"] * 0.1,
            "type": "label",
            "font": {"size": 14},
        }
    )

    sankey_params["labels"]["Did not support " + vlabels[_]] = " "
    sankey_params["labels"]["Supported " + vlabels[_]] = " "

    sankey_params["colors"]["Did not support " + vlabels[_]] = "green"
    sankey_params["colors"]["Supported " + vlabels[_]] = "red"

    # [print(d) for d in sankey_params['data'][-3:]]
    # print('\n---\n')

sankey_params["annotations"][-2]["xValue"] = 5
sankey_params["annotations"][-2]["yValue"] = sankey_params["max"] * 0.4

# print(sankey_params['labels'])
# print(sankey_params['annotations'])
# sankey_params['annotations'] = []

with open("../assets/data/violence-sankey.json", "w") as file:
    json.dump(sankey_params, file, indent=4)


# ---


def recode(x):
    if pd.isna(x):
        return 5
    else:
        return x


data["violence1"] = data["violence1"].apply(lambda x: recode(x))
data["violence2"] = data["violence2"].apply(lambda x: recode(x))
data["violence3"] = data["violence3"].apply(lambda x: recode(x))
data["violence4"] = data["violence4"].apply(lambda x: recode(x))
data["violence5"] = data["violence5"].apply(lambda x: recode(x))
data["violence6"] = data["violence6"].apply(lambda x: recode(x))


for v in vs:
    data_subset = (
        data.groupby(["year", "week", "pid"])
        .agg(
            y=(v, lambda x: round(np.nanmean(x), 6)),
            y_weighted=(v, lambda x: round(utils.agg_weighted_mean(x, data), 6)),
        )
        .reset_index()
    )

    data_subset["y"] = 5 - data_subset["y"]
    data_subset["y_weighted"] = 5 - data_subset["y_weighted"]

    data_subset["x"] = (
        data_subset["year"]
        .astype(str)
        .str.cat(data_subset["week"].astype(str), sep=" ")
        .apply(
            lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime(
                "%Y-%m-%d"
            )
        )
    )

    with open(f"../assets/data/{v}.json", "w") as file:
        json.dump(
            {
                "x": data_subset[data_subset["pid"] == "dem"].to_dict(orient="list")[
                    "x"
                ],
                "Democrat": {  # pid 1
                    # 'x': data_subset[data_subset['pid'] == 'dem'].to_dict(orient = 'list')['x'],
                    "y": data_subset[data_subset["pid"] == "dem"].to_dict(
                        orient="list"
                    )["y"],
                    "y_weighted": data_subset[data_subset["pid"] == "dem"].to_dict(
                        orient="list"
                    )["y_weighted"],
                },
                "Republican": {  # pid 2
                    # 'x': data_subset[data_subset['pid'] == 'rep'].to_dict(orient = 'list')['x'],
                    "y": data_subset[data_subset["pid"] == "rep"].to_dict(
                        orient="list"
                    )["y"],
                    "y_weighted": data_subset[data_subset["pid"] == "rep"].to_dict(
                        orient="list"
                    )["y_weighted"],
                },
            },
            file,
            indent=4,
        )


## Get Violence Index
def binarize(x):
    if x > 2:
        return 0
    elif x <= 2:
        return 1


data["violence1"] = data["violence1"].apply(lambda x: binarize(x))
data["violence2"] = data["violence2"].apply(lambda x: binarize(x))
data["violence3"] = data["violence3"].apply(lambda x: binarize(x))
data["violence4"] = data["violence4"].apply(lambda x: binarize(x))
data["violence5"] = data["violence5"].apply(lambda x: binarize(x))
data["violence6"] = data["violence6"].apply(lambda x: binarize(x))
data["violence_sum"] = data[
    ["violence1", "violence2", "violence3", "violence4", "violence5", "violence6"]
].sum(axis=1, skipna=True)

weektimes = (
    data.groupby(["year", "week"])
    .agg(
        # y = ('violence_sum', lambda x: round(np.nanmean(x), 2)),
        y_weighted=(
            "violence_sum",
            lambda x: round(utils.agg_weighted_mean(x, data), 2),
        ),
    )
    .reset_index()
)

meta["violence_week_avg"] = str(round(weektimes["y_weighted"].values[-1], 2))
meta["violence_week_avg_change"] = str(
    round(weektimes["y_weighted"].values[-2] - weektimes["y_weighted"].values[-1], 2)
)


utils.save_meta(meta)
