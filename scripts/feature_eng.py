import pandas as pd
from datetime import datetime

df = pd.read_csv("../data/tasks.csv")

# Convert Deadline into datetime
df["Deadline"] = pd.to_datetime(df["Deadline"])

# Today’s date (can be dynamic, using datetime.today())
today = datetime.today()

# Calculate Days_Left
df["Days_Left"] = (df["Deadline"] - today).dt.days

# Preview
print(df[["Tasks", "Deadline", "Days_Left"]])

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["Estimated_Hours", "Difficulty", "Completion_History", "Days_Left"]] = scaler.fit_transform(
    df[["Estimated_Hours", "Difficulty", "Completion_History", "Days_Left"]]
)

print(df.head())

df = pd.get_dummies(df, columns=["Category"], drop_first=True)

print(df.head())

df.to_csv("../data/processed_tasks.csv", index=False)
print("Processed dataset saved.")
