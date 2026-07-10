# #? PRACTICE TASK
# def repeat(num):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(num=5)
# def greet(name):
#     print(f"Привет, {name}!")

# greet("Алексей")
# from random import choice
# players = ["Амрулло", "Мухаммад", "Аббос",'Муродали','Кавсар','Надим']
# winner = choice(players)
# print(f"Победил {winner}")

# import random

# def guess_game():
#     secret_num = random.randint(1, 20)
#     attempts = 0
#     while True:
#         try:
#             user_guess = int(input("Угадай число от 1 до 20: "))
#             attempts += 1
#             if user_guess == secret_num:
#                 print(f"Победа! Вы угадали за {attempts} попыток!")
#                 break
#             elif user_guess < secret_num:
#                 print("Загаданное число больше.")
#             else:
#                 print("Загаданное число меньше.")
#         except ValueError:
#             print("Пожалуйста, введите корректное число.")

# guess_game()
#? ---------------
#! TASK 1 - 3
#^ TASK 4 - 6
#= TASK 7 - 9
#- TASK 10 - 14
#? ----------------
#! CLASS TASK 1:
# import datetime

# print(datetime.datetime.now())
#! CLASS TASK 2:
# from datetime import datetime

# print(datetime.now().strftime('%d-%b-%Y %I:%M:%S %p'))
#! CLASS TASK 3:
# from datetime import datetime

# date = datetime(2025, 1, 15)
# print(f"Day of the week: {date.strftime('%A')}")
#^ CLASS TASK 4:
# from datetime import datetime

# dt = datetime(2025, 6, 15, 10, 30, 45)
# print(dt.strftime("%Y-%m-%d %H:%M:%S"))
#^ CLASS TASK 5:
# from datetime import datetime

# dt = datetime(2025, 8, 20, 14, 35, 50)
# print("Year:", dt.year)
# print("Month:", dt.month)
# print("Day:", dt.day)
# print("Hour:", dt.hour)
# print("Minute:", dt.minute)
# print("Second:", dt.second)
#^ CLASS TASK 6:
# import datetime
# now = datetime.datetime.now()
# print(f"Current time: {now.strftime('%I:%M %p')}")
#= CLASS TASK 7:
# from datetime import datetime
# now = datetime.now()
# print(f"Current time: {now.strftime('%H:%M:%S.%f')[:-3]}")
#= CLASS TASK 8:
# from datetime import datetime
# date = datetime(2025, 3, 15)
# print(f"Day of the year: {date.timetuple().tm_yday}")
#= CLASS TASK 9:
# from datetime import date, time, datetime
# d = date(2025, 5, 20)
# t = time(9, 45, 0)
# combined = datetime.combine(d, t)
# print(f"Combined datetime: {combined}")
#- CLASS TASK 10:
# from datetime import datetime
# date_string = "20 January, 2025"
# dt_object = datetime.strptime(date_string.replace(",", ""), "%d %B, %Y")
# print(dt_object)
#- CLASS TASK 11:
# from datetime import datetime, timedelta
# date = datetime(2025, 3, 15)
# result = date - timedelta(days=7)
# print(result)
#- CLASS TASK 12:
# from datetime import datetime, timedelta
# date = datetime(2025, 3, 15)
# result = date + timedelta(days=7)
# print(result)
#- CLASS TASK 13:
# from datetime import datetime
# date1 = datetime(2025, 1, 1)
# date2 = datetime(2025, 3, 15)
# days_diff = abs((date2 - date1).days)
# print("Days between dates:", days_diff)
#- CLASS TASK 14:
# from datetime import datetime
# timestamp = 1672531200
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object.strftime("%Y-%m-%d %H:%M:%S"))
#todo: RANDOM TASK
#^ RANDOM TASK 1:
# import random
# n = int(input())
# arr = [random.randint(1, n) for _ in range(n)]
# print(arr)
# random.shuffle(arr)
# print(arr)
#^RANDOM TASK 2:
