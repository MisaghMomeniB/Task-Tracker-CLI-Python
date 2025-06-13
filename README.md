# ✅ Task Tracker CLI (Python)

A lightweight and intuitive **command-line task management tool** built in Python for organizing tasks, setting deadlines, and tracking progress—all from your terminal.

---

## 📋 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage Examples](#usage-examples)  
6. [Code Structure](#code-structure)  
7. [Data Persistence](#data-persistence)  
8. [Enhancements Ideas](#enhancements-ideas)  
9. [Contributing](#contributing)  
10. [License](#license)

---

## 💡 Overview

This simple yet powerful CLI app allows you to manage tasks directly from your command line—creating, updating, deleting, filtering by status (“todo”, “in-progress”, “done”), and persisting list state in JSON format for easy tracking :contentReference[oaicite:1]{index=1}.

---

## ✅ Features

- ➕ **Add tasks** with descriptive titles  
- 🔁 **Update tasks** to modify titles or change status  
- 🗑️ **Delete tasks** by ID  
- ✅ **Mark tasks** as `todo`, `in-progress`, or `done`  
- 📋 **List tasks** (all, or filter by status)  
- 🔍 **Search tasks** by keyword  
- 🔄 **Clear completed tasks**  
- 💾 **Persistent storage** in `tasks.json`

---

## 🧾 Requirements

- Python **3.7+**  
- No external libraries (uses `argparse`, `json`, and Python standard library only)

---

## ⚙️ Installation

```bash
git clone https://github.com/MisaghMomeniB/Task-Tracker-CLI-Python.git
cd Task-Tracker-CLI-Python
````

---

## 🚀 Usage Examples

```bash
# Add a new task
python task_tracker.py add "Write README for project"

# Update a task's title
python task_tracker.py update 3 "Update README with badges"

# Mark a task in progress or done
python task_tracker.py mark 3 in-progress
python task_tracker.py mark 3 done

# List all tasks or by status
python task_tracker.py list
python task_tracker.py list todo

# Search tasks by keyword
python task_tracker.py search README

# Delete a task
python task_tracker.py delete 3

# Clear all completed tasks
python task_tracker.py clear done
```

---

## 📁 Code Structure

```
Task-Tracker-CLI-Python/
├── task_tracker.py      # Core CLI app with arg parsing and commands
├── tasks.json           # Auto-generated data storage file
└── README.md            # This file
```

* **task\_tracker.py**:

  * Parses user commands via `argparse`
  * Implements task creation, updating, status changes, deletion, searching, listing, and clearing
  * Handles persistent JSON read/write operations

---

## 💾 Data Persistence

Tasks are stored in `tasks.json` with the following fields:

```json
{
  "id": 1,
  "description": "Write README for project",
  "status": "todo",
  "created_at": "2025-06-13T12:34:56",
  "updated_at": "2025-06-13T12:34:56"
}
```

The file is created automatically if it doesn't exist, ensuring seamless first-run experience.

---

## 🌟 Enhancement Ideas

* ⏰ Add **due dates** and **reminders**
* 🏷️ Add **tags or priority levels**
* 🌐 Support **batch import/export** via CSV
* 🚩 Add **CLI flags** for non-interactive modes
* 🧪 Include **unit tests** (e.g., with `pytest`)
* 📊 Integrate lightweight **visual reports** (ASCII charts or logs)

---

## 🤝 Contributing

Improvements are welcome! To contribute:

1. Fork this repository
2. Create a branch (`feature/...`)
3. Add or update features with clear comments
4. Submit a Pull Request detailing your changes

---

## 📄 License

Licensed under the **MIT License** — see `LICENSE` for details.
