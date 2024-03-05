#!/usr/bin/python3
"""Import request module."""
import csv
import requests
from sys import argv


def exportCsv():
    """Returns information about his/her TODO list progress."""
    api = "https://jsonplaceholder.typicode.com/"
    if len(argv) > 1:
        id = int(argv[1])
        reqTodo = requests.get('{}todos'.format(api), params={'userId': id}).json()
        reqUser = requests.get('{}users/{:d}'.format(api, id)).json()

        with open('{}.csv'.format(id), 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in reqTodo:
                writer.writerow([
                    '{}'.format(field) for field in (
                        todo.get('userId'),
                        reqUser.get('username'),
                        todo.get('completed'),
                        todo.get('title')
                    )
                ])


if __name__ == "__main__":
    exportCsv()
