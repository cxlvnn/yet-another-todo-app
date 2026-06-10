import sys

with open("Tasks.txt", "r") as f:
    lines = f.readlines()
    if not lines:
        sys.exit
    else:
        line = lines[-1]
        character = line.find(".")
        id = line[:character] or 0
        print(id, end="")
