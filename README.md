# To-Do Manager

A simple command-line tool to manage tasks.

## What it does

- Add tasks
- Mark tasks as done
- Delete tasks
- List tasks, optionally filtered by status (open/done)
- Optionally set a priority (low / medium /high) and a deadline for a task
- Tasks are saved in a JSON file ('tasks.json')

## Technologies / concepts used

- Python 3, standard library only
- 'argparse' for the command-line interface
- 'json' for reading/writing task data
- 'datetime' for validating the deadline format
- Basic error handling ('try'/'except IndexError') for invalid task indexes

## How to run

Requires Python 3.

# add a task
python todo.py add "Practice Python"

# add a task with priority and deadline
python todo.py add "Write application" --priority high --deadline 20-08-2026

# list all tasks
python todo.py list

# mark a task as done (use the index shown by 'list')
python todo.py done 0

# list only open tasks
python todo.py list --status open

# delete a task
python todo.py delete 0

## Screenshots

<img width="1241" height="588" alt="7" src="https://github.com/user-attachments/assets/55acdc01-2b52-43bb-b14a-b15fdf58ece5" />





