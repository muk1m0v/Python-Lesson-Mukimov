# #todo: task 1
# def greet_user(name):
#     def hello():
#         print(f'Hello, {name}!')
#     hello()

# name = str(input('Enter the name: '))
# greet_user(name)
#todo: task 2
# def create_email(first_name, last_name):
#     def off():
#         print(f'{first_name}.{last_name}@company.com')
#     off()

# name = str(input('Enter the name: '))
# surname = str(input('Enter the surname: '))
# create_email(name, surname)
#todo: task 3
# def cart_total(*prices):
#     return sum(prices)

# prices = [int(x) for x in input('Введите сумму: ').split()]
# total_sum = cart_total(*prices)

# print(f'Итого: {total_sum}')
#todo: task 4
# def average_score(*scores):
#     if not scores:
#         return 0
#     return sum(scores) / len(scores)

# print(f'Средный: {average_score(10, 20, 30 ,40)}')
#todo: task 5
# def employee_card(**employee):
#     for key, value in employee.items():
#         print(f"{key}: {value}")

# info = {
#     "Исм": "Умар",
#     "Вазифа": "Дизайнер",
#     "Шӯъба": "Маркетинг"
# }

# employee_card(**info)
#todo: task 6
# def employee_card(**employee):
#     for key, value in employee.items():
#         print(f"{key}: {value}")

# info = {
#     'Product': 'Laptop',
#     'Price': 8000,
#     'Quantity': 10
# }

# employee_card(**info)
#todo: task 7
# def student_report(name, *ok):
#     if not ok:
#         sredniy = 0
#         max_grade = 0
#     else:
#         sredniy = sum(ok) / len(ok)
#         max_grade = max(ok)
    
#     print(f"Student: {name}")
#     print(f"Average: {int(sredniy) if sredniy % 1 == 0 else sredniy}")
#     print(f"Highest: {max_grade}")

# student_report("Ali", 80, 90, 100)
#todo: task 8
# def salary_system(base):
    
#     def cal_tax():
#         return base * 0.10
    
#     def cal_bon():
#         return base * 0.15
#     tax = cal_tax()
#     bonus = cal_bon()
    
#     final = base - tax + bonus
#     print(f'Налог: {tax}\nБонус: {bonus}\nИтого:')
#     return final

# print(salary_system(int(input('Введите ваше число: '))))