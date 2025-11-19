import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Paths
TODAY_TASKS_PATH = os.path.join("..", "data", "selected_tasks_today.csv")
LOG_PATH = os.path.join("..", "data", "study_log.csv")

# Load only today's selected tasks
tasks_df = pd.read_csv(TODAY_TASKS_PATH)

# Ask user for completion of today's tasks
print("\n📘 Daily Task Completion Logging")
print("---------------------------------")
completed_tasks = []

for i, row in tasks_df.iterrows():
    task_name = row["Tasks"]
    done = input(f'Did you complete "{task_name}"? (y/n): ').strip().lower()
    if done == 'y':
        hours = input(f"How many hours did you spend on '{task_name}'?: ").strip()
        try:
            hours = float(hours)
        except:
            hours = 0
        completed_tasks.append({
            "Date": datetime.today().strftime("%Y-%m-%d"),
            "Task": task_name,
            "Actual_Hours": hours,
            "Completion_Status": 1
        })
    else:
        completed_tasks.append({
            "Date": datetime.today().strftime("%Y-%m-%d"),
            "Task": task_name,
            "Actual_Hours": 0,
            "Completion_Status": 0
        })

# Convert to DataFrame
log_df = pd.DataFrame(completed_tasks)

# Append to existing log or create new
if os.path.exists(LOG_PATH):
    old_log = pd.read_csv(LOG_PATH)
    log_df = pd.concat([old_log, log_df], ignore_index=True)

log_df.to_csv(LOG_PATH, index=False)
print("\n✅ Daily log saved to study_log.csv")

log_df['Date'] = pd.to_datetime(log_df['Date'])
today = pd.to_datetime(datetime.today().strftime("%Y-%m-%d"))


# Ensure 'Date' column is datetime
log_df['Date'] = pd.to_datetime(log_df['Date'])

# Today's date
today = pd.to_datetime(datetime.today().strftime("%Y-%m-%d"))

# Logs for today
today_log = log_df[log_df['Date'] == today]

# Logs for last 7 days (weekly)
last_week = log_df[log_df['Date'] >= (datetime.today() - timedelta(days=7))]


# -----------------------------
# Window 1: Today's Session (2 plots)
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(14,5))

# Hours per task today
today_log.groupby('Task')['Actual_Hours'].sum().plot(kind='bar', ax=axes[0], color='#1f77b4', edgecolor='black', width=0.5)
axes[0].set_title("Hours Spent per Task Today", fontsize=12, fontweight='bold')
axes[0].set_xlabel("Task")
axes[0].set_ylabel("Hours")
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Completion scatter today
axes[1].scatter(today_log['Task'], today_log['Completion_Status'], s=100, c='#2ca02c', edgecolors='black', alpha=0.7)
axes[1].set_title("Task Completion Status Today", fontsize=12, fontweight='bold')
axes[1].set_xlabel("Task")
axes[1].set_ylabel("Completion (1=Done, 0=Not Done)")
axes[1].set_yticks([0,1])
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show(block=False)

# -----------------------------
# Window 2: Weekly Trends (3 plots)
# -----------------------------
fig, axes = plt.subplots(1, 3, figsize=(18,5))

# Tasks completed per day
last_week.groupby(last_week['Date'].dt.date)['Completion_Status'].sum().plot(kind='bar', ax=axes[0], color='#ff7f0e', edgecolor='black', width=0.5)
axes[0].set_title('Tasks Completed per Day', fontsize=12, fontweight='bold')
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Number of Tasks")
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Hours per task in week
last_week.groupby('Task')['Actual_Hours'].sum().plot(kind='barh', ax=axes[1], color='#9467bd', edgecolor='black')
axes[1].set_title("Total Hours per Task", fontsize=12, fontweight='bold')
axes[1].set_xlabel("Hours")
axes[1].set_ylabel("Task")
axes[1].grid(axis='x', linestyle='--', alpha=0.7)

# Completion scatter week
axes[2].scatter(last_week['Task'], last_week['Completion_Status'], s=100, c='#d62728', edgecolors='black', alpha=0.7)
axes[2].set_title("Task Completion Status", fontsize=12, fontweight='bold')
axes[2].set_xlabel("Task")
axes[2].set_ylabel("Completion (1=Done, 0=Not Done)")
axes[2].set_yticks([0,1])
axes[2].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
