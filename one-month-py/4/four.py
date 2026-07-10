# # #todo: tema 1 
# ? Input / Output (3 задачи)
# name = str(input("Your name: "))
# username = str(input("Your username: "))

# print("Ваш Логин: ", name.lower(),"_",username.lower(),"_2026" ,sep="")
# #todo: tema 2
# Film_name = input("Введите название фильма: ")
# Film_time = int(input("Введите длительность фильма: "))

# hours = Film_time // 60
# minutes = Film_time % 60

# print(f"Фильм {Film_name} длится {hours} часа {minutes} минут.")
# #todo: tema 3
# name = str(input("Your name: "))
# job  = str(input("Your job: "))
# company  = str(input("Company: "))

# print("======================")
# print(f"Имя: {name}")
# print(f"Профессия: {job}")
# print(f"Компания: {company}")
# print("========================")
# #todo: tema 4
# ? Condition (if / elif / else) — 5 задач
# age_zone = int(input())

# if age_zone <= 12:
#     print("Вам доступна детская зона.")
# elif age_zone > 12 and age_zone < 17:
#     print("Вам доступна подростковая зона.")
# else:
#     print("Вам доступна взрослая зона.")
# #todo: tema 5
# password = str(input("Your Password: "))

# if len(password) < 8:
#     print("У вас слабый пароль")
# elif len(password) == 8 and len(password)<=12:
#     print("У вас средный пароль")
# else:
#     print("Ваш пароль сильный.")
# #todo: tema 6
# total_sum = int(input("Введите сумму покупки: "))

# if total_sum > 1000:
#     skidka = 15
# elif total_sum > 500:
#     skidka = 10
# else:
#     skidka = 0

# final_price = total_sum * (1 - skidka / 100)

# final_price = int(final_price)

# print(f"Ваша скидка {skidka} %")
# print(f"К оплате: {final_price} сомони")
# #todo: tema 7
# User = int(input("Проверка статуса доставки: "))

# if User >=0 and 2>=User :
#     print("Заказ в Пути")
# elif 3<=User and User<=5:
#     print("Прибудет Скоро")
# else:
#     print("Обратитесь в поддержку")
# #todo: tema 8
# user_score = int(input("Введите очки: "))

# min_level = "Новичок"
# normal_level = "Опытный"
# max_level = "Профессионал"

# if user_score <1000:
#     print(f"Ваш уровень: {min_level}")
# elif user_score >= 1000 and user_score<=5000:
#     print(f"Ваш уровень: {normal_level}")
# else:
#     print(f"Ваш уровень: {max_level}")
# #todo: tema 9
# # ? Match / Case (5 задач)
# lang = str(input("----------------> "))

# match lang:
#     case "ru":
#         print("Добро Пожаловать!")
#     case "en":
#         print("Welcome!")
#     case "tj":
#         print("Хуш омадед!")
# #todo: tema 10
# smart_home = str(input("Введите команду: "))

# match smart_home:
#     case "light":
#         print("Включён свет💡")
#     case "fan":
#         print("Включён вентилятор")
#     case "door":
#         print("Дверь открыта")
#     case _:
#         print("Не извесная команда!")
# #todo: tema 11
# user_tarif = str(input("Выберите тариф: "))

# basic = "50 сомони."
# premium = "120 сомони."
# vip = "250 сомони."

# match user_tarif:
#     case "basic":
#         print(f"Стоимость тарифа {basic}")
#     case "premium":
#         print(f"Стоимость тарифа {premium}")
#     case "vip":
#         print(f"Стоимость тарифа {vip}")
#     case _:
#         print("Такого тарифа нет!")
# #todo: tema 12
# user_commands = str(input("Ввети функцию: "))

# match user_commands:
#     case "balance":
#         print("100 сомони.")
#     case "deposit":
#         enter = int(input('Введите сумму для пополнения: '))
#         print(f"Вы успешно пополнили баланс на {enter}сомони.")
#     case "withdraw":
#         width = int(input("Введите сумму для вывода: "))
#         print(f"Вы успешно пополнили баланс на {width}сомони.")
#     case _:
#         print("eror - commands")
# #todo: tema 13
# menu_restoran = str(input("Введите блюда: "))

# match menu_restoran:
#     case "pizza":
#         print("Ваш заказ: Пицца, цена 60 сомони.")
#     case "burger":
#         print("Ваш заказ: Бургер, цена 40 сомони.")
#     case "coffee":
#         print("Ваш заказ: Кофе, цена 10 сомони.")
#     case _:
#         print(f"В меню нет этого блюда: {menu_restoran}")
# #todo: tema 14
# # ? Loops — циклы (6 задач)
password = 7899
attempts = 3

while attempts > 0:
    user_password = int(input("Введите пароль: "))
    
    if user_password == password:
        print("Вход выполнен.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Неверный пароль. Осталось попыток: {attempts}")
        else:
            print("Аккаунт заблокирован.")
# #todo: tema 15
# total_sum = 0

# while True:
#     user_input = input("Введите цену продукта: ")
    
#     if user_input == "stop":
#         break

#     price = int(user_input)
#     total_sum = total_sum + price

# total_sum = int(total_sum)

# print("Общая сумма:", total_sum)
# #todo: tema 16
# taken_seats = [3, 7, 12, 25]

# print("Свободные места:")

# for seat in range(1, 51):

#     if seat not in taken_seats:
#         print(f"{seat}", end=" ")

# #todo: tema 17
# total_sum = 0
# receipt_items = ""

# while True:
#     user_input = str(input("Введите название товара: "))

#     if user_input == "finish":
#         break

#     price = int(input("Введите цену товара: "))

#     total_sum += price

#     receipt_items += f"{user_input} - {price} сомони\n"

# print("\nЧек:")
# print(receipt_items)
# print(f"Итого: {total_sum} сомони")

# #todo: tema 18
# password = 4343
# attempts = 3
# while attempts > 0:
#     user_password = int(input("Введите пароль карты: "))

#     if user_password == password:
#         print("Добро пожаловать в банк!")
#         break
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(f"Неверный пароль. Осталось попыток: {attempts}")
#         else:
#             print("Карта заблокирован.")
# #todo: tema 19
# score = 0

# print("Добро пожаловать на онлайн-тест! Ответьте на 5 вопросов.\n")

# answer1 = input("Вопрос 1: Сколько планет в Солнечной системе? ")
# if answer1 == "8":
#     score += 1

# answer2 = input("Вопрос 2: Какой город является столицей Таджикистана? ")
# if answer2 == "Душанбе":
#     score += 1

# answer3 = input("Вопрос 3: Сколько будет 5 умножить на 5? ")
# if answer3 == "25":
#     score += 1

# answer4 = input("Вопрос 4: Какой газ необходим человеку для дыхания? ")
# if answer4 == "Кислород":
#     score += 1

# answer5 = input("Вопрос 5: Как называется столица Франции? ")
# if answer5 == "Париж":
#     score += 1

# print("\nТест завершен!")
# print(f"Ваш результат {score} из 5")