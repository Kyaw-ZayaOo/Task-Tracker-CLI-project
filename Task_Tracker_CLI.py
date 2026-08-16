import json
import datetime

#to open the json file in different functions
def open_json_file():
    try:
        with open("task_data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks
#adding tasks 
def add():
    #check the user's input
    while True:
        task_description = input('Task Description - ')
        if task_description:
            break
        else:
            print('Task Description should not be empty!')

    #Opening the Json file by using the function.........
    tasks = open_json_file()
    next_id = max([task["id"] for task in tasks]) + 1 if tasks else 1
    data = {"id": next_id, #I think assiging the ID will be the problem when we delete one task. Will be great if it updates along with the list
            "description":task_description,
            "Status": "to do",
            "createAt": f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "updateAt": f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" }

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
    tasks = open_json_file()
    #iteration the list and ......
    for task in tasks:
            if task['id'] == id:
                task['Status']= "in progress"
                task['updateAt']= f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                with open("task_data.json", "w") as file:
                    json.dump(tasks, file, indent=4)
                print(f'Marked the task {tasks[id-1]["description"]} as in progress')
                break
#the same with to_mark_progress function
def to_mark_done():
    while True:
        id = input('Task ID: ')
        if id and id.isdigit():
            id = int(id)
            break
        else:
            print('Id is not valid')

    tasks = open_json_file()

    for task in tasks:
        for keys,values in task.items():
            if values == id:
                task["Status"] = "done"
                task["updateAt"] = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                with open("task_data.json", "w") as file:
                    json.dump(tasks, file, indent=4)
                print(f'Marked the task {tasks[id-1]["description"]} as done')
                break

def display():

    def display_done_tasks():
        done_list = []
        tasks = open_json_file()
        for task in tasks:
            if task["Status"] == 'done':
                done_list.append(task) 
        if done_list:            
            for n,task in enumerate(done_list, start=1):
                print(n,'.', task)
        else:
            print('There is no done tasks.')

    def display_inprogress_tasks():
        inprogress_list = []
        tasks = open_json_file()
        for task in tasks:
            if task['Status'] == "in progress":
                inprogress_list.append(task)

        if inprogress_list:            
            for n,task in enumerate(inprogress_list, start=1):
                print(n,'.', task)
        else:
            print('There is no in progress tasks.')                    
    def display_todo_tasks():
        todo_list = []
        tasks = open_json_file()
        for task in tasks:
            if task['Status'] == 'to do':
                todo_list.append(task)
        if todo_list:            
            for n,task in enumerate(todo_list, start=1):
                print(n,'.', task)
        else:
            print('There is no todo tasks.')

    print("1.Display Done Tasks'\n2.Display Todo Tasks\n3.Display In-progress Tasks")
    user_choice = input('Choose 1 to 3.')
    if user_choice == '1':
        display_done_tasks()
    elif user_choice == '2':
        display_todo_tasks()

    elif user_choice == '3':
        display_inprogress_tasks()

    else:
        print(f'{user_choice} is not valid. Please choose from 1 to 3.')

def update():
    while True:
        user_input = input('Task ID: ')
        if user_input and user_input.isdigit():
            user_input = int(user_input)
            break
        else:
            print('Id is not valid')
    new_description = input('Update Task: ')
    tasks = open_json_file()

    for task in tasks:
        if task['id'] == user_input:
            task['description'] = new_description
            task["updateAt"] = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            with open("task_data.json", "w") as file:
                json.dump(tasks, file, indent=4)
        
def delete():
    while True:
        id = input('Task ID: ')
        if id and id.isdigit():
            id = int(id)
            break
        else:
            print('Id is not valid')
    tasks = open_json_file()
    initial_len = len(tasks)
    remaining_tasks = [task for task in tasks if task['id'] != id]
    if len(remaining_tasks) < initial_len:
        with open("task_data.json", "w") as file:
            json.dump(remaining_tasks, file, indent=4)
        print('Task has been deleted.')
    else:
        print('Task id is not found')

def main():
    is_running = True
    while is_running:
        print("1. To View the tasks " \
            "\n2. Add Task " \
            "\n3. To mark in Progress " \
            "\n4. To mark Done " \
            "\n5. To delete"\
            "\n6. To update the task" )
        user_choice = input('Choose from 1 to 6')
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

            elif user_choice == '6':
                update()

            else:
                print('Please choose form 1 to 5.')
        else:
            print('Cannot be empty')

        exit = input('Exit?(y/n)').strip().lower()
        if exit == "y":
            break
        
if __name__== "__main__":
    main()


    