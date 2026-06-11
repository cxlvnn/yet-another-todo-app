import sys

help_message = """
usage: todo [OPTIONS]
    -list              List current tasks
    -add [taskname]      Add a new task
    -done [task_id]      Mark a task as done
    -delete [task_id]    Delete a task
    -delete all          Delete all tasks
"""

if len(sys.argv) == 1:
    sys.exit(help_message)


def sanity_check[T](arg: list[T]):
    if arg[1] == "-add" and len(sys.argv) == 2:
        sys.exit("Gotta provide that title buddy")
    elif arg[1] == "-done" and len(sys.argv) == 2:
        sys.exit("Gotta provide that id buddy")
    elif arg[1] == "-delete" and len(sys.argv) == 2:
        sys.exit("Gotta provide that id buddy")


sanity_check(sys.argv)

command = sys.argv[1]


def list_tasks():
    with open("Tasks.txt", "r") as f:
        lines = f.readlines()
        print("Tasks")
        print("----------------------------")
        for line in lines:
            print(line, end="")
        if not lines:
            print("Your list is empty")
        print("----------------------------")


def add_task(title: str):
    id = 0
    with open("Tasks.txt", "r") as f:
        lines = f.readlines()
    lines = [l for l in lines if l.strip()]
    if not lines:
        with open("Tasks.txt", "a") as f:
            _ = f.write(f"{id}.{title}:pending\n")
        print("Added task")
        return
    else:
        line = lines[-1]
        character = line.find(".")
        id = int(line[:character])
        id += 1

    with open("Tasks.txt", "a") as f:
        _ = f.write(f"{id}.{title}:pending\n")
    print("Added task")


def mark_task(id: str):
    with open("Tasks.txt", "r") as f:
        lines = f.readlines()
    found = False
    for i, line in enumerate(lines):
        if line.startswith(f"{id}."):
            lines[i] = line.replace(":pending", ":done", 1)
            found = True
            break
    if not found:
        sys.exit(f"No task found with id {id}")
    with open("Tasks.txt", "w") as f:
        f.writelines(lines)
    print(f"Task {id} marked as done")


def delete_task(id: str):
    with open("Tasks.txt", "r") as f:
        lines = f.readlines()
    found = False
    for i, line in enumerate(lines):
        if line.startswith(f"{id}."):
            _ = lines.pop(i)
            found = True
            break
    if not found:
        sys.exit(f"No task found with id {id}")
    with open("Tasks.txt", "w") as f:
        f.writelines(lines)
    print(f"Deleted task with id {id}")


def delete_all():
    with open("Tasks.txt", "w") as f:
        print("Delete all tasks")


match command:
    case "-list":
        list_tasks()
    case "-add":
        add_task(sys.argv[2])
    case "-done":
        mark_task(sys.argv[2])
    case "-delete":
        if sys.argv[2] == "all":
            delete_all()
            sys.exit()
        delete_task(sys.argv[2])
    case _:
        print(help_message)

# class Task:
#     def __init__(self, title: str, status: str = "Pending"):
#         self.title = title
#         self.status = status
