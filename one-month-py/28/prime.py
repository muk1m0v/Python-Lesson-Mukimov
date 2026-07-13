# n = int(input('Enter dioposon number: '))
# i = 1
# print('Prime numbers: ')
# while i <= n:
#     cnt = 0
#     j = 1
#     while j <= i:
#         if i % j == 0:
#             cnt+=1
#         j+=1
#     if cnt<=2:
#         print(i,end=' ')
#     i+=1

n = int(input("Введите число: "))

for i in range(1, n + 1):
    print(str(i) * i)