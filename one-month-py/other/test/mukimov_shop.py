#_# todo: Первый продукт и его цена
product_one = str(input("1.Продукт: ")) # ? Продукт пример молоко
product_one_price = int(input("1.Цена: ")) # ? Цена продукта пример 43с.
# todo: Второй продукт и его цена
product_two = str(input("2.Продукт: ")) 
product_two_price = int(input("2.Цена: "))
# todo: Третый продукт и его цена
product_three = str(input("3.Продукт: "))
product_three_price = int(input("3.Цена: "))
# todo: Четвёртый продукт и его цена
product_four = str(input("4.Продукт: "))
product_four_price = int(input("4.Цена: "))
# todo: Цена пятого продукта и его цена
product_five = str(input("5.Продукт: "))
product_five_price = int(input("5.Цена: "))

if product_one_price <=0:
    print("Цена продукта не можеть быть ниже нуля и также равно нулю!")
elif product_two_price <=0:
    print("Цена продукта не можеть быть ниже нуля и также равно нулю!")
elif product_three_price <=0:
    print("Цена продукта не можеть быть ниже нуля и также равно нулю!")
elif product_four_price <=0:
    print("Цена продукта не можеть быть ниже нуля и также равно нулю!")
elif product_five_price <=0:
    print("Цена продукта не можеть быть ниже нуля и также  равно нулю!")
else:
    print("\n")
    print("----------Чек----------")
    print(f"{product_one}-----------------{product_one_price}c.") # ? Создаём чек для просотра продуктов 
    print(f"{product_two}-----------------{product_two_price}c.") # ? Продукты пишуться с с новой линии и в конце с. что означает сомони
    print(f"{product_three}-----------------{product_three_price}c.")
    print(f"{product_four}-----------------{product_four_price}c.")
    print(f"{product_five}-----------------{product_five_price}c.\n")
    # todo: Считаем все цены в итоге
    sum = product_one_price + product_two_price + product_three_price + product_four_price + product_five_price
    print(f"Без скидки----------------{sum}") # * Обениняем все прайси в месте
    print(f"Сo скидкой - 50c-----------{sum - 50}") # ? Скидка 50c.