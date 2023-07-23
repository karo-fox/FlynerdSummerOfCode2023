import datetime
import os


PATH = "week3/project/backup.txt"


def save(tasks):
    with open(PATH, "w") as file:
        for idx, task in tasks.items():
            file.write(
                f'{idx};{task["name"]};{task["done"]};{task["description"]};{task["date"]}\n'
            )


def add(tasks):
    name = input("Task name: ")
    description = input("Task description: ")
    date = input("Due date [YYYY-MM-DD]: ")
    tasks[len(tasks)] = {
        "name": name,
        "done": False,
        "description": description,
        "date": datetime.date.fromisoformat(date),
    }

    print("Task was added!")

    return tasks


def mark_as_done(tasks):
    idx = int(input("Task number: "))
    tasks[idx]["done"] = True

    print("Task was marked as done")

    return tasks


def list_tasks(tasks):
    for idx, task in tasks.items():
        mark = "√" if task["done"] else "X"
        print(f'{idx} \t[{mark}]\t{task["name"]}')
        print(f'due: {task["date"]}')
        print(task["description"])

    ui = input("\n[m] - mark task as done\n[b] - go back\n\n")
    if ui == "m":
        tasks = mark_as_done(tasks)

    return tasks


def read_backup():
    if os.path.exists(PATH):
        tasks = {}
        with open(PATH) as file:
            content = file.readlines()
        for line in content:
            line = line.strip().split(";")
            tasks[line[0]] = {
                "name": line[1],
                "done": line[2] == "True",
                "description": line[3],
                "date": datetime.date.fromisoformat(line[4]),
            }
    else:
        tasks = {
            0: {
                "name": "example",
                "done": False,
                "description": "test",
                "date": datetime.date.today(),
            }
        }
    return tasks


tasks = read_backup()
while True:
    ui = input("\n[l] - list all tasks\n[a] - add task\n[q] - quit\n\n")
    if ui == "l":
        tasks = list_tasks(tasks)
    if ui == "a":
        tasks = add(tasks)
    if ui == "q":
        save(tasks)
        break
