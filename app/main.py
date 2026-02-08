from task_manager import add_task, list_tasks, mark_task_done

def main():

    choice = ""

    print("Welcome to Task Manager")

    while choice != "4":
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Which task would you like to mark as done?")) - 1
            if mark_task_done(index):
                print("Done!")
            else:
                print("Task not found")
        elif choice == "4":
            print("Gooodbye!")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
