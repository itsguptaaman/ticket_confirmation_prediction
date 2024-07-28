import os
import pickle
import traceback

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(ROOT_PATH, 'models')
model_path = os.path.join(model_dir, 'models.pkl')


def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            model_data = pickle.load(file)
        return model_data
    except Exception as e:
        print(f"Error loading model: {e}")
        traceback.print_exc()


def predict_new_data_point(model, new_data_point, dt):
    try:
        # Map the travelClass value
        new_data_point["travelClass"] = new_data_point["travelClass"].map(dt)
        
        # Ensure the new data point has the same feature columns as the training data
        new_data_point = new_data_point.drop(columns=['travelClass'])
        
        # I want prediction probabilities
        precision_score = model.predict_proba(new_data_point)
        
        predict = model.predict(new_data_point)

        return predict, precision_score
    except Exception as e:
        print(f"Error predicting new data point: {e}")
        traceback.print_exc()

def give_dataframe(list_data):
    try:
        df = pd.DataFrame([list_data], 
                            columns=['travelClass', 'bookingStatus', 'status1Day', 'status1Month', 'status1Week', 'status2Days'])
        return df
    except Exception as e:
        print(f"Error creating dataframe: {e}")
        traceback.print_exc()

def main():
    model_data = load_model(model_path)
    dt = model_data['dt']
    model = model_data['model']

    new_data_point = give_dataframe(['SL',16,-1,-1,-1,-1])

    print(predict_new_data_point(model, new_data_point, dt))



if __name__ == '__main__':
    main()