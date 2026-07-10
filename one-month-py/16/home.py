# #? Task 1
# def make_counter():
#     count = 1001
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# counter = make_counter()
# print(counter())
# print(counter())
#? Task 2
# def salary_system(base):
    
#     def cal_tax():
#         return base * 0.10
    
#     tax = cal_tax()
    
#     final = base - tax
#     print(f'Налог: {tax}\nИтого:')
#     return final

# print(salary_system(int(input('Введите ваше число: '))))
#? Task 3
# def create_name_formatter(prefix):
#     def format_name(name):
#         return f"{prefix} {name}"
#     return format_name

# mr = create_name_formatter(str(input()))
# print(mr(str(input())))
#? Task 4
# def create_adder(x):
#     def add_num(y):
#         return x + y
#     return add_num

# add = create_adder(int(input()))
# print(add(int(input())))
#? Task 5
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# counter = make_counter()
# print(f'Лайков: {counter()}')
# print(f'Лайков: {counter()}')
#? Task 6
# def make_counter():
#     count = 0
#     def counter(x):
#         nonlocal count
#         count += x
#         return count
#     return counter

# counter = make_counter()
# print(f'Баланс: {counter(int(input('Пополнить: ')))}с.')
# print(f'Баланс: {counter(int(input('Пополнить: ')))}с.')
# print(f'Баланс: {counter(int(input('Пополнить: ')))}с.')
#? Task 7
# def create_email_sender(sender_email):
#     def send_email(recipient_email, message):
#         print(f"--------------\nОтправитель: {sender_email}")
#         print(f"Получатель: {recipient_email}")
#         print(f"Сообщение: {message}")
#         print("Статус: Email успешно отправлен!\n--------------")
#     return send_email

# send_from_work = create_email_sender(str(input('Введите ваш email: ')))
# send_from_work(str(input('Укажите email кому отправить: ')),str(input('Ваше сообщение: ')))
#? Task 8
# def make_counter():
#     count = 0
#     def counter(x):
#         nonlocal count
#         count += x
#         return count
#     return counter

# counter = make_counter()
# print(f'Очков: {counter(int(input('Заработание очки: ')))}')
# print(f'Очков: {counter(int(input('Заработание очки: ')))}')
# print(f'Очков: {counter(int(input('Заработание очки: ')))}')
#? Task 9
# def create_rate_limiter(zapros):
#    requests_count = 0
    
#     def limit_requests():
#         nonlocal requests_count
#         if requests_count < zapros:
#             requests_count += 1
#             return f"Запрос разрешен. Всего запросов: {requests_count}"
#         else:
#             return "Отказ: Превышен лимит запросов!"
            
#     return limit_requests

# limiter = create_rate_limiter(int(input("Максимальное кол-во запросов: ")))
# print(limiter())
# print(limiter())
# print(limiter())
#? Task 10
# def create_inventory(kol):
#     def sell_item(sold):
#         nonlocal kol
#         kol -= sold
#         return kol
#     return sell_item

# inventory = create_inventory(int(input('Товара на складе: ')))
# print("Остаток после продажи:", inventory(int(input('Проданные товары: '))))
# print("Остаток после продажи:", inventory(int(input('Проданные товары: '))))
#? Task 11
# def create_grade_book(student_name):
#     grades = []
    
#     def add_grade(grade):
#         grades.append(grade)
#         average = sum(grades) / len(grades)
#         return average
        
#     return add_grade

# student = create_grade_book(input("Введите имя студента: "))
# print("Средний балл:", student(int(input("Введите оценку: "))))
# print("Средний балл:", student(int(input("Введите оценку: "))))
# print("Средний балл:", student(int(input("Введите оценку: "))))