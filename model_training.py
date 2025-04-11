import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv('mental_health_dataset_cleaned.csv')

# Encode mental health status (Low, Medium, High)
label_encoder = LabelEncoder()
df['Mental_Health_Status'] = label_encoder.fit_transform(df['Mental_Health_Status'])

# Features and Target
X = df.drop('Mental_Health_Status', axis=1)
y = df['Mental_Health_Status']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'mental_health_model.pkl')

# Optional: check accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model trained successfully! Accuracy: {acc:.2f}")

