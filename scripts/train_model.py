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
MODEL_PATH = os.path.join("..", "data", "task_time_model.pkl")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(DATA_PATH)

# -----------------------------
# FEATURES & LABEL
# -----------------------------
# Using normalized columns from processed_tasks.csv
# Example columns: Estimated_Hours, Difficulty, Completion_History, Days_Left, Category_Coding, Category_Reading
X = df.drop(columns=["Tasks", "Deadline", "Priority_Score"]) if "Priority_Score" in df.columns else df.drop(columns=["Tasks", "Deadline"])
y = df["Estimated_Hours"]  # predicting task duration

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
