menu = """
Welcome to yet-another-todo-app, please choose what you want to do:
    1. Add a task
    2. List tasks
    3. Mark task as done
    4. Quit the program
"""

options = """
    1. Add a task
    2. List tasks
    3. Mark task as done
    4. Quit the program
"""


def main():
    print(menu)
    while True:
        choice = int(input(": "))
        print(choice)

        match choice:
            case 1:
                add_task()
                break
            case _:
                print("Please enter a valid option")
                continue


def add_task():
    title = input("Enter task title: ").strip()
    status = "pending"

    with open("tasks.txt", "a") as f:
        _ = f.write(f"{title} \t\t {status}\n")


if __name__ == "__main__":
    main()
