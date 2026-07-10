# #= TASK COMPELTED AT 1 TO 11
#^ PRACTICE TASK 1: input / output
# name = str(input('Enter the name:\n>>> '))
# print(f'Hello, {name}! Welcome!')
#^ PRACTICE TASK 2:
# n = input('Введите число через пробел:\n>>> ').split()
# cnt = 0
# for i in n:
#     num = int(i)
#     cnt += num
# print(f'Total: {cnt}c.')
#^ PRACTICE TASK 3:
# def total(a,b):
#     return int(a)/int(b)
# a,b = tuple(input('Enter the num:\n>>> ').split(','))
# result = total(a,b)
# print(round(result,2))
#^ PRACTICE TASK 4:
# cnt = 0
# while True:
#     line = input('>>> ').split()
#     cnt+=len(line)
#     if line == []:
#         print(f'Total: {cnt}')
#         break
#^ PRACTICE TASK 5:
# mukimov = input('Enter the time - level - message:\n>>> ')
# print(f'[{mukimov[1]}] at {mukimov[0]} --> {mukimov[2]}')
#- PRACTICE TASK 6: if / match
# n = int(input('Enter the number\n>>> '))

# if n > 0:
#     print('Positive')
# elif 0 > n:
#     print('Negative')
# else:
#     print('Zero')
#- PRACTICE TASK 7:
# weight = int(input('Enter the weight:\n>>> '))
# destination = input('Enter the local:\n>>> ')
# if destination == 'local' and weight < 5:
#     print(f'Shopping cost: ${5}')
# elif destination == 'local' and weight >= 5:
#     print(f'Shopping cost: ${10}')
# elif destination == 'international' and weight < 5:
#     print(f'Shopping cost: ${20}')
# elif destination == 'international' and weight >=5:
#     print(f'Shopping cost: ${35}')
#- PRACTICE TASK 8:
# from cor import *
# off()
#- PRACTICE TASK 9:
# n = str(input('Enter the color:\n>>> '))

# match n:
#     case 'red':
#         print('Stop')
#     case 'yellow':
#         print('Slow down, prepare to stop')
#     case 'green':
#         print('Go')
#     case _:
#         print('Invalid input color')\
#- PRACTICE TASK 10:
# n = input('Enter the first - num | second - num | symbol:\n>>> ').split(',')


# match n[2]:
#         case '*':
#             print(f'Total : {int(n[0]) * int(n[1])}')
#         case '-':
#             print(f'Total : {int(n[0]) - int(n[1])}')
#         case '/':
#             print(f'Total : {int(n[0]) / int(n[1])}')
#         case '+':
#             print(f'Total : {int(n[0]) + int(n[1])}')
#         case '%':
#             print(f'Total : {int(n[0]) % int(n[1])}')
#? PRACTICE TASK 11:
# server = input('Enter the index - server:\n>>> ')

# match server[0]:
#     case '1':
#         print('Status ---> Informational')
#     case '2':
#         print('Status ---> Success')
#     case '3':
#         print('Status ---> Redirection')
#     case '4':
#         print('Status ---> Client Error')
#     case '5':
#         print('Status ---> Server Error')
#     case _:
#         print('Is a invalid input')
#? PRACTICE TASK 12: while / for
# n = int(input('Enter the number:\n>>> '))
# i = n
# while i >= 1:
#     print(i)
#     i-=1
# print('Liftoff!')
#? PRACTICE TASK 13:
