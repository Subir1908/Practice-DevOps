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
            add_task(tasks, task_name)
            print(f"Task '{task_name}' added successfully!")

        elif choice == '2':
            if not tasks:
                print("No tasks found.")
            else:
                print("\n--- Your Tasks ---")
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task['title']} - [{task['status']}]")

        elif choice == '3':
            if not tasks:
                print("No tasks available to complete.")
                continue
            try:
                task_num = int(input("Enter task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['status'] = "Completed"
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            if not tasks:
                print("No tasks available to delete.")
                continue
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed['title']}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Exiting tracker...")
            break

        else:
            print("Invalid input. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()