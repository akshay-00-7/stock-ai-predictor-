from flask import Flask, render_template, request, jsonify
import numpy as np
import yfinance as yf
from datetime import date, timedelta
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Model aur Scaler load karo
model = load_model('stock_model.h5')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# NSE Holidays 2026
NSE_HOLIDAYS_2026 = [
    "2026-01-26",
    "2026-03-02",
    "2026-04-14",
    "2026-04-17",
    "2026-05-01",
    "2026-08-15",
    "2026-10-02",
    "2026-10-20",
    "2026-11-04",
    "2026-11-05",
    "2026-12-25",
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        ticker = request.json['ticker']

        df = yf.download(ticker, period="90d")
        close_prices = df['Close'].values[-60:]

        close_prices = close_prices.reshape(-1, 1)
        scaled = scaler.transform(close_prices)

        X = np.array([scaled[:, 0]])
        X = X.reshape(X.shape[0], X.shape[1], 1)

        prediction = model.predict(X)
        predicted_price = scaler.inverse_transform(prediction)[0][0]

        # Agle trading day
        tomorrow = date.today() + timedelta(days=1)
        while True:
            date_str = tomorrow.strftime("%Y-%m-%d")
            if tomorrow.weekday() < 5 and date_str not in NSE_HOLIDAYS_2026:
                break
            tomorrow = tomorrow + timedelta(days=1)

        tomorrow_str = tomorrow.strftime("%d %b %Y")

        return jsonify({
            'success': True,
            'predicted_price': round(float(predicted_price), 2),
            'ticker': ticker,
            'date': tomorrow_str
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)