# SportsX

SportsX predicts NBA game outcomes from team performance data. It pulls team
game logs via the [nba_api](https://github.com/swar/nba_api) package, engineers
matchup features (recent form, win rate, etc.) for the home and away teams,
and trains a baseline logistic regression classifier to predict which team
wins.

## Status

This project is in early, active development. The data collection →
feature engineering → training pipeline under `src/data` and `src/models`
works end to end; most other directories (`src/api`, `src/evaluation`,
`src/features`, `src/sentiment`, `src/utils`, `configs`, `docs`,
`deployment`, `mobile`) are scaffolding for planned work and are currently
empty.

## How it works

1. **Collect** ([src/data/collect.py](src/data/collect.py)) — fetches team
   game logs for a list of NBA seasons via `nba_api`'s `LeagueGameLog`
   endpoint and concatenates them into one DataFrame.
2. **Build training set** ([src/data/pipeline.py](src/data/pipeline.py)) —
   iterates over every game, identifies the home/away teams from the
   matchup string, and computes features for each matchup.
3. **Feature engineering** ([src/data/preprocess.py](src/data/preprocess.py))
   — for each team in a matchup, computes average points and rebounds over
   the last 5 games, wins in the last 5 games, and season-to-date win rate,
   using only games before the matchup date (no data leakage). The label is
   whether the home team won.
4. **Train** ([src/models/train.py](src/models/train.py)) — loads the
   feature CSV, splits into train/test, fits a `LogisticRegression` model,
   and prints accuracy, precision, recall, and F1.

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy nba_api scikit-learn
```

Build the training dataset (writes `src/data/nbagames_dataframe.csv`):

```bash
cd src/data
python pipeline.py
```

Train the baseline model:

```bash
cd src/models
python train.py
```

## Project layout

```
src/
  data/         # collection, feature engineering, and dataset assembly
  models/       # model training / prediction
  evaluation/   # (planned) model evaluation utilities
  features/     # (planned) reusable feature-building utilities
  sentiment/    # (planned) sentiment-based features
  api/          # (planned) serving layer
  utils/        # (planned) shared config/helpers
configs/        # (planned) feature and training configuration
docs/           # (planned) architecture, PRD, ML design docs
deployment/     # (planned) docker/kubernetes deployment
mobile/         # (planned) iOS app
notebooks/      # exploratory analysis and experiments
results/        # saved metrics and predictions
models/         # saved model artifacts
```

## Notes

- The pipeline currently targets the `2020-21` through `2023-24` seasons
  (see `create_nbadataframe` call in `pipeline.py`).
- `nba_api` calls hit the live stats.nba.com endpoints, so building the
  dataset requires network access and can take a while for multiple
  seasons.
