import sys

help_message = """
usage: todo [OPTIONS]
    -list            List current tasks
    -add taskname    Add a new task
    -done task_id    Mark a task as done
"""

if len(sys.argv) == 1:
    sys.exit(help_message)


def sanity_check(arg):
    if arg[1] == "-add" and len(sys.argv) == 2:
        sys.exit("Gotta provide that title buddy")
    elif arg[1] == "-done" and len(sys.argv) == 2:
        sys.exit("Gotta provide that id buddy")


sanity_check(sys.argv)

command = sys.argv[1]


def list_tasks():
    print("Hello tasks")


def add_task(title: str):
    print(f"Hello task {title}")


def mark_task(id: str):
    print(f"Hello task with id {id}")


match command:
    case "-list":
        print("Hello tasks")
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
