#!/usr/bin/python3
""" CSV MANIPULATION """

import csv
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

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        # HERE WE GO
        for task in all_tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, user_name, completed, title_task))
