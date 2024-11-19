import os
import json

# Define the path for the file that will store the tasks
TASK_FILE = "tasks.json"


# Load tasks from the file if it exists. If the file doesn't exist, return an empty list.
def load_tasks():
    # Check if the task file exists
    if os.path.exists(TASK_FILE):
        try:
            # Open and load the tasks from the JSON file
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Handle case where the file is empty or malformed
            print("Error loading tasks. The file might be corrupted. Starting with an empty task list.")
            return []
    return []  # Return an empty list if the file doesn't exist


# Save the current list of tasks to the file in JSON format
def save_tasks(tasks):
    try:
        # Write the tasks to the file with pretty indentation
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error saving tasks. Please check file permissions.")


# Display all tasks with their status (completed or not)
def display_tasks(tasks):
    # Check if there are any tasks
    if not tasks:
        print("No tasks found!")  # Notify the user if there are no tasks
        return

    print("\nYour Tasks:")
    # Loop through each task and display its title along with its completion status
    for index, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"
        print(f"{index + 1}. {task['title']} [{status}]")


# Add a new task to the list
def add_task(tasks):
    title = input("Enter the task title: ").strip()  # Ask user for the task title
    if title:  # If title is not empty
        # Add the new task with completed set to False
        tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added!")
    else:
        print("Task title cannot be empty.")  # Inform the user if title is empty


# Mark a specific task as complete
def mark_task_complete(tasks):
    display_tasks(tasks)  # Show current tasks before asking for completion
    if not tasks:
        return  # If there are no tasks, do nothing and return

    try:
        # Ask the user to input the task number they want to mark as complete
        task_number = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_number < len(tasks):  # Check if the task number is valid
            tasks[task_number]["completed"] = True  # Mark the task as completed
            print(f"Task '{tasks[task_number]['title']}' marked as complete!")
        else:
            print("Invalid task number.")  # Handle invalid task number
    except ValueError:
        print("Please enter a valid number.")  # Handle invalid input (non-numeric)


# Main menu function to drive the program
def main():
    tasks = load_tasks()  # Load tasks when the program starts
    while True:
        print("\n--- Task Tracker ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Exit")

        # Ask the user to choose an option
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tasks(tasks)  # View all tasks
        elif choice == "2":
            add_task(tasks)  # Add a new task
            save_tasks(tasks)  # Save tasks after adding
        elif choice == "3":
            mark_task_complete(tasks)  # Mark a task as complete
            save_tasks(tasks)  # Save tasks after marking as complete
        elif choice == "4":
            save_tasks(tasks)  # Save tasks before exiting
            print("Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choice


# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
