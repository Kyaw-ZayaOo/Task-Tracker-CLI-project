import json
import datetime
import sys

#to open the json file in different functions
def open_json_file():
    try:
        with open("task_data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks
#adding tasks 
def add(task_description):
    #Opening the Json file by using the function.........
    tasks = open_json_file()
    next_id = max([task["id"] for task in tasks]) + 1 if tasks else 1
    data = {"id": next_id,
            "description":task_description,
            "status": "to do",
            "createdAt": f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "updatedAt": f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" }

    tasks.append(data)
    # Save the updated list back to the file
    with open("task_data.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print(f'Task added successfully (ID: {data['id']})')

def to_mark_progress(id):      
    tasks = open_json_file()
    #iteration the list and ......
    for task in tasks:
            if task['id'] == id:
                task['status']= "in progress"
                task['updatedAt']= f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                with open("task_data.json", "w") as file:
                    json.dump(tasks, file, indent=4)
                print(f'Marked the task {tasks[id-1]["description"]} as in progress')
                break
#the same with to_mark_progress function
def to_mark_done(id):
    tasks = open_json_file()

    for task in tasks:
        for keys,values in task.items():
            if values == id:
                task["status"] = "done"
                task["updatedAt"] = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                with open("task_data.json", "w") as file:
                    json.dump(tasks, file, indent=4)
                print(f'Marked the task {tasks[id-1]["description"]} as done')
                break
#to change
def display(filter_task=None):
    valid_task_type = ['done','todo','in-progress']
    tasks = open_json_file()
    if filter_task:
        if filter_task in valid_task_type:
            filtered_tasks = [task for task in tasks if task['status'] == filter_task]
        else:
            print(f'{filter_task} is not Valid. Valid filter status are ', ', '.join(valid_task_type))
            return
    else:
        filtered_tasks = tasks

    if filtered_tasks:
        for task in filtered_tasks:
            print(f"Description: {task['description']}")
            print((f"Status: {task['status']}"))
            print((f"CreatedAt: {task['createdAt']}"))
            print(f"UpdatedAt: {task['updatedAt']}")
    else:
        if filter_task is None:
            print('Thre is not tasks.')
        else:
            print(f'There is no {filter_task}')

def update(user_input,new_description):
    tasks = open_json_file()
    for task in tasks:
        if task['id'] == user_input:
            task['description'] = new_description
            task["updatedAt"] = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            with open("task_data.json", "w") as file:
                json.dump(tasks, file, indent=4)
        
def delete(id):
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
    if len(sys.argv) < 2:
        print("Usage: python task-cli.py <command> [args]")
        print("Commands:")
        print("  add \"<description>\"")
        print("  update <id> \"<new description>\"")
        print("  delete <id>")
        print("  mark-in-progress <id>")
        print("  mark-done <id>")
        print("  list [todo|in-progress|done]")
        return

    command = sys.argv[1]
    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py add \"<description>\"")
            return
        description = sys.argv[2]
        add(description)

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: python task-cli.py update <id> \"<new description>\"")
            return 
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        new_description = sys.argv[3]
        update(task_id, new_description) 

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        delete(task_id)      

    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py mark-in-progress <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        to_mark_progress(task_id, 'in-progress') 

    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py mark-done <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        to_mark_done(task_id, 'done')

    elif command == 'list':
        status_filter = None
        if len(sys.argv) == 3:
            status_filter = sys.argv[2].lower()
        elif len(sys.argv) > 3:
            print("Usage: python task-cli.py list [todo|in-progress|done]")
            return
        display(status_filter)

    else:
        print(f"Unknown command: '{command}'")
        print("Please use one of: add, update, delete, mark-in-progress, mark-done, list")


if __name__== "__main__":
    main()


    