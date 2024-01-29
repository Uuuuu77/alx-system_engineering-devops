#!/usr/bin/python3
"""
    Using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ My main function """
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = f"{url}/users/{id}"
    todo = f"{url}/todos?userId={id}"

    employee = requests.get(user).json()
    tasks = requests.get(todo).json()

    name = employee['name']
    total = len(tasks)
    done = [task for task in tasks if task['completed']]

    print(f"Employee {name} is done with tasks({len(done)}/{total}):")
    for dn in done:
        print(f"\t {dn['title']}")
