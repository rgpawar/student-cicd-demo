import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle


# Load dataset
data = pd.read_csv("data/student_placement.csv")

# Features and target
X = data[
    [
        "CGPA",
        "Attendance",
        "CodingScore",
        "Projects",
        "Internship"
    ]
]

y = data["Placement"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# Train model
model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)
print("Model being trained:", type(model).__name__)

# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")