# # #! EXAM TASK 1:
def avg(a,b,c,d):
    suum = a + b + c + d
    if a > 101:
        print(f'\n{on} not big 100: [{a}]')
    if b > 101:
        print(f'{it} not big 100: [{b}]')
    if c > 101:
        print(f'{ro} not big 100: [{c}]')
    if d > 101:
        print(f'{er} not big 100: [{d}]\n')
    else:
        ok = suum / 4
        print(f'\nYour average is: {ok}')
        if ok >= 80:
            print('You have successfully passed the exam. Happy coding\n')
        elif ok < 80:
            print('You have failed the exam. Study hard!\n')
on = 'Exam - 1: '
it = 'Exam - 2: '
ro = 'Exam - 3: '
er = 'Exam - 4: '
a = int(input(f'{on}'))
b = int(input(f'{it}'))
c = int(input(f'{ro}'))
d = int(input(f'{er}'))
avg(a,b,c,d)
# #! EXAM TASK 2:
# pos = 0
# neg = 0
# while True:
#     ok = int(input('>>> '))
#     if ok > 0:
#         pos += 1
#     elif ok < 0:
#         neg +=1
#     elif ok == 0:
#         break

# print(f'\nPositive: {pos}')
# print(f'Negative: {neg}')
# #! EXAM TASK 3:
# ok = [1, 2, 2, 4, 3, 3 ,3]
# cnt = 0
# for i in set(ok):
#     if i == i:
#         cnt += 1
# print(cnt)
# #! EXAM TASK 4:
# #? Нафахмидим задача чи мега!
# #! EXAM TASK 5:
# from random import *  
# data_db = []
# for i in range(101):
#     ok = (f'Bilet: {randrange(1,1000000000)}')
#     data_db.append(ok)
# print(data_db)
# #! EXAM TASK 6:
# ok = input('>>> ')
# lict = []
# touple = ()
# for i in ok:
#     touple = list(touple)
#     for o in touple:
#         if o == ',':
#             touple.remove(o)
#     touple.append(i)
#     touple = tuple(touple)
# for i in ok:
#     lict.append(i)
#     if i == ',':
#         lict.remove(i)
# print(touple)
# print(lict)
# #! EXAM TASK 7:
# def ok(n, off=7):
#     if off > n:
#         return
#     print(f'{off}', end=" ")
#     ok(n, off + 7)

# ok(int(input('Enter the num:\n>>> ')))
# #! EXAM TASK 8;
# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def plus(self):
#         print(f'Total: {self.a + self.b}')

#     def minus(self):
#         print(f'Total: {self.a - self.b}')

#     def umnozhit(self):
#         print(f'Total: {self.a * self.b}')

#     def delenie(self):
#         print(f'Total: {self.a / self.b}')

# ok = Calculator(int(input('First number:\n>>> ')),int(input('Second-number:\n>>> ')))
# ok.plus()
# ok.minus()
# ok.umnozhit()
# ok.delenie()
# #! EXAM TASK 9:
# class Person:
#     def __init__(self, name, country,date):
#         self.name = name
#         self.country = country
#         self.date = date

#     def birthday(self):
#         ok = 2026 - self.date
#         print(f'\n{self.name}: your age {ok} you are from {self.country}')

# ok = Person(str(input('Enter your name:\n>>> ')),str(input('Enter the country:\n>>> ')),int(input('Enter date birthday:\n>>> ')))
# ok.birthday()
# #! EXAM FINAL TASK 10:
# is_premium_user = True
# username = str(input('Enter your username:\n>>> '))
# def premium(ok):
#     def wrapper(username, is_premium):
#         if is_premium:
#             return ok(username, is_premium)
#         else:
#             return f"{username} is not a premium user."
#     return wrapper

# @premium
# def watch_course(username, is_premium):
#     if is_premium == True:
#         return f"{username} started watching the course."
#     else:
#         return f"{username} is not a premium user."