# #?task 1
# def add_users(users, name):
#     for i in users:
#         if name == i:
#             print(
#                 '--------------\nUser is log!'
#             )
#             break
#         else:
#             users.append(name)
#             print('------------\nNew name add!')
#             break
#     print(users)
# log_name = input("Enter the log name: ").split()
# name = str(input("Enter the name: "))
# print(add_users(log_name, name))
#? task 2
# def calculate_total(cart):
#     return sum(cart)

# user_input = input("Введите цены: ").split()
# cart = []

# for price in user_input:
#     number = int(price)
#     cart.append(number)

# total = calculate_total(cart)
# print(f"Общая стоимость товаров: {total}")
#? task 3
# def public(view):
#     return max(view)

# user_input = input("Введите просмотри: ").split()
# views = []

# for price in user_input:
#     number = int(price)
#     views.append(number)

# total = public(views)
# print(f"Самое популярное видео: {total}")
#? task 4
# def high_salary(salaries):
#     return salaries

# n = input('Enter salaries: ').split()
# salar = []

# for i in n:
#     number = int(i)
#     if number >=5000:
#         salar.append(i)

# total = high_salary(salar)
# print(f"All big salaries: {total}")
#? task 5 - none
#? task 6
# def show_location(location):
#     latitude, longitude = location
    
#     print(f"Latitude: {latitude}")
#     print(f"Longitude: {longitude}")

# show_location((38.56, 68.78))
#? task 7
def product_info(product):
    return product

n = input('Enter the product: ').split()
kit = []

for i in n:
    num = int(i)
    kit.append(num)

total = product_info(kit)
print(f"product: {total}")
