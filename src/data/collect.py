import pandas 
import nba_api
from nba_api.stats.static import teams 
from nba_api.stats.endpoints import leaguegamefinder

#get hornets teams stats and put into a dataframe
nba_teams = teams.get_teams() 
hornets = next((team for team in nba_teams if team["abbreviation"] == "CHA"), None) 
hornets_id = hornets["id"]
#query for games where the hornets were playing 
hornetsgamesfinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=hornets_id) 
hornetgames = hornetsgamesfinder.get_data_frames()[0] 

#games in 2023-2024 BOS aganist CHA
season_list = ["2020", "2021", "2022", "2023"]
hornetgames_2324 = hornetgames[hornetgames.SEASON_ID.str[-4:].isin(season_list)]    
bos_games_2324 = hornetgames_2324[hornetgames_2324.MATCHUP.str.contains("BOS")] 
bos_games_2324 = bos_games_2324[['SEASON_ID','TEAM_ABBREVIATION','GAME_DATE', 'MATCHUP', 'PTS', 'FGM', 'FG3M', 'REB', 'AST', 'STL', 'BLK']]

