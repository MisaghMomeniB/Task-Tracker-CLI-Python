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