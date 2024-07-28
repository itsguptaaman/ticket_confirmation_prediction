import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

from prediction import *

app = FastAPI()

# Define the data schema for the input
class DataPoint(BaseModel):
    travelClass: str
    bookingStatus: int
    status1Day: int = Field(default=-1)
    status1Month: int = Field(default=-1)
    status1Week: int = Field(default=-1)
    status2Days: int = Field(default=-1)

model_data = load_model(model_path)
dt = model_data['dt']
model = model_data['model']


@app.get('/')
def index():
    return {'status': 'online'}

@app.post("/predict")
def predict(data: DataPoint):
    travelClass = data.travelClass.upper()
    bookingStatus = data.bookingStatus
    status1Day = data.status1Day
    status1Month = data.status1Month
    status1Week = data.status1Week
    status2Days = data.status2Days
    # print(travelClass, bookingStatus, status1Day, status1Month, status1Week, status2Days)
    new_data_point = give_dataframe([travelClass, bookingStatus, status1Day, status1Month, status1Week, status2Days])
    prediction, prediction_prob = predict_new_data_point(model, new_data_point, dt)
    prediction_prob = prediction_prob[0]
    # print(prediction, prediction_prob)
    if prediction[0] == 0:
        return {"prediction": "Your Ticket wont get confirm", 
                f"Chances of a ticket getting confirmed after train chart preparation is ": f"{np.round(prediction_prob[1], 4) * 100}%"}
    else:
        return {"prediction": "Your Ticket will be confirm",
                "Chances of a ticket getting confirmed after train chart preparation is": f"{np.round(prediction_prob[1], 4) * 100}%"}

