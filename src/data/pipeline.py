from preprocess import compute_matchup_features
from pandas import DataFrame 
import pandas as pd
#filtering games where it is only boston and charlotte 
def matchup(hornet_games, celtic_games):  
    cha_boston_games = hornet_games[hornet_games['MATCHUP'].isin(['CHA vs. BOS', "CHA @ BOS"])]
    games_dataset = [] 
    for game in cha_boston_games.itertuples(): 
        game_date = game.GAME_DATE
        features = compute_matchup_features(hornet_games, celtic_games, game_date)  
        if features["celtics_avg_pts_last_5"] == 0 or features["hornets_avg_pts_last_5"] == 0:
            continue
        outcome = 1 if game.WL == "W" else 0  
        features["outcome"] = outcome
        games_dataset.append(features)    
    games_dataframe = pd.DataFrame(games_dataset)

    return games_dataframe
