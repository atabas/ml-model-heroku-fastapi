from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.data import process_data


def test_process_data():
    data = pd.read_csv('./starter/data/census_nospace.csv')
    train, test = train_test_split(data, test_size=0.20, random_state=42)
    
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X_train, y_train, _, _ = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )
    assert len(X_train) == len(y_train)
