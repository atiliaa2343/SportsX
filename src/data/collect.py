import pandas as pd 
import nba_api
from nba_api.stats.static import teams 
from nba_api.stats.endpoints import LeagueGameLog 
import time  
import pathlib 

season_list = ["2020", "2021", "2022", "2023"] 
nba_games = pd.DataFrame() 
for seasonid in season_list: 
    season_log = LeagueGameLog(season=seasonid, player_or_team_abbreviation='T')  
    season_df = season_log.get_data_frames()[0] 
    nba_games.append(season_df)
