def plus(a, b): 
    return a + b
def minus(a, b): 
    return a - b
def multiply(a, b): 
    return a * b
def divisions(a, b): 
    return a / b

cnt = 0
while True:
    n = input(f'{cnt}-Введите Значение \n------------------------\n[ + ] [ - ] [ / ] [ * ]: ')
    if n == '0':
        print('Вы успешно вышли!')
        break
    if n in ('+', '-', '*', '/'):
        try:
            a = float(input('Первое число: '))
            b = float(input('Второе число: '))
            if n == '+': print(f'Результат: {plus(a, b)}')
            elif n == '-': print(f'Результат: {minus(a, b)}')
            elif n == '*': print(f'Результат: {multiply(a, b)}')
            elif n == '/': print(f'Результат: {divisions(a, b)}')
            cnt += 1
        except ZeroDivisionError:
            print('Ошибка: Деление на ноль!')
    else:
        print('Ошибка: Неверный знак операции!')
