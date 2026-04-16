import pandas as pd
from datetime import datetime
import statistics

def compute_matchup_features(hornets_games, celtics_games, game_date):
    game_date = datetime.strptime(game_date, '%Y-%m-%d')
    
    # --- Helper to compute features for one team ---
    def team_features(team_games, prefix):
        # Copy & filter games before matchup
        team_games = team_games.copy()
        team_games["GAME_DATE"] = pd.to_datetime(team_games["GAME_DATE"])
        team_games = team_games[team_games["GAME_DATE"] < game_date]
        team_games = team_games.sort_values(by="GAME_DATE", ascending=True)
        
        # Take last 5 games
        last_games = team_games.tail(5)
        
        # Compute avg points last 5
        points = last_games["PTS"] if not last_games.empty else [0]
        avg_pts_last_5 = statistics.mean(points)
        
        # Compute avg rebounds last 5
        rebs = last_games["REB"] if not last_games.empty else [0]
        avg_reb_last_5 = statistics.mean(rebs)
        
        # Compute recent wins last 5
        wins_last_5 = 0
        for wl in last_games["WL"]:
            if wl == "W":
                wins_last_5 += 1
        
        # Compute win rate over all previous games
        all_wins = 0
        all_games = team_games["WL"]
        total_games = len(all_games)
        for wl in all_games:
            if wl == "W":
                all_wins += 1
        win_rate = all_wins / total_games if total_games > 0 else 0
        
        # Return dictionary with prefixed keys
        return {
            f"{prefix}_avg_pts_last_5": avg_pts_last_5,
            f"{prefix}_avg_reb_last_5": avg_reb_last_5,
            f"{prefix}_recent_wins_last_5": wins_last_5,
            f"{prefix}_win_rate": win_rate
        } 
    
    # Compute features for both teams
    hornets_feats = team_features(hornets_games, "hornets")
    celtics_feats = team_features(celtics_games, "celtics")
    
    # --- Combine features into one dictionary (output row) ---
    row = {}
    row.update(hornets_feats)
    row.update(celtics_feats)
    
    return row
    #function should return something like:
    #{ 
    # avg_pts_last_5:, 
    #avg_reb_last_5:, 
    # recent_wins_last_5: ,
    # win_rate
    #  } 
#filter celtics history  
