import pandas 
import nba_api
from nba_api.stats.static import teams 
from nba_api.stats.endpoints import leaguegamefinder 
from preprocess import compute_matchup_features 
from pipeline import matchup

#get hornets teams stats and put into a dataframe
nba_teams = teams.get_teams() 
hornets = next((team for team in nba_teams if team["abbreviation"] == "CHA"), None) 
hornets_id = hornets["id"]
#query for games where the hornets were playing 
hornetsgamesfinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=hornets_id) 
hornetgames = hornetsgamesfinder.get_data_frames()[0]  

#get celtics teams stats and put into a dataframe
nba_teams = teams.get_teams() 
celtics = next((team for team in nba_teams if team["abbreviation"] == "BOS"), None) 
celtics_id = celtics["id"]
#query for games where the celtics were playing 
celticsgamesfinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=celtics_id) 
celticsgames = celticsgamesfinder.get_data_frames()[0] 
season_list = ["2020", "2021", "2022", "2023"] 
#games in 2023-2024 for hornets aganist celtics 
hornetgames_2324 = hornetgames[hornetgames.SEASON_ID.str[-4:].isin(season_list)]    
cha_games_2324 = hornetgames_2324[hornetgames_2324.MATCHUP.str.contains("BOS")] 
cha_games_2324 = cha_games_2324[['SEASON_ID','TEAM_ABBREVIATION','GAME_DATE', 'MATCHUP', 'PTS', 'FGM', 'FG3M', 'REB', 'AST', 'STL', 'BLK', 'WL']]
allhornetgames = hornetgames_2324[['SEASON_ID','TEAM_ABBREVIATION','GAME_DATE', 'MATCHUP', 'PTS', 'FGM', 'FG3M', 'REB', 'AST', 'STL', 'BLK', 'WL']] 
#games in 2023-2024 for celtics aganist hornets 
season_list = ["2020", "2021", "2022", "2023"]
celgames_2324 = celticsgames[celticsgames.SEASON_ID.str[-4:].isin(season_list)]    
bos_games_2324 = celgames_2324[celgames_2324.MATCHUP.str.contains("CHA")] 
bos_games_2324 = bos_games_2324[['SEASON_ID','TEAM_ABBREVIATION','GAME_DATE', 'MATCHUP', 'PTS', 'FGM', 'FG3M', 'REB', 'AST', 'STL', 'BLK',  'WL']]
allcelticgames = bos_games_2324[['SEASON_ID','TEAM_ABBREVIATION','GAME_DATE', 'MATCHUP', 'PTS', 'FGM', 'FG3M', 'REB', 'AST', 'STL', 'BLK',  'WL']]

filter_games = compute_matchup_features(allcelticgames, allhornetgames, '2024-04-01' )  
matchup_games = matchup(allhornetgames, allcelticgames) 
print(matchup_games) 
