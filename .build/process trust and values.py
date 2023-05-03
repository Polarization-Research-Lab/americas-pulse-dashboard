# ---
# ---
import json, datetime

import pandas as pd

import utils

meta = utils.get_meta()

# # Setup
data = pd.read_csv(".tmp/all.csv")
data = utils.remove_disengaged(data)

# PRIDE | 1: extremely proud; 5: only a little proud
pride = (
    data.groupby(["year", "week", "pid3"])
    .agg(
        y_weighted=("pride", lambda x: round(utils.agg_weighted_mean(x, data), 2)),
    )
    .reset_index()
)

pride["y_weighted"] = (5 - pride["y_weighted"]) + 1
pride["x"] = (
    pride["year"]
    .astype(str)
    .str.cat(pride["week"].astype(str), sep=" ")
    .apply(
        lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime("%Y-%m-%d")
    )
)
with open("../assets/data/trustval/pride.json", "w") as file:
    json.dump(
        {
            "x": pride[pride["pid3"] == 1].to_dict(orient="list")["x"],
            "Democrats": pride[pride["pid3"] == 1].to_dict(orient="list")["y_weighted"],
            "Republicans": pride[pride["pid3"] == 2].to_dict(orient="list")[
                "y_weighted"
            ],
            "Independents": pride[pride["pid3"] == 3].to_dict(orient="list")[
                "y_weighted"
            ],
        },
        file,
        indent=4,
    )

# voting
vote_importance = (
    data.groupby(["year", "week", "pid3"])
    .agg(
        y_weighted=(
            "vote_importance",
            lambda x: round(utils.agg_weighted_mean(x, data), 2),
        ),
    )
    .reset_index()
)

vote_importance["y_weighted"] = (5 - vote_importance["y_weighted"]) + 1
vote_importance["x"] = (
    vote_importance["year"]
    .astype(str)
    .str.cat(vote_importance["week"].astype(str), sep=" ")
    .apply(
        lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime("%Y-%m-%d")
    )
)
with open("../assets/data/trustval/vote.json", "w") as file:
    json.dump(
        {
            "x": vote_importance[vote_importance["pid3"] == 1].to_dict(orient="list")[
                "x"
            ],
            "Democrats": vote_importance[vote_importance["pid3"] == 1].to_dict(
                orient="list"
            )["y_weighted"],
            "Republicans": vote_importance[vote_importance["pid3"] == 2].to_dict(
                orient="list"
            )["y_weighted"],
            "Independents": vote_importance[vote_importance["pid3"] == 3].to_dict(
                orient="list"
            )["y_weighted"],
        },
        file,
        indent=4,
    )

# response
institutional_response = (
    data.groupby(["year", "week", "pid3"])
    .agg(
        y_weighted=(
            "institutional_response",
            lambda x: round(utils.agg_weighted_mean(x, data), 2),
        ),
    )
    .reset_index()
)

institutional_response["y_weighted"] = institutional_response["y_weighted"]
institutional_response["x"] = (
    institutional_response["year"]
    .astype(str)
    .str.cat(institutional_response["week"].astype(str), sep=" ")
    .apply(
        lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime("%Y-%m-%d")
    )
)
with open("../assets/data/trustval/response.json", "w") as file:
    json.dump(
        {
            "x": institutional_response[institutional_response["pid3"] == 1].to_dict(
                orient="list"
            )["x"],
            "Democrats": institutional_response[
                institutional_response["pid3"] == 1
            ].to_dict(orient="list")["y_weighted"],
            "Republicans": institutional_response[
                institutional_response["pid3"] == 2
            ].to_dict(orient="list")["y_weighted"],
            "Independents": institutional_response[
                institutional_response["pid3"] == 3
            ].to_dict(orient="list")["y_weighted"],
        },
        file,
        indent=4,
    )


# corruption
institutional_corruption = (
    data.groupby(["year", "week", "pid3"])
    .agg(
        y_weighted=(
            "institutional_corruption",
            lambda x: round(utils.agg_weighted_mean(x, data), 2),
        ),
    )
    .reset_index()
)

institutional_corruption["y_weighted"] = (
    5 - institutional_corruption["y_weighted"]
) + 1
institutional_corruption["x"] = (
    institutional_corruption["year"]
    .astype(str)
    .str.cat(institutional_corruption["week"].astype(str), sep=" ")
    .apply(
        lambda x: datetime.datetime.strptime(x + " 0", "%Y %W %w").strftime("%Y-%m-%d")
    )
)
with open("../assets/data/trustval/corruption.json", "w") as file:
    json.dump(
        {
            "x": institutional_corruption[
                institutional_corruption["pid3"] == 1
            ].to_dict(orient="list")["x"],
            "Democrats": institutional_corruption[
                institutional_corruption["pid3"] == 1
            ].to_dict(orient="list")["y_weighted"],
            "Republicans": institutional_corruption[
                institutional_corruption["pid3"] == 2
            ].to_dict(orient="list")["y_weighted"],
            "Independents": institutional_corruption[
                institutional_corruption["pid3"] == 3
            ].to_dict(orient="list")["y_weighted"],
        },
        file,
        indent=4,
    )
