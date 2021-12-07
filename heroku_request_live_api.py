import requests

data = {
  "age": 0,
  "workclass": "Private",
  "fnlwgt": 0,
  "education": "Bachelors",
  "education_num": 0,
  "marital_status": "Married-civ-spouse",
  "occupation": "Tech-support",
  "relationship": "Wife",
  "race": "White",
  "sex": "Female",
  "hours_per_week": 0,
  "native_country": "United-States",
  "capital_gain": 0,
  "capital_loss": 0
}

response = requests.post(
    url='https://ml-model-heroku-fastapi.herokuapp.com/predict',
    json=data
)

print("Response completed successfully: ", response.status_code)
print("The response is: ", response.json())