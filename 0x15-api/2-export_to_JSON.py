#!/usr/bin/python3
""" JSON MANIPULATION API STUFF """

import json
import requests
import sys

ENDPOINT = 'https://jsonplaceholder.typicode.com/users/'

if __name__ == '__main__':
    # DEAR GOD
    user_id = sys.argv[1]
    user = ENDPOINT + user_id

    response = requests.get(user)
    user_name = response.json().get('username')

    task = user + '/todos'
    response = requests.get(task)

    all_tasks = response.json()

    datationary = {user_id: []}

    for task in all_tasks:
        completed = task.get('completed')
        title_task = task.get('title')            
        datationary[user_id].append({
                                  "task": title_task,
                                  "completed": completed,
                                  "username": user_name})

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(datationary, f)
