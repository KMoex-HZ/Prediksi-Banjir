import pickle
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset/flood.csv")  

# Pisahkan fitur (X) dan target (y)
X = df.drop(columns=["FloodProbability"])  
y = df["FloodProbability"]

# Split data untuk training & testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat model terbaik (hasil fine-tuning)
best_xgb = XGBRegressor(
    learning_rate=0.15,
    n_estimators=400,
    max_depth=3,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

# Training model
best_xgb.fit(X_train, y_train)

# Simpan model
with open("models/xgb_flood_model.pkl", "wb") as file:
    pickle.dump(best_xgb, file)

print("✅ Model berhasil disimpan di 'models/xgb_flood_model.pkl'!")
