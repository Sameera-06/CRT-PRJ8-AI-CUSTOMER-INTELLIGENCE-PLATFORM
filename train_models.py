import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("data/customers.csv")

# Features
X = df[
    [
        "age",
        "income",
        "spending_score",
        "tenure",
        "monthly_visits",
        "purchase_frequency"
    ]
]

# Target
y = df["churn"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Save Model
joblib.dump(
    model,
    "models/churn_model.pkl"
)

print("Model Saved Successfully")