import sys

help_message = """
usage: todo [OPTIONS]
    -list            List current tasks
    -add taskname    Add a new task
    -done task_id    Mark a task as done
"""

if len(sys.argv) == 1:
    sys.exit(help_message)


def sanity_check[T](arg: list[T]):
    if arg[1] == "-add" and len(sys.argv) == 2:
        sys.exit("Gotta provide that title buddy")
    elif arg[1] == "-done" and len(sys.argv) == 2:
        sys.exit("Gotta provide that id buddy")


sanity_check(sys.argv)

command = sys.argv[1]


lines = None


def list_tasks():
    with open("Tasks.txt", "r") as f:
        print("Tasks")
        print("----------------------------")
        for line in f:
            print(line, end="")
        print("----------------------------")


def add_task(title: str):

    id = 0
    with open("Tasks.txt", "r") as f:
        lines = f.readlines()
    if not lines:
        sys.exit
    else:
        line = lines[-1]
        character = line.find(".")
        id = int(line[:character]) or 0
        id += 1

    with open("Tasks.txt", "a") as f:
        _ = f.write(f"{id}.{title}:pending\n")


def mark_task(id: str):
    with open("Tasks.txt", "r") as f:
        lines = f.readlines()


match command:
    case "-list":
        list_tasks()
    case "-add":
        add_task(sys.argv[2])
    case "-done":
        mark_task(sys.argv[2])
    case _:
        print(f"Hello {command}")

# class Task:
#     def __init__(self, title: str, status: str = "Pending"):
#         self.title = title
#         self.status = status
