# def my_function(name, age, surname="Testov", fathername="Testovich"):
#     print(f"Hello {name} {surname} {fathername} you are {age} years old")

# def test_function(*args, ** kwargs):
#     print (kwargs)
#     print (args)
#     for i in args:
#         print(i, end=" ")
#     print()

# test_function()
# test_function(123, "hello", "good bye", a=12, b=13)

# # my_function(age=18, name="Mustafo", fathername="Ahmadovich")
# # my_function(name="Nadim", surname="Bahor", age=20)
# test1 = "test1"
# def outer():
# print("this is outer function")
# test = "test" # local
# def inner(): # local
# d = 10 # local
# globaltest1
# test = "Hello"
# print("This is inner function")
# print(test)
# inner()
# print(test)

# outer()
#todo: task class
#? task 1
# def greet_user(name):
#     def hello():
#         print(f'Привет, {name}!')
#     hello()

# name = input('Введите имя: ')
# greet_user(name)
#? task 2
# def final_price(price):
#     def off():
#         on = price * 0.9
#         print(on)
#     off()

# price = int(input('Ввелите сумму: '))
# final_price(price)
#? task 3
# def check_password(password):
#     def off():
#         if len(password) >= 8:
#             print(f'Ваш пароль: {password} \n---Надежный---')
#         else:
#             print(f'Ваш пароль: {password} \n---Не надёжный----')
#     off()

# password = str(input('Введите ваш пароль: '))
# check_password(password)
#? task 4
# def student_report(ball):
#     def sredniy():
#         sum = 0
#         for i in ball:
#             sum+=int(i)
#         print(f'Средний: {sum/len(ball)}')
#     sredniy()
#     def maximum():
#         ok = max(ball)
#         print(f'Высший: {ok}')
#     maximum()

# ball = input().split()
# student_report(ball)