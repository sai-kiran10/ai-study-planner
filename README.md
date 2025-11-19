# 📘 AI-Powered Personalized Study Planner

## 🚀 Project Summary
The **AI-Powered Personalized Study Planner** is a smart application that helps students and professionals **plan, track, and optimize their study/work schedule**. Using **machine learning** and **AI-generated recommendations**, it suggests **task priorities**, estimates **time required**, and generates a **personalized study plan** based on your available hours and past performance.  

It also maintains a **study log** and provides **visual insights** on your daily and weekly productivity, helping you stay focused and achieve your learning goals efficiently.

## ✨ Features
- ✅ **AI-Generated Personalized Study Plan**: Suggests an optimized study schedule based on task difficulty, estimated hours, deadlines, and past completion history.
- 📝 **Task Logging & Completion Tracking**: Log actual hours spent and mark tasks as completed. Keeps a **cumulative history** of your study sessions.
- 📊 **Daily & Weekly Insights**: Visualize productivity trends with interactive plots:
  - Hours spent per task today  
  - Task completion status today  
  - Tasks completed per day (weekly)  
  - Total hours per task (weekly)  
  - Weekly task completion scatter
- 🔮 **ML-Based Time Prediction**: Uses a trained **Linear Regression model** to predict the time required for new tasks based on historical data.
- 🤖 **AI-Powered Recommendations**: Optionally integrates with **OpenAI API** to provide smart suggestions for scheduling and prioritizing tasks.
- 💾 **Persistent Data Storage**: All tasks, logs, and plans are stored in CSV files for easy retrieval and analysis.

## 🛠️ Tech Stack
- **Python 3.10+**
- **Pandas & NumPy** for data handling
- **Scikit-Learn** for ML time prediction
- **Matplotlib** for visual insights
- **OpenAI GPT API** (optional) for AI-powered suggestions

## 💻 Installation & Setup
1. **Clone the repository**  
```bash
git clone https://github.com/sai-kiran10/ai-study-planner.git
cd ai-study-planner
```
2. **Create and activate virtual environment:**
```bash
python -m venv venv # Windows
venv\Scripts\activate  # Windows
```
```bash
python3 -m venv venv  # Linux/MacOS
source venv/bin/activate  # Linux/MacOS
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Set OpenAI API key (optional for AI suggestions):**
```bash
setx OPENAI_API_KEY "YOUR_API_KEY_HERE" # Windows
export OPENAI_API_KEY="YOUR_API_KEY_HERE" # Linux/MacOS
```

# 🚀 How to Run:
**Load data and generate a study plan:**
```bash
python main.py
```
- Enter available study hours and select tasks.
- Get your AI-powered personalized study plan.

**Log task completion and view insights:**
```bash
python study_logger.py
```
- Marks task completion.
- Generates daily and weekly plots in two separate windows for comparison.

# 🔮 Future Scope:
- 🌐 Web or Mobile Version: Make the planner accessible online.
- 🤖 Enhanced AI Integration: Include GPT suggestions for task prioritization and study tips.
- 📅 Calendar Integration: Sync with Google Calendar or Outlook for automated scheduling.
- 🏆 Gamification & Reminders: Add badges, streaks, and notifications for motivation.
- 📊 Advanced Analytics: Heatmaps, productivity scores, and ML-based performance prediction.

# 👨‍💻 Author:
Sai Kiran
