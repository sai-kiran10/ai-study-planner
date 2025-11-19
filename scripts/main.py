import pandas as pd
import joblib
import openai
from datetime import timedelta, datetime
import os

# -----------------------------
# LOAD API KEY FROM ENV
# -----------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    raise ValueError(
        "OpenAI API key not found. "
        "Set OPENAI_API_KEY as an environment variable before running the script."
    )

# -----------------------------
# PATHS
# -----------------------------
DATA_PATH = os.path.join("..", "data", "processed_tasks.csv")
MODEL_PATH = os.path.join("..", "data", "task_priority_model.pkl")

# -----------------------------
# LOAD MODEL AND DATA
# -----------------------------
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

# -----------------------------
# PREDICT PRIORITY
# -----------------------------
def predict_priority(row):
    X = row.drop(labels=["Tasks", "Deadline", "Priority_Score"], errors="ignore").values.reshape(1, -1)
    return model.predict(X)[0]

# -----------------------------
# GENERATE GPT STUDY PLAN
# -----------------------------
def generate_ai_plan(task_list, available_hours):
    tasks_text = "\n".join([f"{t['task']} - predicted priority {t['priority']:.2f}" for t in task_list])

    prompt = f"""
You are an expert study coach. Create a daily study plan.

Available hours today: {available_hours} hours

Tasks sorted by priority:
{tasks_text}

Include:
1. Order of tasks with timeline (start–end times)
2. Short reason for prioritization
3. 3 short productivity tips
"""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    print("\n📘 AI-Powered Personalized Study Plan")
    print("-------------------------------------")

    # Step 1: Ask available hours
    try:
        available_hours = float(input("How many hours can you study today? "))
    except:
        print("Invalid input. Exiting.")
        return

    # Step 2: Show available tasks
    print("\nAvailable Tasks:")
    for i, row in df.iterrows():
        print(f"{i+1}. {row['Tasks']} (Difficulty: {row['Difficulty']})")

    # Step 3: User selects tasks
    task_nums = input("\nEnter task numbers separated by commas (e.g., 1,3): ").split(",")

    selected_tasks = []
    for tn in task_nums:
        tn = tn.strip()
        if not tn.isdigit():
            continue
        idx = int(tn) - 1
        if 0 <= idx < len(df):
            row = df.iloc[idx]
            priority = predict_priority(row)
            selected_tasks.append({
                "task": row["Tasks"],
                "priority": priority
            })

    if not selected_tasks:
        print("No valid tasks selected. Exiting.")
        return

    # Step 4: Sort by predicted priority
    selected_tasks.sort(key=lambda x: x["priority"], reverse=True)

    # Step 5: Generate AI study plan
    print("\n⏳ Generating your personalized study plan...\n")
    plan = generate_ai_plan(selected_tasks, available_hours)
    print(plan)

if __name__ == "__main__":
    main()
