import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from datetime import datetime

def main():
    input_path = "data/processed/features.csv"
    
    # ✅ Create versioned model filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    model_dir = "models"
    model_path = f"{model_dir}/model_{timestamp}.pkl"

    # Load data
    df = pd.read_csv(input_path)

    # Features
    X = df[
        [
            "interaction_score",
            "interaction_type_encoded",
            "user_product_interaction"
        ]
    ]

    # Target
    y = df["is_purchase"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Evaluate
    acc = accuracy_score(y_test, predictions)

    print("Model Training Completed")
    print(f"Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    # ✅ Save model (versioned)
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, model_path)

    print(f"\nModel saved at: {model_path}")


if __name__ == "__main__":
    main()