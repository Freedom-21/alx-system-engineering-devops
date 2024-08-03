#!/usr/bin/python3

""" Export to CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = \
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [
                    employee_id,
                    user['username'],
                    todo['completed'],
                    todo['title']
                ]
            )
