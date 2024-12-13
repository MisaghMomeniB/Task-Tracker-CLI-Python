# 📝 Task Tracker

Welcome to the **Task Tracker**! 🚀 This simple Python program allows you to manage your daily tasks with ease. It lets you add tasks, mark them as completed, and save them for future use. The tasks are stored in a `tasks.json` file, which ensures your data is persistent even after the program ends. ✅

### 🚀 Features:
- 🆕 **Add new tasks**: You can easily add tasks to your to-do list.
- ✔️ **Mark tasks as completed**: Track your progress by marking tasks as complete.
- 💾 **Persistent data storage**: All tasks are saved in a JSON file (`tasks.json`).
- 📑 **View tasks**: Quickly view your tasks and their current completion status.

### 💡 How It Works:
The Task Tracker program is a command-line application that interacts with the user through a simple text-based interface. Here’s how the flow works:

1. **Load Tasks**: When you start the application, it loads existing tasks from `tasks.json`. If the file doesn’t exist or is corrupted, the program will start with an empty task list.
2. **Add a Task**: You can add a new task by providing a title. The new task will be added with the status "not completed".
3. **Mark Task as Complete**: You can choose a task to mark as completed. It will show a ✅ (check mark) beside the task.
4. **Save Tasks**: After adding or completing tasks, the task list is saved to the JSON file so that it persists when you reopen the program.

### 🎥 Screenshots:
*(Add any screenshots or GIFs demonstrating the application in action if you'd like!)*

---

### 🛠️ Requirements:
To run the Task Tracker, make sure you have:
- Python 3.x installed
- Basic knowledge of how to run Python scripts from the command line

### 📥 How to Run:
1. **Clone or Download** this repository to your local machine.
2. **Navigate** to the project directory in your terminal.
3. **Run** the script with:
   ```bash
   python task_tracker.py
   ```

---

### 📜 Code Explanation:

Here’s a breakdown of how the program works:

1. **Loading and Saving Tasks**:
   ```python
   def load_tasks():
       # Loads tasks from 'tasks.json' if it exists
   def save_tasks(tasks):
       # Saves tasks to 'tasks.json' in a readable format
   ```

2. **Displaying Tasks**:
   ```python
   def display_tasks(tasks):
       # Shows a list of tasks with their current completion status (✔️ or ❌)
   ```

3. **Adding Tasks**:
   ```python
   def add_task(tasks):
       # Prompts the user to add a new task with a title and adds it to the list
   ```

4. **Marking Tasks as Complete**:
   ```python
   def mark_task_complete(tasks):
       # Lets the user choose a task to mark as complete (✔️)
   ```

5. **The Main Menu**:
   ```python
   def main():
       # Provides a text-based menu to the user to manage tasks
   ```

---

### 🔧 How to Contribute:
- Feel free to fork this repository, make improvements, or add new features like task priority, due dates, or more advanced task management options.
- Open an issue if you find any bugs or if you'd like to request new features.

---

### 🙏 Special Thanks:
Thanks for checking out this project! I hope it helps you stay organized and boost your productivity! 🏆

---

### 👋 Stay Connected:
Feel free to reach out with feedback or suggestions! 😊
