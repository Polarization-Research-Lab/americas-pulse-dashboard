# ---
# ---
import json

import numpy as np
import pandas as pd


# Setup
## Weighted Mean
def weighted_mean(series, weights):
    return np.average(series[~np.isnan(series)], weights=weights[~np.isnan(series)])


def agg_weighted_mean(
    x, data
):  # <-- from pansen @ https://stackoverflow.com/a/43049373/6794367
    dropped = x.dropna()
    if x[dropped.index].shape[0] == 0:
        return np.nan
    else:
        return np.average(dropped, weights=data.loc[dropped.index, "weight"])


## Remove Disengaged Participants
def remove_disengaged(data):
    return data[
        (
            (data["engagement_measure"] == 7)
            & (data["year"] == 2022)
            & ((data["week"] == 40) | (data["week"] == 39))
        )
        | (
            (data["engagement_measure"] == 1)
            & (
                (data["year"] == 2022) & ((data["week"] == 40) | (data["week"] == 39))
                == False
            )
        )
        | ((data["engagement_measure"] == 1) & ((data["year"] == 2023) & (data['week'] < 25)))
        | (data["engaged"] == True)
    ]


# Recode Functions
def recode_violence_or_norm_measures(x):
    if pd.isna(x):
        return 5
    else:
        return x


## Get Violence Index
def binarize_violence(x):
    if x > 2:
        return 0
    elif x <= 2:
        return 1


def get_meta():
    with open("../_data/meta.json", "r") as file:
        return json.load(file)


def save_meta(meta):
    with open("../_data/meta.json", "w") as file:
        json.dump(meta, file)


def load_data_partisan():
    data = pd.read_csv(".tmp/all.csv")

    # remove disengaged participants
    data = remove_disengaged(data)

    # index democrats and repbulicans
    data["pid"] = None
    data.loc[data["pid7"] < 4, "pid"] = "dem"
    data.loc[(data["pid7"] > 4) & (data["pid7"] < 8), "pid"] = "rep"
    data = data[data["pid"].isin(["dem", "rep"])]

    return data
