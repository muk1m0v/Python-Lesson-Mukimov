def plus(a, b):
    print(a+b)

def minus(a, b):
    print(a - b)

def um(a, b):
    print(a * b)

def delen(a, b):
    print(a / b)

def ost(a, b):
    print(a // b)

def po(a , b):
    print(pow(a,b))
try:
    while True:
        choice = input ('------------\n[+] - Плюс\n[-] - Минус\n[*] - Умножение\n[/] - Деление\n[//] - Деление без остатка\n[**] - Возведение в корень\n------------\nВведите комманду: ')
        match choice:
            case '+':
                plus(int(input('Первое число: ')), int(input('Второе число: ')))
            case '-':
                minus(int(input('Первое число: ')), int(input('Второе число: ')))
            case '*':
                um(int(input('Первое число: ')), int(input('Второе число: ')))
            case '/':
                delen(float(input('Первое число: ')), float(input('Второе число: ')))
            case '//':
                ost(int(input('Первое число: ')), int(input('Второе число: ')))
            case '**':
                po(int(input('Первое число: ')), int(input('Второе число: ')))
            case _:
                print('Такой комманды не существует!')
except:
    print('Ошибка: Введите число а не строку!')