import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense 
from tensorflow.keras.models import load_model
from pathlib import Path
import os

#Define the root-file path 
project_root = Path.cwd().parents[0]
file_path = os.path.join(project_root, "data", "bank_churn.csv") 

# Read the file
df = pd.read_csv(file_path)

#Drop dimension which doesn't add value
X = df.drop(['CustomerId', 'Surname', 'Exited'], axis=1)
y = df['Exited']

#Label encoder for categorical columns 
X['Geography'] = LabelEncoder().fit_transform(X['Geography'])
X['Gender']= LabelEncoder().fit_transform(X['Gender'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test , y_train, y_test = train_test_split(X_scaled, y, test_size=0.20, random_state=20)


def save_model():
    model = Sequential([
    Dense(16,activation='relu', input_shape=(X_train.shape[1],)), 
    Dense(8, activation = 'relu'),
    Dense(1,activation='sigmoid')
])
    model.compile(optimizer='adam', loss= 'binary_crossentropy', metrics = ['accuracy'])
    model.fit(X_train,y_train, epochs=30, batch_size=16, validation_split=0.1, verbose=1)
    model.save('./bank_churn_ann.h5')
    pd.to_pickle(scaler, './scaler.pkl')

if __name__ == "__main__" :
    save_model()
    print("model saved successfully !!!")