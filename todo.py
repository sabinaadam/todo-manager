import argparse
import json
import os
from datetime import datetime

FILE = "tasks.json"
PRIORITIES = ["low", "medium", "high"]


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(tasks, text, priority=None, deadline=None):
    new_task = {
        "text": text,
        "done": False,
        "priority": priority,
        "deadline": deadline,
    }
    tasks.append(new_task)
    return tasks


def complete_task(tasks, index):
    tasks[index]["done"] = True
    return tasks


def delete_task(tasks, index):
    tasks.pop(index)
    return tasks


def show_tasks(tasks, filter_status=None):
    """filter_status: None = all, "open" or "done" """
    for i, task in enumerate(tasks):
        status = "done" if task["done"] else "open"
        if filter_status and status != filter_status:
            continue
        check = "x" if task["done"] else " "

        extra = []
        if task.get("priority"):
            extra.append(f"priority: {task['priority']}")
        if task.get("deadline"):
            extra.append(f"due: {task['deadline']}")
        extra_text = f" ({', '.join(extra)})" if extra else ""

        print(f"[{check}] {i}: {task['text']}{extra_text}")


def main():
    parser = argparse.ArgumentParser(description="Simple to-do manager")
    subparser = parser.add_subparsers(dest="command", required=True)

    add_parser = subparser.add_parser("add", help="add a new task")
    add_parser.add_argument("text")
    add_parser.add_argument("--priority", choices=PRIORITIES, default=None)
    add_parser.add_argument("--deadline", default=None, help="format: DD-MM-YYYY, e.g. 20-08-2026")

    list_parser = subparser.add_parser("list", help="show tasks")
    list_parser.add_argument("--status", choices=["open", "done"], default=None)

    done_parser = subparser.add_parser("done", help="mark a task as done")
    done_parser.add_argument("index", type=int)

    delete_parser = subparser.add_parser("delete", help="delete a task")
    delete_parser.add_argument("index", type=int)

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == "add":
        if args.deadline:
            try:
                datetime.strptime(args.deadline, "%d-%m-%Y")
            except ValueError:
                print("Invalid deadline. Please use the format DD-MM-YYYY, e.g. 20-08-2026.")
                return
        add_task(tasks, args.text, args.priority, args.deadline)
        save_tasks(tasks)
        print(f"Task added: {args.text}")

    elif args.command == "list":
        show_tasks(tasks, args.status)

    elif args.command == "done":
        try:
            complete_task(tasks, args.index)
            save_tasks(tasks)
            print(f"Task {args.index} marked as done.")
        except IndexError:
            print(f"No task with index {args.index}.")

    elif args.command == "delete":
        try:
            delete_task(tasks, args.index)
            save_tasks(tasks)
            print(f"Task {args.index} deleted.")
        except IndexError:
            print(f"No task with index {args.index}.")

if __name__ == "__main__":
    main()