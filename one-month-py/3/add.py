# numbers = [1,2,3,4,5,6,7,8]
# colors = ("red", "blue,", "green")
# mix = ("1, 'hello', True, 'world',2.4")

# for i in range():
#     print()
# # todo: tema 2
# n = input().split()

# odd = 0
# even = 0

# for i in n:
#     if int(i) % 2==0:
#         odd+=1
#     if int(i) % 2 !=0:
#         even+=1


# print("Odd: ", odd)
# print("Even: ", even)
# # todo: tema 3
# a = input().split()

# for i in range(0, len(a), 2):
#     print(a[i], end=" ")
# # todo: tema 4
# a = input().split()

# for i in a:
#     if int(i) % 2 == 0:
#         print(i, end=" ")
# # todo: tema 5
# a = input().split()

# count = 0

# for i in a:
#     if int(i) > 0:
#         count += 1

# print(count)
# todo: tema 6
a = input().split()

for i in range(1, len(a)):
    if int(a[i]) > int(a[i - 1]):
        print(a[i], end=" ")