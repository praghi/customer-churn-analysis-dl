from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os
from pathlib import Path
from tensorflow.keras.models import load_model
from typing import Dict, Union, List
from fastapi import HTTPException , Depends , status , Header
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import pickle


def verify_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    
app = FastAPI()

# Define the root-file path 
# Get the project root relative to the script location
project_root = Path(__file__).parent.parent.resolve()  # two levels up if main.py is inside a folder
env_path = project_root / ".env"
print(load_dotenv(dotenv_path=env_path))

# #Call API Key & Model 
API_KEY = os.getenv("FAST_API_KEY")
model_file_path = os.path.join(project_root, "model", "bank_churn_ann.h5")
scaler_file_path = os.path.join(project_root, "model", "scaler.pkl")

#Load the model 
model = load_model(model_file_path) 

#Load standard scaler 
with open(scaler_file_path, 'rb') as f:
    scaler = pickle.load(f)

class CustomerFeatures(BaseModel):
    CreditScore:int 
    Geography:str
    Gender:str 
    Age:int
    Tenure:int 
    Balance:float 
    NumOfProducts:int
    HasCrCard:int
    IsActiveMember:int
    EstimatedSalary:float

geo_map = {'France':0, 'Spain':1, 'Germany':2}
gender_map = {'Male': 0,'Female': 1,} 

@app.post('/predict', status_code=status.HTTP_200_OK)
def predict_churn(features: CustomerFeatures, key: None = Depends(verify_key)) -> Dict[str, Union[float, int, List[str]]]:
    data = features.dict()
    #Encode Categorical 
    errors = []

    if data['Geography'] not in geo_map:
        errors.append(f"Invalid Geography: {data['Geography']}. Valid options: {list(geo_map.keys())}")
    if data['Gender'] not in gender_map:
        errors.append(f"Invalid Gender: {data['Gender']}. Valid options: {list(gender_map.keys())}")

    if errors:
        # Return all errors together as JSON with status 400 Bad Request
        return JSONResponse(status_code=400, content={"errors": errors})

    # If no errors, proceed with encoding and prediction
    data['Geography'] = geo_map[data['Geography']]
    data['Gender'] = gender_map[data['Gender']]
    
    #Convert to Dataframe 
    X = pd.DataFrame([data])
    X_scaled = scaler.transform(X) 
    #Predict 
    pred = model.predict(X_scaled)[0][0]
    return {'churn_probability': float(pred), 'churned': int(pred > 0.5)}


