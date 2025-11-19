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

# -----------------------------
# Weekly Insights / Plots
# -----------------------------
# Aggregate last 7 days
log_df['Date'] = pd.to_datetime(log_df['Date'])
last_week = log_df[log_df['Date'] >= (datetime.today() - pd.Timedelta(days=7))]

# Tasks completed per day
tasks_per_day = last_week.groupby(last_week['Date'].dt.date)['Completion_Status'].sum()
tasks_per_day.plot(kind='bar', title='Tasks Completed per Day', xlabel='Date', ylabel='Number of Tasks')
plt.tight_layout()
plt.show()

# Hours spent per task
hours_per_task = last_week.groupby('Task')['Actual_Hours'].sum()
hours_per_task.plot(kind='barh', title='Hours Spent per Task', xlabel='Hours', ylabel='Task')
plt.tight_layout()
plt.show()

# Completion vs Task (optional scatter)
plt.scatter(last_week['Task'], last_week['Completion_Status'])
plt.title("Task Completion Status")
plt.xlabel("Task")
plt.ylabel("Completion (1=Done, 0=Not Done)")
plt.grid(True)
plt.show()
