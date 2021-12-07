# Put the code for your API here.
import pandas as pd
import uvicorn
import numpy as np
from starter.census_data_model import CensusDataModel
from fastapi import FastAPI
import joblib
from starter.ml.data import process_data
from starter.ml.model import inference

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Welcome to the Census Data model app!"}

@app.post('/predict')
async def predict(input: CensusDataModel):
    model = joblib.load("./starter/model/model.joblib")
    encoder = joblib.load("./starter/model/encoder.joblib")
    lb = joblib.load("./starter/model/lb.joblib")

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

    input_as_dict = {k.replace('_', '-'): v  for k, v in input}
    values = np.array(list(input_as_dict.values())).reshape(1, 14)
    df = pd.DataFrame(values, columns=input_as_dict.keys())

    X, _, _, _ = process_data(
                df,
                categorical_features=cat_features,
                encoder=encoder,
                lb=lb,
                training=False
            )
    prediction = inference(model, X)
    y = lb.inverse_transform(prediction)[0]
    return {"prediction": y}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)