# 📈 StockAI — LSTM Stock Price Predictor

Ek din main apne phone pe stocks dekh raha tha aur socha — *"kash koi bata deta ki kal price kya hogi"*. Bas wahi se ye idea aaya. Maine soch liya ki kuch aisa banaunga jo actually kaam kare — sirf theory nahi, real prediction.

---

## 🤔 Ye Project Kya Hai?

Ye ek **AI-powered web app** hai jo NSE (National Stock Exchange of India) ke stocks ka **agle din ka closing price predict** karta hai.

Andar se **LSTM (Long Short-Term Memory)** neural network kaam karta hai — jo specifically time-series data (jaise stock prices) ke liye best hota hai. Model ko **6 saal ka real NSE data** dekhakar train kiya gaya hai.

---

## 🛠️ Maine Kya Use Kiya

**Machine Learning:**
- Python
- TensorFlow / Keras — LSTM model banane ke liye
- Scikit-learn — Data normalize karne ke liye (MinMaxScaler)
- NumPy — Array operations

**Backend:**
- Flask — Web server
- yFinance — Real-time stock data fetch karne ke liye

**Frontend:**
- HTML, CSS, JavaScript — Pure vanilla, koi framework nahi
- Dark theme with animated ticker tape 😄

---

## 🧠 Model Kaise Kaam Karta Hai?

```
Step 1 — yFinance se last 90 days ka data fetch karo
Step 2 — Last 60 days ka closing price lo
Step 3 — Data normalize karo (0 to 1 ke beech)
Step 4 — LSTM model mein daalo
Step 5 — Output ko wapas original scale pe lao
Step 6 — Predicted price dikha do!
```

**60 din ka window isliye** — LSTM ko pattern samajhne ke liye enough history chahiye hoti hai. Kam data doge toh prediction weak hogi.

---

## 📁 Project Structure

```
stock_project/
├── templates/
│   └── index.html        # Poora frontend yahan hai
├── app.py                # Flask server + prediction logic
├── train_model.py        # LSTM model train karne ka code
├── stock_model.h5        # Trained model (save kiya hua)
├── scaler.pkl            # MinMaxScaler (save kiya hua)
└── requirements.txt      # Saari dependencies
```

---

## 🚀 Apne PC Pe Kaise Chalayein

**1. Repo clone karo:**
```bash
git clone https://github.com/akshay-00-7/stock-ai-predictor-.git
cd stock-ai-predictor-
```

**2. Virtual environment banao:**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Dependencies install karo:**
```bash
pip install -r requirements.txt
```

**4. App chalao:**
```bash
python app.py
```

**5. Browser mein kholo:**
```
http://localhost:5000
```

---

## 📊 Supported Stocks

Abhi ye stocks directly select kar sakte ho:

| Company | Symbol |
|---------|--------|
| Reliance Industries | RELIANCE.NS |
| Tata Consultancy Services | TCS.NS |
| Infosys | INFY.NS |
| HDFC Bank | HDFCBANK.NS |
| Wipro | WIPRO.NS |
| Tata Motors | TATAMOTORS.NS |

Aur koi bhi NSE stock manually type kar sakte ho — bas `.NS` lagana mat bhoolna!

---

## 💡 Kuch Important Baatein

- Model ko **Reliance, TCS, Infosys, HDFC Bank** ke combined data pe train kiya gaya hai
- Prediction **next trading day** ke liye hoti hai — weekends aur NSE holidays automatically skip hote hain
- Ye project **educational purpose** ke liye hai — please isko actual investment decisions ke liye use mat karo 😅
- Stock market predict karna 100% possible nahi hai — ye ek learning project hai

---

## 🎯 Maine Kya Seekha Is Project Se

Sach batao toh jab maine pehli baar LSTM ke baare mein padha tha toh kuch samajh nahi aaya tha. Phir actually implement kiya toh cheezein clear hone lagi — jaise 60 din ka window kyun zaroori hai, scaling kyun karni padti hai, aur overfitting se kaise bachein.

Flask bhi pehli baar seriously use kiya — aur yFinance ne real-time data fetch karna itna easy bana diya ki hairani hui.

---

## ⚠️ Disclaimer

Ye sirf ek **student project** hai. Kisi bhi financial decision ke liye kisi certified financial advisor se milein. Stock market mein invest karna risky hota hai.

---

*Built with ❤️ and a lot of Stack Overflow — 2026*
