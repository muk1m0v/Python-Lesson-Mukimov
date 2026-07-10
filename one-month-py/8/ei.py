data = []
user_id_counter = 1 
user_logined = None

while True:
    if user_logined == None:

        user_input = int(input("1)Register \n2)log in \n3)Exit \nChouse func: "))

        if user_input == 1:
            shablon = {
                'id': user_id_counter,
                'full_name': input('Full name: '),
                'Username': input('Username: '),
                'Password': input('Password: '),
                'age': int(input("Age: ")),
                'is_login': False,
            }
            user_id_counter += 1
            data.append(shablon)
            print("Регистрация успешна!")

        elif user_input == 2:
            login_username = input('Enter Username: ')
            login_password = input('Enter Password: ')

            found = False

            for user in data:
                if user['Username'] == login_username and user['Password'] == login_password:
                    user['is_login'] = True
                    print(f"Добро пожаловать, {user['full_name']}! Вы успешно вошли.")
                    found = True
                    user_logined=user
                    break 
                
            if not found:
                print("Ошибка: Неверный Username или Password!")

        elif user_input == 3:
            print('Вы вишли из аккаунта!')
            break
    else:
        user_value = int(input("1)View Profile \n2)log out \n3)Exit \nEnter the command: ")) 
        if user_value == 1:
            print(f'Полное имя: {user['full_name']}')  
            print(f"Никнейм: {user['Username']}")   
            print(f"Возраст: {user['Password']}") 
            print(f"Ваш уникальный номер: {user['id']}")  
        elif user_value == 2:
            user['is_login'] = False
            user_logined = None
            print(f"{user['Username']} вы успешно вышли из аккаунта!")
        elif user_value == 3:
            print("Вы вишлы из приложения!")
            break
        else:
            print("Не правильная команда ведите от 1 до 3")

print("\nТекущая база данных пользователей:")
print(data)