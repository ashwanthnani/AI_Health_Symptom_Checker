import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("dataset.csv")

# Features and Target
X = df.drop("Disease", axis=1)
y = df["Disease"]

# Train Model
model = DecisionTreeClassifier()
model.fit(X, y)

# Disease Prediction Function
def predict_disease(symptoms):
    prediction = model.predict([symptoms])
    return prediction[0]

# Confidence Score Function
def get_confidence(symptoms):
    probabilities = model.predict_proba([symptoms])
    confidence = max(probabilities[0]) * 100
    return round(confidence, 2)