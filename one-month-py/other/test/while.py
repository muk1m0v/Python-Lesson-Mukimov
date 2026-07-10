user_length = int(input("Введите длину листа: "))

list = []
start = 1

while start <= user_length :
    str = f"Введите значение №{start}: "
    list.append(input(f"{str}"))
    start += 1

print(list)