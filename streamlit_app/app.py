import streamlit as st
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from project root (adjust the number of .parent if needed)
project_root = Path(__file__).parent.parent.resolve()
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("FAST_API_KEY")


st.title ('Bank Churn Prediction - Deep Learning')

st.write('Enter Customer details:')

credit_score = st.number_input ('Credit Score', min_value = 300, max_value = 900, value = 650)
geography = st.selectbox('Geography', ['France','Germany','Spain'])
gender = st.selectbox('Gender', ['Male','Female'])
age = st.number_input('Age', min_value=18,max_value=100, value = 25)
tenure = st.number_input ('Tenure', min_value = 0, max_value = 10, value = 5)
balance = st.number_input('Balance', min_value=0, max_value=5000000)
num_of_products = st.number_input('Num of Product', min_value=1, max_value=4, value=1)
has_cr_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Member', [0,1])
estimated_salary = st.number_input('Estimated Salary', min_value=0, max_value=500000,value=1000)

if st.button('Predict Churn'):
    data = {
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_of_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active_member,
        'EstimatedSalary': estimated_salary
    }

    headers = {"x-api-key": API_KEY}  # Loaded securely from .env 
    
    try:
        response = requests.post('http://localhost:8000/predict', json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Churn Probability: {result['churn_probability']:.2f}")
            st.write('Customer is Likely Churned' if result['churned'] else 'Customer is Not Churned')
        else:
            st.error(f"Prediction failed: {response.json()}")
    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")