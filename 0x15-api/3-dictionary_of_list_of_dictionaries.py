#!/usr/bin/python3
"""
    Using this REST API, for a given employee ID,
    export data in the JSON format.
"""
import csv
import requests
from json import dump
from sys import argv


if __name__ == "__main__":
    """ My main function """
    url = "https://jsonplaceholder.typicode.com"
    user = f"{url}/users/{id}"
    todo = f"{url}/todos?userId={id}"

    employee = requests.get(user).json()
    tasks = requests.get(todo).json()

    all_dict = {}
    for emp in employee:
        tasks_list = []
        uname = emp['username']
        for task in tasks:
            if task['userId'] == emp['id']:
                status = task['completed']
                tasks_list.append({"username": uname, "task": task['title'],
                                  "completed": status})
        all_dict[emp['id']] = tasks_list

    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        dump(all_dict, jsonfile)
