#!/usr/bin/python3
""" module doc """
import json
import requests


def main():
    id = 1
    data_dict = {}

    while True:
        url = "https://jsonplaceholder.typicode.com/"
        users = f"users?id={id}"
        todos = f"todos?userId={id}"
        userData = requests.get(f"{url}{users}").json()

        if not userData:
            break

        userName = userData[0].get("username")
        todosData = requests.get(f"{url}{todos}").json()

        data_dict[id] = [
            {
                "username": userName,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todosData
        ]

        id += 1

    with open("todo_all_employees.json", "w") as f:
        json.dump(data_dict, f)


if __name__ == "__main__":
    main()

"""Using what you did in the task #0, extend your
Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username":
"USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
 "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json

export json format
{ "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
 {"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json


export in CSV as : "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
USER_ID.csv




Employee *NAME* is done with tasks(*DONE*/*TOTAL*):
     *TITLE*
     *TITLE*
     *TITLE*


https://jsonplaceholder.typicode.com/users?id=1
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
https://jsonplaceholder.typicode.com/todos?userId=5
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  ]

https://jsonplaceholder.typicode.com/todos?userId=5&completed=true
https://jsonplaceholder.typicode.com/todos?userId=5&completed=false
  """
