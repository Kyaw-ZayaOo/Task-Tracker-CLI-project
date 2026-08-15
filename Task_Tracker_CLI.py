import json
import datetime


def add():
    while True:
        task_description = input('Task Description - ')
        if task_description:
            break
        else:
            print('Task Description should not be empty!')
    try:
        with open("task_data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    data = {"id": len(tasks) + 1,
            "description":task_description,
            "Status": "todo",
            "createAt": f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}",
            "updateAt": None}

    tasks.append(data)
    # Save the updated list back to the file
    with open("task_data.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print(f'Task added successfully (ID: {data['id']})')

def to_mark_progress():
    while True:
        id = input('Task ID: ')
        if id and id.isdigit():
            id = int(id)
            break
        else:
            print('Id is not valid')
    try:
        with open("task_data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    if id <= len(tasks):
        for task in tasks:
            for values in task.values():
                if values == id:
                    tasks[id-1]["Status"] = "in progress"
                    tasks[id-1]["updateAt"] = f"{datetime.datetime.now()}"
                    with open("task_data.json", "w") as file:
                        json.dump(tasks, file, indent=4)
                    print(f'Marked the task {tasks[id-1]["description"]} as in progress')
                    break
    else:
        print('ID is not vilid.')

def to_mark_done():
    while True:
        id = input('Task ID: ')
        if id and id.isdigit():
            id = int(id)
            break
        else:
            print('Id is not valid')
    try:
        with open("task_data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    if id <= len(tasks):
        for task in tasks:
            for keys,values in task.items():
                if values == id:
                    tasks[id-1]["Status"] = "done"
                    tasks[id-1]["updateAt"] = f"{datetime.datetime.now()}"
                    with open("task_data.json", "w") as file:
                        json.dump(tasks, file, indent=4)
                    print(f'Marked the task {tasks[id-1]["description"]} as done')
                    break
    else:
        print('ID is not vilid.')

def delete():
    pass

def display():
    pass


def main():
    is_running = True
    while is_running:
        print("1. To View the tasks " \
            "\n2. Add Task " \
            "\n3. To mark in Progress " \
            "\n4. To mark Done " \
            "\n5. To delete" )
        user_choice = input('Choose from 1 to 5')
        if user_choice:
            if user_choice == '1':
                display()
            elif user_choice == '2':
                add()
            elif user_choice == '3':
                to_mark_progress()

            elif user_choice == '4':
                to_mark_done()

            elif user_choice == '5':
                delete()

            else:
                print('Please choose form 1 to 5.')
        else:
            print('Cannot be empty')

        exit = input('Exit?(y/n)').strip().lower()
        if exit == "y":
            break
        
if __name__== "__main__":
    main()


    