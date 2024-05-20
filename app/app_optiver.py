import streamlit as st
import pickle
import pandas as pd
import os

# Define the path to the model
model_path = os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'best_model.pkl')

# Load the saved model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]

# Streamlit interface
st.title("Model Prediction App")

# Define the feature inputs
wap = st.number_input("WAP", value=0.0)
bid_size = st.number_input("Bid Size", value=0)
ask_size = st.number_input("Ask Size", value=0)
seconds_in_bucket = st.number_input("Seconds in Bucket", value=0)
reference_price = st.number_input("Reference Price", value=0.0)
near_price = st.number_input("Near Price", value=0.0)
bid_price = st.number_input("Bid Price", value=0.0)
ask_price = st.number_input("Ask Price", value=0.0)
matched_size = st.number_input("Matched Size", value=0)
imbalance_buy_sell_flag = st.number_input("Imbalance Buy Sell Flag", value=0)
far_price = st.number_input("Far Price", value=0.0)
imbalance_size = st.number_input("Imbalance Size", value=0)

# Create a button for prediction
if st.button("Predict"):
    input_data = {
        'wap': wap,
        'bid_size': bid_size,
        'ask_size': ask_size,
        'seconds_in_bucket': seconds_in_bucket,
        'reference_price': reference_price,
        'near_price': near_price,
        'bid_price': bid_price,
        'ask_price': ask_price,
        'matched_size': matched_size,
        'imbalance_buy_sell_flag': imbalance_buy_sell_flag,
        'far_price': far_price,
        'imbalance_size': imbalance_size
    }
    prediction = predict(input_data)
    st.write(f"The predicted value is: {prediction}")

# Running the Streamlit app
if __name__ == "__main__":
    st.write("Model Prediction App")
