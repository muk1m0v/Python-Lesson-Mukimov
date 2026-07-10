# def employees (employee_name) :
#     base_salary = 1000
#     def increese_salary(n):
#         nonlocal base_salary
#         base_salary += base_salary*n/100
#         return f"{employee_name} {base_salary}"
#     return increese_salary

# m = employees ("Murodali")
# print(m(30))
# print(m(30))
# print(m(10))
#? task 1
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# counter = make_counter()
# print(counter())
# print(counter())
#? task 2
# def make_greeter():
#     def off(name):
#         return f'Привет, {name}'
#     return off

# a = make_greeter()
# print(a(input('Enter the name: ')))
#? task 3
# def make_multiplier(x):
#     def multiply(y):
#         return x * y
#     return multiply


# times_three = make_multiplier(int(input('Fist number: ')))
# print(times_three(int(input('Second number: '))))

# times_ten = make_multiplier(int(input('First number: ')))
# print(times_ten(int(input('Second number: '))))
#? task 4
# def make_password_checker():
#     def cor_pas(ok):
#         password = 1234
#         if password == ok:
#             print(True)
#         else:
#             print(False)
#     return cor_pas

# a = make_password_checker()
# a(int(input('Enter the password: ')))
#? task 5