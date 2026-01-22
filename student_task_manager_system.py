tasks = []

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({"name": task_name, "completed": False})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['name']} - {status}")

def complete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    except:
        print("Invalid input.")

def main_menu():
    while True:
        print("\nStudent Task Manager System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

main_menu()
