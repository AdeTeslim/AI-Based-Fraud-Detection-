# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle

# Define the structure of the data you expect (the transaction details)
class Transaction(BaseModel):
    type: float
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

app = FastAPI()

# Load your model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.post("/predict/")
async def predict_fraud(transaction: Transaction):
    try:
        # Convert the transaction details into a DataFrame
        input_df = pd.DataFrame([transaction.dict()])
        
        # Predict using your model
        prediction = model.predict(input_df)
        
        # Interpret the prediction
        prediction_result = "fraudulent" if prediction[0] == 1 else "not fraudulent"
        
        # Return the prediction
        return {"prediction": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


