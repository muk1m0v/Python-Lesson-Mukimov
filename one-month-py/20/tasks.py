from datetime import *

tasks = []
cnt = 0

def add_task():
    global cnt
    cnt += 1
    new_tasks = {
        'id': cnt,
        'user': input('-----------\nUsername: '),
        'title': input('Title: '),
        'is_completed': False,
        'due_date': datetime.strptime(input('time: '), "%d-%m-%Y %H:%M")
    }
    tasks.append(new_tasks)

def show_all():
    for task in tasks:
        print(f"""
id: {task['id']}
User: {task['user']}
Title: {task['title']}
is_completed: {task['is_completed']}
due_date: {task['due_date']}
""")

def delete_by_id(id):
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            return f"Task with ID {id} successfully deleted."
    return f"NOT Found Task with ID: {id}"

def get_by_id(id):
    for task in tasks:
        if task['id'] == id:
            return f"""
id: {task['id']}
Username: {task['user']}
Title: {task['title']}
Due Date: {task['due_date']}
"""
    return f'NOT Found Task With ID: {id}'

def update_by_id(id):
    for task in tasks:
        if task['id'] == id:
            new_title = input("New Title: ")
            if new_title:
                task['title'] = new_title
            new_due = input("New due date: ")
            if new_due:
                task['due_date'] = datetime.strptime(new_due, "%d-%m-%Y %H:%M")
            new_completed = input("Is completed? (Y/N, press Enter to keep current): ")
            if new_completed:
                if new_completed.lower() == 'Y':
                    task['is_completed'] = 'y'
                elif new_completed.lower() == 'N':
                    task['is_completed'] = 'n'
                else:
                    print("Invalid input, keeping current status.")
            return f"Task with ID {id} updated successfully."
    return f"NOT Found Task with ID: {id}"