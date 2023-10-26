
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model('../app/api_insurance')

# Define predict function
@app.post('/predict')
def predict(age, bmi, children, smoker):
    data = pd.DataFrame([[age, bmi, children, smoker]])
    data.columns = ['age', 'bmi', 'children', 'smoker']
    predictions = predict_model(model, data=data) 
    return {'prediction': list(predictions['Label'])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)