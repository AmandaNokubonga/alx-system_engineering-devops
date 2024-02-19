#!/usr/bin/python3
""" Import request module """
import csv
import requests
from sys import argv


def exportCsv():
    """ returns information about his/her TODO list progress. """
    api = "https://jsonplaceholder.typicode.com/"
    if (len(argv) > 1):
        id = int(argv[1])
        reqTodo = requests.get('{}todos'.format(api),
                               params={'userId': id}).json()
        reqUser = requests.get('{}users/{:d}'.format(api, id)).json()

    with open('{}.csv'.format(id), 'w') as file:
        writer = csv.writer(file, lineterminator='\n', quoting=csv.QUOTE_ALL)
        [writer.writerow(['{}'.format(field)
                          for field in (todo.get('userId'),
                                        reqUser.get('username'),
                                        todo.get('completed'),
                                        todo.get('title')
                                        )])
            for todo in reqTodo]


if _name_ == "_main_":
    exportCsv()
