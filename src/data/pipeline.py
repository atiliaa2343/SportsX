import pandas as pd

from collect import create_nbadataframe
from preprocess import compute_matchup_features

master_dataframe = create_nbadataframe(["2020-21", "2021-22", "2022-23", "2023-24"])

def training_dataset(nba_games):
    game_ids = nba_games["GAME_ID"].unique()
    games_dataset = []

    for game_id in game_ids:

        current_game = nba_games[nba_games["GAME_ID"] == game_id]
        first_row = current_game.iloc[0]
        current_date = first_row["GAME_DATE"]
        matchup = first_row["MATCHUP"]

        if "vs." in matchup:
            split_teams = matchup.split(" vs. ")
            home_team = split_teams[0].strip()
            away_team = split_teams[1].strip()

        else:
            split_teams = matchup.split(" @ ")
            away_team = split_teams[0].strip()
            home_team = split_teams[1].strip()

        features = compute_matchup_features(
            home_team,
            away_team,
            current_date,
            nba_games
        )

        games_dataset.append(features)

    return pd.DataFrame(games_dataset)
    

        