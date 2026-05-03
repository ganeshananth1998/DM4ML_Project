import joblib
import pandas as pd

model = joblib.load("models/model_20260503090814.pkl")

df = pd.read_csv("data/processed/features.csv")

X = df[[
    "interaction_score",
    "interaction_type_encoded",
    "user_product_interaction"
]]

print(model.predict(X.head(5)))