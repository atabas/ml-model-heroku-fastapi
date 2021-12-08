# Script to train machine learning model.

from sklearn.model_selection import train_test_split
# Add the necessary imports for the starter code.
import pandas as pd
from ml.data import process_data
from ml.model import train_model, compute_model_metrics
from joblib import dump

def train():
    # Add code to load in the data.
    data = pd.read_csv('./starter/data/census_nospace.csv')
    # Optional enhancement, use K-fold cross validation instead of a train-test split.
    train, test = train_test_split(data, test_size=0.20)

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
    # Proces the test data with the process_data function.

    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    # Train and save a model.
    model = train_model(X_train, y_train)

    dump(model, "./starter/model/model.joblib")
    dump(encoder, "./starter/model/encoder.joblib")
    dump(lb, "./starter/model/lb.joblib")

    X_test, y_test, _, _ = process_data(
        test,
        categorical_features=cat_features,
        label="salary",
        encoder=encoder,
        lb=lb,
        training=False
    )
    preds = model.predict(X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)

if __name__ == '__main__':
    train()