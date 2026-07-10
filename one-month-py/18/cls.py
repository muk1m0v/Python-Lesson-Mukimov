# #= PRACTICE TASK 
# def my_decorator(func):
#     def wrapper(name) :
#         print("Before a function")
#         func(name)
#         print("After a function")
#     return wrapper

# def upper_decorator(func) :
#     def wrapper(*args, ** kwargs):
#         res = str(func(*args, ** kwargs)).upper()
#         return res
#     return wrapper

# @upper_decorator
# def say_hello(name):
#     return f"salom {name}"

# @upper_decorator
# def say_welcome():
#     return f"Welcome"

# new_function = my_decorator(say_hello)
# new_function("Amrullo")
# print(say_hello(str(input('Enter the name: '))))
# print(say_welcome())

# def sum(a, b):
#     return a + b

# res = lambda a,b: a+b
# print(res(10, 5))
#^ CLASS TASK 1: 
# def avg(*args):
#     result = sum(*args) / len(*args)
#     print(result)
# def mukimov_decorator(func):
#     def wrapper(*args):
#         print('MUKIMOV')
#         return avg(*args)
#     return wrapper

# @mukimov_decorator
# def add_three(a, b, c):
#     return avg(a,b,c)

# print(add_three(10, 20, 5))
#^ CLASS TASK 2:
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('Over')
#         return result
#     return wrapper

# @logger
# def say_hello(name):
#     print(f"Hello {name}")

# say_hello(str(input('Enter the name: ')))
#^ CLASS TASK 3:
# is_logged_in = False

# def login_required(func):
#     def wrapper(*args, **kwargs):
#         if not is_logged_in:
#             print("Ошибка: Вы должны войти в систему!")
#             return None
#         return func(*args, **kwargs)
#     return wrapper

# @login_required
# def view_profile():
#     return "Добро пожаловать в ваш профиль!"

# print("Проверка 1:")
# result = view_profile()
# print("Результат:", result) 

# print("-" * 20)

# is_logged_in = True
# print("Проверка 2:")
# result = view_profile()
# print("Результат:", result)
#- CLASS TASK 4:
# def logger(func):
#     calls = 0

#     def wrapper(*args, **kwargs):
#         nonlocal calls
#         print(f"Вызов #{calls + 1}")
#         calls += 1
#         result = func(*args, **kwargs)
#         print("Вызов завершён")
#         return result

#     return wrapper

# @logger
# def say_hello(name):
#     print(f"{name}")

# say_hello(str(input('>>> ')))
#- CLASS TASK 5:
# def logger(n):
#     def decr(func):
#         calls = 0

#         def wrapper(f):
#             nonlocal calls
#             print(f"Вызов: {calls}")
#             calls += 1
#             func(f)
#             if calls <= n:
#                 print('Превышен лимит!')
#             print("Вызов завершён")
#         return wrapper

#     return decr

# @logger(3)
# def say_hello(name):
#     print(name)

# say_hello("Hello")
# say_hello("Hello")
# say_hello("Hello")
# say_hello("Hello")
#- CLASS TASK 6: