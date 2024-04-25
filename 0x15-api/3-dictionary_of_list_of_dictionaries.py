#!/usr/bin/python3
""" JSON MANIPULATION API STUFF """

import json
import requests

ENDPOINT = 'https://jsonplaceholder.typicode.com/users/'

if __name__ == '__main__':
    response = requests.get(ENDPOINT)
    Users = response.json()

    datationary = {}
    for user in Users:
        user_id = user.get('id')
        user_name = user.get('username')
        NEW_ENDPOINT = f'{ENDPOINT}{user_id}/todos/'
        response = requests.get(NEW_ENDPOINT)

        tasks = response.json()
        datationary[user_id] = []

        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            datationary[user_id].append({
                                    "task": title_task,
                                    "completed": completed,
                                    "username": user_name
                                })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(datationary, f)
