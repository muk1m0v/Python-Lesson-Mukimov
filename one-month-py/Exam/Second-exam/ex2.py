# '''
# 🇷🇺 Русский
# Напишите функцию:

# count_words(text)
# Функция получает строку, состоящую из слов, разделённых пробелами.

# Выведите количество слов в строке.

# Input
# lorem ipsum dolor
# Output
# 3
# '''
# #?----------------------
# #? task 1
# def count_words(text):
#     return len(text)

# lict = input('Enter the text: ').split()

# print(count_words(lict))
# #?-----------------------
# '''
# 🇷🇺 Русский
# Напишите функцию:

# longest_word(text)
# Функция получает строку.

# Выведите:

# Самое длинное слово
# Его длину
# Если таких слов несколько, выведите первое.

# Input
# one two three four five six
# Output
# three
# 5
# '''
# #?----------------------
# #? task 2
# def longest_word(text):
#     words = text.split()
#     max_word = ''
#     max_length = 0

#     for word in words:
#         if len(word) > max_length:
#             max_length = len(word)
#             max_word = word

#     print(f"Самое длинное слово: {max_word}")
#     print(f"Его длина: {max_length}")

# longest_word(str(input()))
# #?------------------------
# '''
# 🇷🇺 Русский
# Напишите функцию:

# smallest_odd(numbers)
# Функция получает список целых чисел.

# Верните наименьшее нечётное число.

# Если нечётных чисел нет, верните 0.

# Input
# 0 1 2 3 4
# Output
# 1
# '''
# #?----------------------
# #? task 3
# def smallest_odd(numbers):
#     for num in numbers:
#         if num % 2 != 0:  
#             return num
#     return 0 

# new = input('Enter the numder: ').split()
# numbers = []

# for i in new:
#     num = int(i)
#     numbers.append(num)
# print(smallest_odd(numbers))
# #?----------------------
# '''
# Unique Visitors (SET)
# 🇷🇺 Русский
# Напишите функцию:

# unique_visitors(visitors)
# Функция получает список посетителей сайта.

# Верните количество уникальных посетителей.

# Input
# ["Ali", "Ali", "Sara", "Kamol"]
# Output
# 3
# '''
# #?----------------------
# #? Task 4
# def unique_visitors(visitors):
#     return len(set(visitors))

# print(unique_visitors(["Ali", "Ali", "Sara", "Kamol"]))
# #?----------------------
# '''
# 🇷🇺 Русский
# Напишите функцию:

# vowel_sum(text)
# Используйте словарь:

# {
#     "A": 4,
#     "E": 3,
#     "I": 1,
#     "O": 0,
#     "U": 0
# }
# Посчитайте и верните сумму гласных.

# Input
# Do I get the correct output?
# Output
# 10
# '''
# #?---------------------
# #? task 5
# #todo: Нафахмидим:(
# #?---------------------
# '''
# 🇷🇺 Русский
# Напишите функцию:

# censor_words(text)
# Замените каждое слово длиной более 4 символов на:

# *****
# Верните изменённую строку.

# Input
# The code is fourty
# Output
# The code is *****
# '''
# #?-------------------
# #? task 6
# def censor_words(text):
#     if len(text) >= 4:
#         for i in text:
#             i = '*'
#     return text

# text = input('Enter the text: ')
# print(censor_words(text))
# просто принтиш карда натонистим
# #?--------------------
# '''
# 🇷🇺 Русский
# Напишите функцию:
# common_friends(user1, user2)
# Верните всех общих друзей.

# Input
# {"Ali", "Sara", "Kamol"}
# {"Sara", "Madina", "Ali"}
# Output
# {"Ali", "Sara"}
# '''
# #?----------------
# #? task 7
# def price(products, name):
#     if name in products:
#         return products[name]
#     else:
#         return "Not Found"

# products = {
#     "Laptop": 8000,
#     "Mouse": 150
# }

# print(price(products, "Laptop"))
# print(price(products, "Keyboard"))
# #?----------------
# #?-----------------
# # #? task 8
# def common_friends(user1, user2):
    
#     ok = set(user1)
#     good = set(user2)

#     common = ok.intersection(good)

#     return list(common)

# user1_friends = {"Ali", "Sara", "Kamol"}
# user2_friends = {"Sara", "Madina", "Ali"}
# print(common_friends(user1_friends, user2_friends))
# #?-------------------
# def report(main):
#     if not main:
#         return None, 0
#     best_employee = None
#     best_tasks = -99999999
#     for name, tasks in main.items():
#         if tasks > best_tasks:
#             best_tasks = tasks
#             best_employee = name
#     return best_employee, best_tasks


# data = {
#     "Ali": 15,
#     "Sara": 22,
#     "Kamol": 18,
#     "Madina": 20
# }
# name, tasks = report(data)
# print(name)
# print(tasks)