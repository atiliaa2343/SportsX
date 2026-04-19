#saves dataframe

def save_dataframe(games_dataframe): 
    games_dataframe.to_csv('./src/data/nbagames_dataframe.csv', encoding = 'utf-8', index=False)