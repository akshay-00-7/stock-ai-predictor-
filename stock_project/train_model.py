import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import pickle

# Data download
def download_data():
    today = date.today().strftime("%Y-%m-%d")
    df = yf.download("RELIANCE.NS", start="2020-01-01", end=today)
    close_prices = df["Close"].values
    return close_prices

# Data prepare
def prepare_data(close_prices):
    close_prices = close_prices.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(close_prices)

    X, y = [], []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i-60:i, 0])
        y.append(scaled_data[i, 0])

    X, y = np.array(X), np.array(y)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    return X_train, X_test, y_train, y_test, scaler

# Model banana
def build_model():
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(60, 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Main
if __name__ == "__main__":
    print("Data download ho raha hai...")
    close_prices = download_data()

    print("Data prepare ho raha hai...")
    X_train, X_test, y_train, y_test, scaler = prepare_data(close_prices)

    print("Model train ho raha hai...")
    model = build_model()
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1, verbose=1)

    print("Model save ho raha hai...")
    model.save('stock_model.h5')
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    print("Done! Model save ho gaya!")