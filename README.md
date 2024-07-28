# Ticket Confirmation Prediction API

This project provides a REST API for predicting the chances of a ticket getting confirmed after train chart preparation using a machine learning model. The model is exposed via a FastAPI application.

## Project Overview

The FastAPI application exposes a machine learning model trained to predict ticket confirmation based on various features like booking status, travel class, and more. The model uses a RandomForestClassifier and is served through a RESTful API.

## Dataset Description 
Refer this [Link](https://github.com/itsguptaaman/ticket_confirmation_prediction/blob/main/dataset_description.md)

## Running the API

To start the FastAPI server, use the following command:

```
uvicorn main:app 
```

### Example Usage

```
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
  "travelClass": "3A",
  "bookingStatus": 25,
  "status1Day": 30,
  "status1Month": 10,
  "status1Week": 15,
  "status2Days": 20
}'
```
