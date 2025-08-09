# Customer Churn Analysis - Using Deep Learning

This project focuses on building an end-to-end deep learning solution for predicting customer churn. It covers the complete lifecycle from data analysis to deployment.

# Project Workflow

1. **Environment Creation**  
```bash
uv venv --python 3.10 .venv
 ``` 

2. **Activate Environment**
 ```bash 
   .venv\Scripts\Activate
 ``` 

3. **Install Requirements**
 ```bash
uv pip install -r requirements.txt
 ``` 

4. **Run FastAPI** 
 ```bash
 uvicorn main:app --reload --host 0.0.0.0 --port 800
 ``` 
Note: Running FastAPI in local host 

5. **Steps**

- EDA: Explore and visualize the dataset to understand key trends.
- Model Training: Build and train a deep learning model for churn prediction.
- Model Evaluation: Assess the model using relevant metrics and visualizations.
- Model Deployment: Deploy the model as an API service using FastAPI.
- App Creation:
a)  Frontend: Streamlit application for user interaction                    
b) Backend: FastAPI for serving predictions.

6. **Technologies Used** 
Python 3.10
Pandas, NumPy, Matplotlib, Seaborn
TensorFlow / Keras
FastAPI
Streamlit

7. **Disclaimer**
All data used in this project is fictitious and intended only for experimental and educational purposes.Using this code or methodology on real datasets is at your own risk. The author holds no responsibility for any consequences.