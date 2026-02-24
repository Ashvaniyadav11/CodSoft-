import json
import os

FILENAME = "tasks.json"

# Loading tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Saving tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=2)

# Adding new task
def add_task(tasks):
    print("\n--- Add Task ---")
    title = input("Enter task title: ")
    description = input("Enter description (optional): ")

    task = {
        "title": title,
        "description": description,
        "status": "pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully")

# Viewing all tasks
def view_tasks(tasks):
    print("\n--- Your Tasks ---")

    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["status"] == "completed" else "Not Completed"
        print(f"{i}. {task['title']} [{status}]")
        print(f"   {task['description']}")

# Marking task as completed
def complete_task(tasks):
    view_tasks(tasks)
    number = int(input("\nEnter task number to mark completed: ")) - 1

    if 0 <= number < len(tasks):
        tasks[number]["status"] = "completed"
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid number.")

# Deleting task
def delete_task(tasks):
    view_tasks(tasks)
    number = int(input("\nEnter task number to delete: ")) - 1

    if 0 <= number < len(tasks):
        tasks.pop(number)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid number.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n----------TO-DO LIST-----------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()