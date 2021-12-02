'''
Outputs the performance of the model on slices of the data.
'''
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from ml.data import process_data
from ml.model import train_model, compute_model_metrics
from joblib import load

def check_perf_on_slices():
    data = pd.read_csv('./starter/data/census_nospace.csv')
    train, test = train_test_split(data, test_size=0.20, random_state=42)

    model = load('./starter/model/model.joblib')
    encoder = load('./starter/model/encoder.joblib')
    lb = load('./starter/model/lb.joblib')
    
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
        
    with open('./starter/model/perf_slices.txt', 'w') as f:
        for cat in cat_features:
            for col in test[cat].unique():
                item = test[test[cat] == col]
                X_test, y_test, _, _ = process_data(
                    item,
                    categorical_features=cat_features,
                    label="salary",
                    encoder=encoder,
                    lb=lb,
                    training=False
                )
                
                preds = model.predict(X_test)
                precision, recall, fbeta = compute_model_metrics(y_test, preds)
                perf = f'Category:{cat}, Col:{col}, Precision:{precision}, Recall:{recall}, FBeta:{fbeta}'
                f.write(perf + '\n')

if __name__ == '__main__':
    check_perf_on_slices()