import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

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

# -----------------------------
# Window 1: Today's Session
# -----------------------------
today_log = log_df[log_df['Date'] == today]

# 1️⃣ Hours spent per task today
plt.figure(figsize=(8,5))
hours_today = today_log.groupby('Task')['Actual_Hours'].sum()
hours_today.plot(kind='bar', color='#1f77b4', edgecolor='black', width=0.5)
plt.title("Hours Spent per Task Today", fontsize=14, fontweight='bold')
plt.xlabel("Task", fontsize=12)
plt.ylabel("Hours", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=False)

# 2️⃣ Completion status scatter today
plt.figure(figsize=(8,5))
plt.scatter(today_log['Task'], today_log['Completion_Status'], s=100, c='#2ca02c', edgecolors='black', alpha=0.7)
plt.title("Task Completion Status Today", fontsize=14, fontweight='bold')
plt.xlabel("Task", fontsize=12)
plt.ylabel("Completion (1=Done, 0=Not Done)", fontsize=12)
plt.xticks(rotation=45)
plt.yticks([0, 1])
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=False)

# -----------------------------
# Window 2: Weekly Trends (Last 7 Days)
# -----------------------------
last_week = log_df[log_df['Date'] >= (datetime.today() - pd.Timedelta(days=7))]

# 1️⃣ Tasks completed per day
plt.figure(figsize=(8,5))
tasks_per_day = last_week.groupby(last_week['Date'].dt.date)['Completion_Status'].sum()
tasks_per_day.plot(kind='bar', color='#ff7f0e', edgecolor='black', width=0.5)
plt.title('Tasks Completed per Day (Last 7 Days)', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Tasks', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=False)

# 2️⃣ Hours spent per task in last 7 days
plt.figure(figsize=(8,5))
hours_week = last_week.groupby('Task')['Actual_Hours'].sum()
hours_week.plot(kind='barh', color='#9467bd', edgecolor='black')
plt.title('Total Hours per Task (Last 7 Days)', fontsize=14, fontweight='bold')
plt.xlabel('Hours', fontsize=12)
plt.ylabel('Task', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=False)

# 3️⃣ Completion vs Task scatter (weekly)
plt.figure(figsize=(8,5))
plt.scatter(last_week['Task'], last_week['Completion_Status'], s=100, c='#d62728', edgecolors='black', alpha=0.7)
plt.title("Task Completion Status (Last 7 Days)", fontsize=14, fontweight='bold')
plt.xlabel("Task", fontsize=12)
plt.ylabel("Completion (1=Done, 0=Not Done)", fontsize=12)
plt.xticks(rotation=45)
plt.yticks([0,1])
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)  # final show blocks script so all windows stay open
