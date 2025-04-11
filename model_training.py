import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("mental_health_dataset_cleaned.csv")

# Encode target variable (mental_health_level: Low, Medium, High)
label_encoder = LabelEncoder()
df["mental_health_level"] = label_encoder.fit_transform(df["mental_health_level"])

# Define features and target
X = df.drop(columns=["mental_health_level"])
y = df["mental_health_level"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(acc * 100, 2), "%")

# Save model and encoder
joblib.dump(model, "model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
