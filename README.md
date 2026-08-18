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
<img width="737" height="66" alt="1" src="https://github.com/user-attachments/assets/669b2744-1947-49ab-8d0d-08196c1444dd" />
<img width="1155" height="78" alt="2" src="https://github.com/user-attachments/assets/d3b233fe-0a8e-4c22-8b13-0c694b62c4d4" />
<img width="812" height="123" alt="3" src="https://github.com/user-attachments/assets/26619060-f1f4-4965-859f-1a43f02e9da0" />
<img width="547" height="97" alt="4" src="https://github.com/user-attachments/assets/7756b2ff-a9c7-4a17-809e-75a06e9339e3" />
<img width="674" height="139" alt="5" src="https://github.com/user-attachments/assets/291e69a9-aad6-4b5d-ad37-77822363b778" />
<img width="706" height="148" alt="6" src="https://github.com/user-attachments/assets/584e0862-0f4e-4508-8ff0-cd18d2827f6e" />





