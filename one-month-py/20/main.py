from tasks import *
tasks = []
user_db = []
user_logined = None
while True:
    if user_logined == None:
        n = 
    n = input('1 - Add Tasks\n2 - View All Tasks\n3 - View By ID\n4 - Delete Tasks By ID\n5 - Update Tasks By ID\n0 - Exit\n-----------\nChoice: ')
    if n == '1':
        add_task()
    elif n == '2':
        show_all()
    elif n == '3':
        print(get_by_id(int(input('Enter the tasks id: '))))
    elif n == '4':
        print(delete_by_id(int(input('Enter the id tasks by delete: '))))
    elif n == '5':
        print(update_by_id(int(input('Enter the id tasks by update: '))))
    elif n == '0':
        if n == 'stop':
            print()
        print('')
        break
    else:
        print('Invalid input enter the 0 to 5')