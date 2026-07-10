"""
1. Shopping Cart / Сабади харид
🇷🇺 Добавьте новый товар в корзину. Если товар уже есть — выведите сообщение.
🇹🇯 Маҳсулоти навро ба сабад илова кунед. Агар маҳсулот аллакай бошад — паём нишон диҳед.
Input:
cart = ["milk", "bread", "apple"]
banana
Output:
Updated cart:
["milk", "bread", "apple", "banana"]
"""
#todo: tema 1
# cart = ["milk", "bread", "apple"]
# new_item = str(input("Enter your product: "))

# if new_item in cart:
#     print(f"Маҳсулоти '{new_item}' аллакай дар сабад ҳаст!")
# else:
#     cart.append(new_item)
#     print("Updated cart: ")
#     print(cart)
"""
2. Student List / Рӯйхати донишҷӯён
🇷🇺 Удалите студента, если он существует в списке.
🇹🇯 Агар донишҷӯ дар рӯйхат бошад — ӯро хориҷ кунед.
Input:
students = ["Ali", "Zarina", "Kamol"]
Zarina
Output:
Updated students:
["Ali", "Kamol"]
"""
# #todo: tema 2
# students = ["Ali", "Zarina","Kamol"]
# remove_students = str(input("Введите имя студента: "))

# if remove_students in students:
#     students.remove(remove_students)
#     print(students)
# else:
#     print(f"Студент '{remove_students}' не найден!")
"""
3. Top Sales / Фурӯшҳои беҳтарин
🇷🇺 Покажите 3 самых больших продажи.
🇹🇯 3 фурӯши калонтаринро нишон диҳед.
Input:
sales = [120, 550, 340, 900, 760]
Output:
Top 3:
[900, 760, 550]
"""
# #todo: tema 3
# sales = input().split()

# sales.sort(reverse=True)

# top_3_sales = sales[:3]

# print("Top 3:")
# print(top_3_sales)
"""
4. Movie Ratings / Рейтинги филмҳо
🇷🇺 Найдите средний рейтинг и количество оценок 5.
🇹🇯 Рейтинги миёна ва шумораи баҳои 5-ро ёбед.
Input:
ratings = [5, 4, 5, 3, 5]
Output:
Average: 4.4
Five stars: 3
"""
# #todo: tema 4
# ratings = input("Enter your film number: ").split()

# average_rating = sum(ratings) / len(ratings)

# five_stars_count = ratings.count(5)

# print(f"Average: {average_rating}")
# print(f"Five stars: {five_stars_count}")
"""
5. Bank Queue / Навбат дар бонк
🇷🇺 Обслужите первого клиента.
🇹🇯 Ба мизоҷи аввал хизмат расонед.
Input:
["Ahmad", "Said", "Kamol"]
Output:
Served: Ahmad
Remaining:
["Said", "Kamol"]
"""
# #todo: tema 5
# queue = ["Ahmad", "Said", "Kamol"]

# served_client = queue.pop(0)

# print(f"Served: {served_client}")
# print("Remaining:")
# print(queue)
"""
6. Remove Duplicate Emails / Нест кардани email-ҳои такрорӣ
🇷🇺 Удалите повторяющиеся email.
🇹🇯 Email-ҳои такрориро нест кунед.
Input:
["a@gmail.com", "b@gmail.com", "a@gmail.com"]
Output:
["a@gmail.com", "b@gmail.com"]
"""
# #todo: tema 6
# # Исходный список
# emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]

# unique_emails = []

# for email in emails:
#     if email not in unique_emails:
#         unique_emails.append(email)

# print(unique_emails)
"""
7. Product Search / Ҷустуҷӯи маҳсулот
🇷🇺 Проверьте наличие товара и покажите индекс.
🇹🇯 Мавҷудияти маҳсулот ва индекси онро нишон диҳед.
Input:
products = ["laptop", "mouse", "keyboard"]
mouse
Output:
Product found at index 1
"""
# #todo: tema 7
# products = ["laptop", "mouse", "keyboard"]
# search_item = "mouse"

# if search_item in products:
#     index = products.index(search_item)
#     print(f"Product found at index {index}")
# else:
#     print("Product not found")
"""
8. Passed Students / Донишҷӯёни гузашта
🇷🇺 Оставьте оценки выше 50.
🇹🇯 Танҳо баҳои аз 50 болоиро нигоҳ доред.
Input:
[45, 70, 90, 30, 60]
Output:
[70, 90, 60]
"""
# #todo: tema 8
# scores = [45, 70, 90, 30, 60]
# passed_scores = []

# for score in scores:
#     if score > 50:
#         passed_scores.append(score)

# print(passed_scores)
"""
9. Voting System / Системаи овоздиҳӣ
🇷🇺 Найдите победителя голосования.
🇹🇯 Ғолиби овоздиҳиро муайян кунед.
Input:
["Ali", "Ali", "Said", "Kamol", "Ali"]
Output:
Winner: Ali
Votes: 3
"""
# #todo: tema 9
# votes = ["Ali", "Ali", "Said", "Kamol", "Ali"]

# vote_counts = {}

# for name in votes:
#     if name in vote_counts:
#         vote_counts[name] += 1
#     else:
#         vote_counts[name] = 1

# winner = ""
# max_votes = 0

# for name, count in vote_counts.items():
#     if count > max_votes:
#         max_votes = count
#         winner = name

# print(f"Winner: {winner}")
# print(f"Votes: {max_votes}")
"""
10. Discount Prices / Нархҳо бо тахфиф
🇷🇺 Примените скидку 10%.
🇹🇯 Ба ҳамаи нархҳо 10% тахфиф диҳед.
Input:
[100, 200, 300]
Output:
[90, 180, 270]
"""
# # #todo: tema 10
# prices = [100, 200, 300]
# discounted_prices = []

# for price in prices:
#     new_price = int(price * 0.9)
#     discounted_prices.append(new_price)

# print(discounted_prices)
"""
11. Positive and Negative / Рақамҳои мусбат ва манфӣ
🇷🇺 Разделите числа на положительные и отрицательные.
🇹🇯 Рақамҳоро ба мусбат ва манфӣ ҷудо кунед.
Input:
[-5, 10, -2, 8]
Output:
Positive: [10, 8]
Negative: [-5, -2]
"""
# #todo:tema 11
# numbers = [-5, 10, -2, 8]

# positive = []
# negative = []

# for num in numbers:
#     if num > 0:
#         positive.append(num)
#     elif num < 0:
#         negative.append(num)

# print(f"Positive: {positive}")
# print(f"Negative: {negative}")
"""
12. Athlete Results / Натиҷаи варзишгарон
🇷🇺 Найдите лучшее время.
🇹🇯 Беҳтарин вақтро пайдо кунед.
Input:
[12.5, 11.8, 13.1, 10.9]
Output:
Best result: 10.9
"""
# #todo: tema 12
# results = [12.5, 11.8, 13.1, 10.9]

# best_result = results[0]

# for time in results:
#     if time < best_result:
#         best_result = time

# print(f"Best result: {best_result}")
"""
13. Music Playlist / Рӯйхати мусиқӣ
🇷🇺 Добавьте новую песню.
🇹🇯 Суруди навро илова кунед.
Input:
["Song A", "Song B"]
Song C
Output:
["Song A", "Song B", "Song C"]
"""
# #todo: tema 13
# playlist = ["Song A", "Song B"]
# new_song = input()

# playlist.append(new_song)

# print(playlist)
"""
14. Student Scores Matrix / Матритсаи баҳоҳо
🇷🇺 Найдите средний балл первого студента.
🇹🇯 Баҳои миёнаи донишҷӯи аввалро ҳисоб кунед.
Input:
[[80,90,100],[70,60,50]]
Output:
Average: 90
"""
# #todo: tema 14
# matrix = [[80, 90, 100], [70, 60, 50]]

# first_student_scores = matrix[0]

# average = sum(first_student_scores) / len(first_student_scores)

# print(f"Average: {int(average)}")
"""
15. Seat Booking / Бронкунии ҷой
🇷🇺 Забронируйте место.
🇹🇯 Ҷойро брон кунед.
Input:
["A1","A2","A3"]
A2
Output:
Booked successfully
Available seats:
["A1","A3"]
"""
# #todo: tema 15
# available_seats = ["A1", "A2", "A3"]
# seat_to_book = input()

# if seat_to_book in available_seats:
#     available_seats.remove(seat_to_book)
    
#     print("Booked successfully")
#     print("Available seats:")
#     print(available_seats)
# else:
#     print("Seat is already booked or does not exist")
"""
16. Student Tuple / Tuple-и донишҷӯ
🇷🇺 Распакуйте данные студента.
🇹🇯 Маълумоти донишҷӯро ҷудо кунед.
Input:
("Ali", 20, "Python")
Output:
Name: Ali
Age: 20
Course: Python
"""
# #todo:tema 16
# student_data = input().split()

# name = student_data[0]
# age = student_data[1]
# course = student_data[2]


# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Course: {course}")
"""
17. GPS Coordinates / Координатаҳои GPS
🇷🇺 Покажите широту и долготу.
🇹🇯 Арзи ҷуғрофӣ ва тӯли ҷуғрофиро нишон диҳед.
Input:
(38.5, 68.7)
Output:
Latitude: 38.5
Longitude: 68.7
"""
# #todo: tema 17
# gps = input("Enter your location -----> ").split()

# Latitude = gps[0]
# Longitude = gps[1]


# print(f"Latitude: {Latitude}")
# print(f"Longitude: {Longitude}")
"""
18. Product Tuple / Tuple-и маҳсулот
🇷🇺 Выведите информацию о товаре.
🇹🇯 Маълумоти маҳсулотро нишон диҳед.
Input:
("Laptop", 8000, 10)
Output:
Product: Laptop
Price: 8000
Quantity: 10
"""
# #todo: tema 18
# all_products = input("Enter product_name: ").split()

# products = all_products[0]
# price = all_products[1]
# Quantity = all_products[2]


# print(f"Product: {products}")
# print(f"Price: {price}")
# print(f"Quantity: {Quantity}")
"""
19. Temperature Analysis / Таҳлили ҳарорат
🇷🇺 Найдите максимальную температуру.
🇹🇯 Ҳарорати баландтаринро ёбед.
Input:
(23,25,21,30,19)
Output:
Maximum temperature: 30
"""
# #todo: tema 19
# tem = list(map(int, input("Enter temperature:").split()))
# print(f"Maximum temperature: {max(tem)}")
"""
20. City Database / Пойгоҳи шаҳрҳо
🇷🇺 Проверьте наличие города.
🇹🇯 Мавҷудияти шаҳрро санҷед.
Input:
("Dushanbe", "Khujand", "Bokhtar")
Khujand
Output:
City found at index 1
"""
#todo: tema 20
cityes = ["khujand","dushanbe","bohtar"]
user = str(input("Enter the city: "))

for i in cityes:
    if i == user:
        print(f'City found at index {user.index()}')
    else:
        print("Is city not found!")