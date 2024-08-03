#!/usr/bin/python3

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    tasks = [{"task": todo["title"], "completed": todo["completed"], "username": user["username"]} for todo in todos]
    with open(f"{employee_id}.json", mode='w') as file:
        json.dump({employee_id: tasks}, file)
