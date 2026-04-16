#all CHA vs. Boston games with game_date 



#filtering games where it is only boston and charlotte 
def matchup(team_games):  
    cha_boston_games = team_games[team_games['MATCHUP'].isin(['CHA vs. BOS', "CHA @ BOS"])]
    return cha_boston_games  

   