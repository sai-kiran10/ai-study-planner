import pandas as pd

# Load data
df = pd.read_csv("../data/tasks.csv")

# Preview data
print(df.head())
print(df.info())
print(df.describe())
