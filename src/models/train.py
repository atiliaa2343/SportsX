import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split



def train(nbagamesdataframe):
    dataframe = pd.read_csv(nbagamesdataframe)
    y = dataframe["outcome"]
    X = dataframe.drop("outcome", axis=1)


    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )


    model = LogisticRegression()
    model.fit(X_train, y_train)


    predictions = model.predict(X_test)


    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)


    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 score: {f1}")



if __name__ == "__main__":
    train("src/data/nbagames_dataframe.csv")