def add_task(tasks_list, task_name):
    """Adds a new task to the provided list."""
    new_task = {"title": task_name, "status": "Pending"}
    tasks_list.append(new_task)
    return tasks_list
def main():
    tasks = []

    while True:
        print("\n--- Mini Task Tracker ---")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter the task description: ")
            tasks.append({"title": task_name, "status": "Pending"})
            print(f"Task '{task_name}' added successfully!")
        elif choice == '5':
            print("Exiting tracker...")
            break
        else:
            # Handle at least one invalid input condition cleanly
            print("Invalid input. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()