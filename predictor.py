import joblib
import pandas as pd

# Load the trained model
model = joblib.load("mental_health_model.pkl")

# Label encoding for gender and bullying
def encode_inputs(gender, bullying):
    gender_map = {"Male": 0, "Female": 1, "Other": 2}
    bullying_map = {"No": 0, "Yes": 1}
    return gender_map[gender], bullying_map[bullying]

def predict_mental_health(age, gender, anxiety, depression, stress, bullying, sleep):
    gender_encoded, bullying_encoded = encode_inputs(gender, bullying)
    
    input_df = pd.DataFrame([[
        age, gender_encoded, anxiety, depression, stress, bullying_encoded, sleep
    ]], columns=['Age', 'Gender', 'Anxiety Level', 'Depression Level', 'Stress Level', 'Bullying', 'Sleep Hours'])
    
    prediction = model.predict(input_df)[0]
    return prediction.capitalize()
