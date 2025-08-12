from django.db import models

# Create your models here.
import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2024-01-01')
data['Prediction'] = data['Close'].shift(-1)

X = np.array(data[['Close']][:-1])
y = np.array(data['Prediction'][:-1])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'predictor/model/stock_model.pkl')

