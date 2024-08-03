#!/usr/bin/python3

""" Gather Data from an API"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)

    print(
        f"Employee {user['name']} is done with tasks"
        f"({len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")
