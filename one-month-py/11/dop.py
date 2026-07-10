# user_name = str(input('Введите ваш логин: '))
# user_input = str(input('Введите свой пароль: '))
# correct_login = 'Mukimov'
# correct_password = '7899'

# if user_input == correct_password:
#     if user_name == correct_login:
#         print('Добро пожаловать в NoteEdits!')
#     else:
#         print('Ошибка: Указан не корректный логин!')
# elif user_input == '0':
#     break
# else:
#     print('Ошибка: Указан не корректный пароль!')

# def mav_two_big(lict):
#     max1 = -999999999999999999
#     max2 = -999999999999999999
#     for k in lict:
#         if k > max1:
#             max2 = max1
#             max1 = k
#         elif k > max2:
#             max2 = k
#     return max1, max2

# old = input('Введите рузультат: ').split()
# lict = []

# for i in old:
#     num = int(i)
#     lict.append(num)

# m1, m2 = mav_two_big(lict)
# print(f'----------------------|\n Результать: {m1} - {m2}\n----------------------|')

data = []
cnt = 0

def reg(full_name, username, phone_numbers, password):
    global cnt
    cnt += 1
    user_register = {
        'id': cnt,
        'Full_name': full_name,
        'Username': username,
        'phone_numbers': phone_numbers,
        'Password': password
    }
    data.append(user_register)
    return 'Успешная Регистрация✅'

while True:
    user_input = int(input('1)Регистрация \n2)Вход в аккаунт \n0)Выход \nВведите комманду: '))
    
    if user_input == 1:
        register_menu = reg(
            input('------------\nВведите ваше полное имя: '), 
            input('Введите ваш логин: '), 
            input('Введите ваш номер телефона: +992-'), 
            input('Введите ваш пароль: ')
        )
        print(register_menu)
        
    elif user_input == 2:
        print('------------\nАвторизация')
        login_input = input('Введите ваш логин: ')
        password_input = input('Введите ваш пароль: ')
        
        account_found = False
        
        for user in data:
            if user['Username'] == login_input and user['Password'] == password_input:
                print(f"Добро пожаловать, {user['Full_name']}! Вы успешно вошли.🎉")
                account_found = True
                break
                
        if not account_found:
            print('Ошибка: Неверный логин или пароль!❌')
            
    elif user_input == 0:
        print('Вы вышли из программы!')
        break