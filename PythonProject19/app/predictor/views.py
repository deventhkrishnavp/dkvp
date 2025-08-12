import yfinance as yf
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

# Load model once globally
model = joblib.load('predictor/model/stock_model.pkl')

def home(request):
    return render(request, 'predictor/home.html')

def predict(request):
    if request.method == 'POST':
        ticker = request.POST['ticker'].strip().upper()

        try:
            # Download stock data
            data = yf.download(ticker, period='5d', interval='1d')
        except Exception as e:
            messages.error(request, f"Error fetching data: {e}")
            return render(request, 'predictor/home.html')

        if data.empty or 'Close' not in data.columns:
            messages.error(request, f"No valid stock data found for '{ticker}'.")
            return render(request, 'predictor/home.html')

        try:
            # Get last 5 valid closing prices
            valid_closes = data['Close'].dropna().tail(5)
            if valid_closes.empty:
                messages.error(request, f"Not enough data for '{ticker}'. Try again later.")
                return render(request, 'predictor/home.html')

            # ✅ FIX: Extract float, not Series/Row
            latest_price = float(valid_closes.values[-1])

            # Predict using model
            predicted_price = model.predict(np.array([[latest_price]]))[0]
        except Exception as e:
            messages.error(request, f"Prediction failed: {e}")
            return render(request, 'predictor/home.html')

        # Prepare plot data
        prices = [float(p) for p in valid_closes]
        labels = list(valid_closes.index.strftime('%b %d'))

        # Fallback if only 1 data point
        if len(prices) == 1:
            prices.insert(0, prices[0] - 10.0)
            labels.insert(0, 'Mock')

        prices.append(predicted_price)
        labels.append('Predicted')

        if len(prices) != len(labels):
            messages.error(request, "Mismatch between prices and labels. Try again.")
            return render(request, 'predictor/home.html')

        # Plot chart
        plt.figure(figsize=(8, 4))
        plt.plot(labels, prices, marker='o', linestyle='--', color='blue')
        plt.title(f"{ticker} - Recent Prices + Prediction")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (₹)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save plot imag
        img_path = os.path.join(settings.BASE_DIR, 'static', 'predictor', 'stock_plot.png')
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        plt.savefig(img_path)
        plt.close()

        return render(request, 'predictor/result.html', {
            'ticker': ticker,
            'latest': round(latest_price, 2),
            'prediction': round(predicted_price, 2),
            'graph_url': '/static/predictor/stock_plot.png',
        })

    return render(request, 'predictor/home.html')



def signup(request):
    if request.method == 'POST':
        username=request.POST.get(username='').strip()
        email = request.POST.get(email='').strip()
        password=request.POST.get(password='')
        password2 = request.POST.get(password2='')
        if password!=password2:
            message.error(request,'not match')
            redirect('signup')
            if User.objects.filter(username=username).exist():
            if User.objects.filter(email=email).exist():
                
