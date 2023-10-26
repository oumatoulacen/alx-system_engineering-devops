#!/usr/bin/python3
""" Python script to export data in the JSON format. """

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    name = (requests.get(url + "/users/{}".format(argv[1])).json().get("name"))
    todos = requests.get(url + "/user/{}/todos".format(argv[1])).json()
    with open("{}.json".format(argv[1]), mode="w") as f:
        row_list = []
        data = {}
        for todo in todos:
            row = {}
            row['task'] = todo.get("title")
            row['completed'] = todo.get("completed")
            row['username'] = name
            row_list.append(row)
        data[argv[1]] = row_list
        json.dump(data, f)
