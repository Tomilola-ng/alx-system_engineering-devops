#!/usr/bin/python3
""" EMPLOYEE DATA GATHER """

import re
import requests
import sys

ENDPOINT = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            idx = int(sys.argv[1])
            response = requests.get(f'{ENDPOINT}/users/{idx}').json()
            results = requests.get(f'{ENDPOINT}/todos').json()
            employee = response.get('name')
            all_tasks = list(filter(lambda x: x.get('userId') == idx, results))
            done_tasks = list(filter(lambda x: x.get('completed'), all_tasks))
            print(
                f'Employee {employee} is done with tasks({len(done_tasks)}/{len(all_tasks)}):'
            )
            if len(done_tasks) > 0:
                for task in done_tasks:
                    print(f'\t {task.get('title')}')
