#!/usr/bin/python3

""" Dictionary of list of dictionaries"""

import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    data = {}
    for user in users:
        user_tasks = [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            }
            for todo in todos if todo["userId"] == user["id"]
        ]
        data[user["id"]] = user_tasks

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(data, file)
