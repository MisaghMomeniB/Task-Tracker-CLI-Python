import os
import json
import datetime

# Define the path for the file that will store the tasks
TASK_FILE = "tasks.json"

# Load tasks from the file if it exists. If the file doesn't exist, return an empty list.
def load_tasks():
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading tasks. The file might be corrupted. Starting with an empty task list.")
            return []
    return []

# Save the current list of tasks to the file in JSON format
def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error saving tasks. Please check file permissions.")

# Display all tasks with their status (completed or not)
def display_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks):
        status = "✔️" if task.get("completed", False) else "❌"
        priority = task.get("priority", "Medium")
        due_date = task.get("due_date", "None")
        print(f"{index + 1}. {task['title']} [Status: {status}, Priority: {priority}, Due: {due_date}]")

# Add a new task with optional priority and due date
def add_task(tasks):
    title = input("Enter the task title: ").strip()
    if title:
        priority = input("Enter the priority (Low, Medium, High): ").strip().capitalize()
        if priority not in ["Low", "Medium", "High"]:
            priority = "Medium"

        due_date = input("Enter the due date (YYYY-MM-DD, optional): ").strip()
        if due_date:
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Due date will be ignored.")
                due_date = "None"
        else:
            due_date = "None"

        tasks.append({"title": title, "completed": False, "priority": priority, "due_date": due_date})
        print(f"Task '{title}' added with priority '{priority}' and due date '{due_date}'!")
    else:
        print("Task title cannot be empty.")

# Mark a specific task as complete
def mark_task_complete(tasks):
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print(f"Task '{tasks[task_number]['title']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task from the list
def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number)
            print(f"Task '{deleted_task['title']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Edit the title of an existing task
def edit_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_number < len(tasks):
            new_title = input("Enter the new title: ").strip()
            if new_title:
                tasks[task_number]["title"] = new_title
                print("Task updated successfully!")
            else:
                print("Task title cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Search tasks by keyword
def search_tasks(tasks):
    keyword = input("Enter a keyword to search: ").strip().lower()
    matching_tasks = [task for task in tasks if keyword in task["title"].lower()]
    if matching_tasks:
        print("\nMatching Tasks:")
        for index, task in enumerate(matching_tasks):
            status = "✔️" if task.get("completed", False) else "❌"
            print(f"{index + 1}. {task['title']} [Status: {status}]")
    else:
        print("No tasks match your search.")

# Generate a summary report of tasks
def generate_report(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task.get("completed", False))
    pending = total - completed
    print(f"\nTask Report:\n- Total tasks: {total}\n- Completed: {completed}\n- Pending: {pending}")

# Main menu function to drive the program
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Tracker ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Search Tasks")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            edit_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            generate_report(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
