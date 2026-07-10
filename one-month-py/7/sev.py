# #! Class - Work
# students = [
#     {"Name": "Muhammad", "Surname": "Muqimov", "Age": 16},
#     {"Name": "Abbos   ", "Surname": "Vasidov", "Age": 18},
#     {"Name": "Mustafo ", "Surname": "Hasanov", "Age": 14}
# ]
# print('Name        Surname  Age')
# for st in students:
#     print(f"{st['Name']}    {st['Surname']}  {st['Age']}")
# #? task 1
# """
# 1. create an empty dict
# 2.add key name value ---> Muhammad to the dict
# 3.update value of name to mansur
# 4.Delete an element with key name
# """
# empty_dict = {}
# list_empty_for_dict = [empty_dict]

# lem = list_empty_for_dict
# dem = empty_dict

# user_commands = str(input("Enter your command: "))
# run = user_commands

# match run:
#     case "add":
#         add = lem.append(run)
#         str(input("Enter add name: "))
#         print()
# print('simple test:' \
# 'example: task 1 
#todo: tema list tasks
#! Легкий уровень
# #? task 1
# user_input = input("Enter your number: ").split()
# l = len(user_input)
# sup = user_input

# sum = 0
# for  i in range(l):
#     sum+=int(sup[i])

# print(sum)
# #? task 2
# user_list = input("Enter your number: ").split()
# num = input("Second num: ")
# my = user_list

# if num in my:
#     print("Number found!!!")
# else:
#     print("Number not found!!!")
# #? task 3
# numbers = input("Enter your number: ").split()
# squares = []

# for num in numbers:
#     squares.append(int(num) ** 2)

# print(squares)
#* Задачи со словарями(dict):
# #? task 1
# user_input = input('Enter numbers: ')
# numbers = [int(num) for num in user_input.split()]
# counts = {}

# for num in numbers:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1

# print(counts)
# #? task 2
# my_dict = {"apple": 5, "banana": 3, "orange": 2, "watermelon": 4, "melon": 7}
# search_key = str(input("Enter your text: "))

# if search_key in my_dict:
#     print(f"Key({search_key}) found!!")
# else:
#     print(f"Key({search_key}) not found!")
#? task 3