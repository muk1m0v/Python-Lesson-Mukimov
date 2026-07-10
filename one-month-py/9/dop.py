try:
    data = []
    cnt_one = 0

    while True:
        user_print = int(input('-------------------------|\n[0] -    Удалить чек \n-------------------------|\n[1] -    Cоздать чек \n-------------------------|\n[2] -  Показать все чеки \n-------------------------|\n[3] -    Изменить чек\n-------------------------|\n[4] -       Выход \n-------------------------|\nВведите комманду: '))
        if user_print == 1:
            cnt_one += 1
            dist = {
                'chek_id':cnt_one,
                'product':[]
            }
            cnt = 0
            while True:
                print(f'-------Продукт: {cnt}-------')
                name = input(f'Имя продукта: ')
                if name == 'stop':
                    break
                elif name == '0':
                    break
                count = int(input('Количество продукта: '))
                price = int(input('Цена продукта: '))
                cnt+=1

                shablon = {
                    'id': cnt,
                    'name': name,
                    'count': count,
                    'price': price,
                }
                dist['product'].append(shablon)
            data.append(dist)
        elif user_print == 2:
            for chek in data:
                print(f'----------\nЧек ID: {chek["chek_id"]}')
                total_chek = 0
                for product in chek['product']:
                    total_product = product['count'] * product['price']
                    total_chek += total_product
                    print(f'{product["name"]}: {product["count"]} x {product["price"]} = {total_product}')
                print(f'Итого по чеку: {total_chek}')
                print('----------')
        elif user_print == 3:
            chek_id_to_edit = int(input('Укажите ID чека для изменения: '))
            found = False
            for chek in data:
                if chek['chek_id'] == chek_id_to_edit:
                    found = True
                    chek['product'] = []
                    cnt = 0
                    while True:
                        print(f'-------Продукт: {cnt}-------')
                        name = input('Имя продукта: ')
                        if name == 'stop':
                            break
                        elif name == '0':
                            break
                        count = int(input('Количество продукта: '))
                        price = int(input('Цена продукта: '))
                        cnt += 1
                        shablon = {
                            'id': cnt,
                            'name': name,
                            'count': count,
                            'price': price
                        }
                        chek['product'].append(shablon)
                    break
            if not found:
                print('Чек с таким ID не найден.')
        elif user_print == 0:
            chek_id_to_del = int(input('Укажите ID чека для удаления: '))
            found = False
            for chek in data:
                if chek['check_id'] == chek_id_to_del:
                    data.remove(chek)
                    found = True
                    print('Чек удалён.')
                    break
            if not found:
                print('Чек с таким ID не найден.')
        elif user_print == 4:
            print("Вы успешно вышли!\n")
            break
        else:
            print('Неверная комманда веддите от 0 до 4!')

    print('Все чеки: ') 
    print(data)
except:
    print('Ошибка: Введите  [int] для выполнение комманды!')