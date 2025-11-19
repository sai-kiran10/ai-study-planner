import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# -----------------------------
# PATHS
# -----------------------------
DATA_PATH = os.path.join("..", "data", "processed_tasks.csv")
MODEL_PATH = os.path.join("..", "data", "task_priority_model.pkl")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(DATA_PATH)

# -----------------------------
# CREATE PRIORITY SCORE
# -----------------------------
df["Priority_Score"] = (
    0.4 * df["Difficulty"] +
    0.3 * (1 - df["Completion_History"]) +
    0.2 * (1 - df["Estimated_Hours"]) +
    0.5 * (1 - df["Days_Left"])
)

# -----------------------------
# FEATURES & LABEL
# -----------------------------
X = df.drop(columns=["Tasks", "Deadline", "Priority_Score"])
y = df["Priority_Score"]

# -----------------------------
# TRAIN/TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# EVALUATE MODEL
# -----------------------------
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMODEL TRAINED SUCCESSFULLY!")
print("--------------------------------")
print(f"Mean Absolute Error : {mae:.3f}")
print(f"R² Score           : {r2:.3f}")

# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, MODEL_PATH)
print(f"\nModel saved as {MODEL_PATH}")
