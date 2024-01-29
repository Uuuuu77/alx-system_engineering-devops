#!/usr/bin/python3
"""
    Using this REST API, for a given employee ID,
    export data to json file.
"""
import csv
import requests
from json import dump
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
    uname = employee['username']

    tasks_list = []
    for task in tasks:
        status = task['completed']
        tasks_list.append({"task": task['title'],
                          "completed": status, "username": uname})
    tasks_dict = {id: tasks_list}
    filename = f"{id}.json"
    with open(filename, 'w') as jsonfile:
        dump(tasks_dict, jsonfile)
