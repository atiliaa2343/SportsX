import pandas as pd 
from nba_api.stats.endpoints import LeagueGameLog 


#This function calls the nba api to grab season data and all team stats into one dataframe
def create_nbadataframe(season_list): 
    nba_games = pd.DataFrame() 
    for seasonid in season_list: 
        season_log = LeagueGameLog(season=seasonid, player_or_team_abbreviation='T')  
        season_df = season_log.get_data_frames()[0] 
        nba_games = nba_games._append(season_df)
    return nba_games 

season_list = ["2020-21", "2021-22", "2022-23", "2023-24"]  
create_nbadataframe(season_list)