print("\n\n--------------------------------TODO APP-----------------------------------")

task: list[str] = []

while True:
    user_input: int = int(
        input(
            """\nEnter the number of operation you want to perform :
            1. Add Task  
            2. Delete Task
            3. View Task
            4. Quit
            ----------------------------------------------------
            """
        )
    )
    if user_input == 1:
        new_task = input("Enter your task here: ")
        if new_task.strip() == "":
            print("\nError: Task cannot be blank.\n")
        else:
            task.append(new_task)
            print("\nTask added successfully!\n")
    elif user_input == 2:
        if len(task) == 0:
            print("\nNo tasks available in list.\n")
        else:
            print("\nSelect the task which you want to delete:\n")
            for i in range(len(task)):
                print(f"{i+1}. {task[i]}")
            del_index = (
                int(input("Enter the number of the task you want to delete: ")) - 1
            )
            del task[del_index]
            print("\nTask deleted successfully!\n")
    elif user_input == 3:
        if len(task) == 0:
            print("\nNo tasks available in list .")
        else:
            print("\nYour tasks are as follows:\n")
            for i in range(len(task)):
                print(f"{i+1}. {task[i]}")
    elif user_input == 4:
        print("\nThank You! See you soon.")
        break
    else:
        print("\n\nInvalid Input!! Please enter a valid option \n")
