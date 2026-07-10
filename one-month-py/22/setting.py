# #!PRACTICE TASK
# class dog:
#     breed = 'Buldog'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print(f'{self.name}: bark bark')

#     def show_info(self):
#         print(f'-------------\nDog name: {self.name}\nDog age: {self.age}\n-------------')

#     @classmethod
#     def my_class_metods(cls):
#         print(f'Dog name: {cls.breed}\n------------')


# bars = dog(str(input('Dog-name and Dog-age:\n>>> ')),int(input('>>> ')))
# bars.show_info()
# bars.make_sound()
# rex = dog(str(input('Dog-name and Dog-age:\n>>> ')),int(input('>>> ')))
# rex.show_info()
# rex.make_sound()
#^ CLASS TASK 1:
# class Students:
#     pass
    
# ali = Students()
# vali = Students()
# Sangali = Students()
#^ CLASS TASK 2:
# class Cat:
#     pass

#     def __init__(self,name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

#     def show(self):
#         print(f'-------------\nCat name: {self.name}\nCat age: {self.age}\nCat color: {self.color}\n-------------')

# bars = Cat(str(input('Name:\n>>> ')),int(input('Age\n>>> ')),str(input('Color:\n>>> ')))
# bars.show()
#^ CLASS TASK 3:
# class Car:
#     pass
#     def __init__(self,brand, model,year,color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color

#     def show_car(self):
#         print(f'------------\nCar brand: {self.brand}\nCar model: {self.model}\nCar year: {self.year}\nCar color: {self.color}\n------------')

# toyota =  Car(str(input('Brand:\n>>> ')),str(input('Model:\n>>> ')),int(input('Years:\n>>> ')),str(input('Color:\n>>> ')))
# mers = Car(str(input('\nBrand:\n>>> ')),str(input('Model:\n>>> ')),int(input('Years:\n>>> ')),str(input('Color:\n>>> ')))
# toyota.show_car()
# mers.show_car()
#^ CLASS TASK 4:
# class BankAccount:
#     pass

#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance

#     def show_balance(self):
#         print(f'-----------\nOwner: {self.owner} and your balance: {self.balance}c.')

# Director = BankAccount(str(input('Owner\n>>> ')),int(input('Balance\n>>> ')))
# Outher = BankAccount(str(input('-----\nOwner\n>>> ')),int(input('Balance\n>>> ')))
# Director.show_balance()
# Outher.show_balance()
#^ CLASS TASK 5:
# class Phone:
#     pass

#     def __init__(self, brand,model,battery):
#         self.brand = brand
#         self.model = model
#         self.battery = battery

#     def turn_on(self):
#         print('----------\nYour Phone is ON')
#     def turn_off(self):
#         print('----------\nYour Phone is OFF')
#     def show_info(self):
#         print(f'---------\nPhone brand: {self.brand}\nPhobe model: {self.model}\nPhone battery: {self.battery}')

# iphone = Phone(str(input('Phone brand:\n>>> ')),str(input('Phone model:\n>>>')),str(input('Phone battery:\n>>> ')))
# samsung = Phone(str(input('\nPhone brand:\n>>> ')),str(input('Phone model:\n>>>')),str(input('Phone battery:\n>>> ')))
# iphone.turn_on()
# iphone.show_info()
# samsung.turn_off()
# samsung.show_info()
#^ CLASS TASK 6:
# class Rectangle:
#     pass
#     def __init__(self,width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         Area = self.width * self.height
#         print(f'Area: {Area}')

#     def perimetr(self):
#         Perimetr = 2 * (self.width + self.height)
#         print(f'Perimetr: {Perimetr}')


# zone = Rectangle(int(input('Width:\n>>> ')),int(input('Height:\n>>> ')))
# zone.area()
# zone.perimetr()
#^ CLASS TASK 7:
# class Employee:
#     pass

#     def __init__(self,name, position,salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def show_info(self):
#         print(f'----------\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}\n-----------')

#     def in_salary(self, percent):
#         percent = int(input('Percent\n>>> '))
#         ok = self.salary * percent
#         print(f'Percent: {ok}')

# outher = Employee(str(input('Name:\n>>> ')),str(input('Position:\n>>> ')),int(input('Salary:\n>>> ')))
# outher.show_info()
# outher.in_salary(None)
#^ CLASS TASK 8:
# class Products:
#     pass

#     def __init__(self,name, price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total(self):
#         total = self.price * self.quantity
#         print(f'Product {self.name}: {self.price} x {self.quantity}')
#         print(f'Total price: {total}')

#     def update_quantity(self):
#         self.quantity = int(input('New quantity:\n>>> '))
#         ok.total()

# ok = Products(str(input('Product:\n>>> ')),
#             int(input('Price:\n>>> ')),
#             int(input('Quantity:\n>>> ')))
# ok.total()
# ok.update_quantity()
#^ CLASS TASK 9:
# class Book:
#     pass

#     def __init__(self, title, author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def read(self):
#         print('Вы читаете книгу "Python для начинающих"\n-------------')

#     def book_info(self):
#         print('----------')
#         print(f'Title: {self.title}')
#         print(f'Author: {self.author}')
#         print(f'Pages: {self.pages}')
#         print('----------')
# title = str(input('Title:\n>>> '))
# author = str(input('Author:\n>>> '))
# pages = str(input('Pages:\n>>> '))
# ok = Book(title,author,pages)
# ok.book_info()
# ok.read()
#^ CLASS TASK 10:
# class Students:
#     pass
#     def __init__(self,name, scores=[]):
#         self.name = name
#         self.scores = scores

#     def avg_score(self):
#         cnt = 0
#         for i in self.scores:
#             num = int(i)
#             cnt +=num
#         avg = cnt / len(self.scores)
#         print('----------')
#         print(f'Name: {self.name}')
#         print(f'Average: {avg}')
#         print('----------')
    
#     def add_scores(self):
#         n = input('New scores:\n>>> ').split()
#         for i in n:
#             scores.append(i)
#         print(f'Name: {self.name}')
#         print('Scores:')
#         for i in scores:
#             print(f'{i}',end=' ')

# name = str(input('Name:\n>>> '))
# scores = input('Student scores:\n>>> ').split()
# ok = Students(name,scores)
# ok.avg_score()
# ok.add_scores()
#^ CLASS TASK 11:
# class Employees:
#     pass
#     cnt = 0

#     def __init__(self,name):
#         self.name = name
#         cnt +=1
#         print(cnt)

# ok = Employees('Abu')
# ot = Employees('Ali')
#^ CLASS TASK 12:
# class School:
#     sc = 'School 23'
#     def __init__(self,name):
#         self.name = name

# st1 = School('Mukimov')
# st2 = School('Abbos')
# print(st1.name,st1.sc)
# print(st2.name,st2.sc)
#^ CLASS TASK 13:
# class Corrent:
#     udt_rate = 9.22
#     def __init__(self):
#         pass

#     @classmethod
#     def change_rate(cls, new_rate):
#         cls.udt_rate = new_rate
#         print(f'KURS: {cls.udt_rate}')

# Corrent.change_rate(int(input('New rate: ')))
#^ CLASS TASK 14:
# class University:
#     country = None

#     def __init__(self, name, students):
#         self.name = name
#         self.students = students


#     def info(self):
#         print(f'{self.name} university and all students {self.students}')

# name = str(input('University name: '))
# students = int(input('University students: '))
# ok = University()
# ok.info(name,students) 