Python Practice Tasks
Functions + List + Tuple + Dictionary + Set
Each task must be solved using a function.
________________________________________
LIST TASKS
Task 1 (Easy ⭐)
User Registration Queue
🇬🇧 English
Create a function:
add_user(users, username)
If the username does not exist in the list, add it.
🇷🇺 Русский
Создайте функцию:
add_user(users, username)
Если пользователя нет в списке, добавьте его.
Input
users = ["ali", "sara"]
username = "kamol"
Output
["ali", "sara", "kamol"]
________________________________________
Task 2 (Easy ⭐)
Shopping Cart Total
🇬🇧 English
Create a function that calculates the total price of all products in the cart.
🇷🇺 Русский
Создайте функцию, которая вычисляет общую стоимость товаров в корзине.
Function
calculate_total(cart)
Input
[120, 50, 80]
Output
250
________________________________________
Task 3 (Medium ⭐⭐)
YouTube Analytics
🇬🇧 English
Find the most viewed video.
🇷🇺 Русский
Найдите видео с максимальным количеством просмотров.
Function
top_video(views)
Input
[1200, 5500, 3400, 9000]
Output
9000
________________________________________
Task 4 (Medium ⭐⭐)
Employee Salary Filter
🇬🇧 English
Return only salaries greater than 5000.
🇷🇺 Русский
Верните только зарплаты больше 5000.
Function
high_salary(salaries)
Input
[3000, 7000, 4500, 9000]
Output
[7000, 9000]
________________________________________
Task 5 (Hard ⭐⭐⭐)
E-Commerce Order Analytics
🇬🇧 English
Create a report with:
•	total orders
•	total revenue
•	average order value
•	largest order
🇷🇺 Русский
Создайте отчет:
•	количество заказов
•	общая сумма
•	средний чек
•	самый большой заказ
Function
order_stats(orders)
Input
[120, 340, 550, 90, 800]
Output
{
    "count": 5,
    "total": 1900,
    "average": 380,
    "max": 800
}
________________________________________
TUPLE TASKS
Task 6 (Easy ⭐)
GPS Coordinates
🇬🇧 English
Extract latitude and longitude from a tuple.
🇷🇺 Русский
Извлеките широту и долготу из кортежа.
Function
show_location(location)
Input
(38.56, 68.78)
Output
Latitude: 38.56
Longitude: 68.78
________________________________________
Task 7 (Easy ⭐)
Product Information
🇬🇧 English
Display product name, price, and quantity.
🇷🇺 Русский
Покажите название товара, цену и количество.
Function
product_info(product)
Input
("Laptop", 8000, 10)
Output
Laptop
8000
10
________________________________________
Task 8 (Medium ⭐⭐)
Student Report
🇬🇧 English
Calculate the average score of a student.
🇷🇺 Русский
Посчитайте средний балл студента.
Function
student_report(student)
Input
("Ali", [90, 80, 70])
Output
Average: 80
________________________________________
Task 9 (Medium ⭐⭐)
Weather Analytics
🇬🇧 English
Return maximum, minimum, and average temperature.
🇷🇺 Русский
Верните максимальную, минимальную и среднюю температуру.
Function
weather_summary(data)
Input
(23, 25, 21, 30, 19)
Output
{
    "max": 30,
    "min": 19,
    "average": 23.6
}
________________________________________
Task 10 (Hard ⭐⭐⭐)
Flight Tracking System
🇬🇧 English
Convert flight tuple data into a dictionary report.
🇷🇺 Русский
Преобразуйте данные рейса в словарь.
Function
flight_report(flight)
Input
("TJ101", "Dushanbe", "Dubai", 180)
Output
{
    "id": "TJ101",
    "departure": "Dushanbe",
    "arrival": "Dubai",
    "duration": 180
}
________________________________________
DICTIONARY TASKS
Task 11 (Easy ⭐)
User Profile
Function
show_profile(user)
🇬🇧 English
Display user information.
🇷🇺 Русский
Покажите информацию о пользователе.
Input
{
    "name": "Ali",
    "age": 25
}
Output
Ali is 25 years old
________________________________________
Task 12 (Easy ⭐)
Product Price Lookup
Function
get_price(products, name)
Input
{
    "Laptop": 8000,
    "Mouse": 150
}
"Laptop"
Output
8000
________________________________________
Task 13 (Medium ⭐⭐)
Website Analytics
Function
most_popular_page(stats)
Input
{
    "home": 5000,
    "blog": 3000,
    "pricing": 7000
}
Output
pricing
________________________________________
Task 14 (Medium ⭐⭐)
School Gradebook
Function
average_grade(grades)
Input
{
    "Math": 90,
    "English": 80,
    "Python": 100
}
Output
90
________________________________________
Task 15 (Hard ⭐⭐⭐)
Sales Dashboard
Function
sales_report(data)
Input
{
    "January": 5000,
    "February": 8000,
    "March": 6500
}
Output
{
    "best_month": "February",
    "worst_month": "January",
    "total": 19500,
    "average": 6500
}
________________________________________
SET TASKS
Task 16 (Easy ⭐)
Unique Visitors
Function
unique_visitors(visitors)
Input
["Ali", "Ali", "Sara", "Kamol"]
Output
3
________________________________________
Task 17 (Easy ⭐)
Unique Tags
🇬🇧 English
Remove duplicate tags.
🇷🇺 Русский
Удалите повторяющиеся теги.
Function
unique_tags(tags)
Input
["python", "ai", "python", "coding"]
Output
{"python", "ai", "coding"}
________________________________________
Task 18 (Medium ⭐⭐)
Social Network
Function
common_friends(user1, user2)
Input
{"Ali", "Sara", "Kamol"}
{"Sara", "Madina", "Ali"}
Output
{"Ali", "Sara"}
________________________________________
Task 19 (Medium ⭐⭐)
Online Course Platform
Function
missing_students(all_students, attended)
Input
{"Ali", "Sara", "Kamol", "Madina"}
{"Ali", "Kamol"}
Output
{"Sara", "Madina"}
________________________________________
Task 20 (Hard ⭐⭐⭐)
Cyber Security Login Monitor
Function
detect_suspicious_ips(logins)
Input
[
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.1",
    "192.168.1.3",
    "192.168.1.2"
]
Output
{
    "192.168.1.1",
    "192.168.1.2"
}
