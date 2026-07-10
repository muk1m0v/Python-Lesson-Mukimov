# #todo: tema 1
# my_list = list()
# for i in range(3,31):
#     if i % 2 == 0:
#         print(i)

# print(my_list)
#todo: tema 2
# str1 = "James"

# first_char = str1[0]

# middle_index = len(str1) // 2
# middle_char = str1[middle_index]

# last_char = str1[-1]

# res = first_char + middle_char + last_char

# print(res)
# #todo: tema 3
# s1 = "JhonDipPeta"
# m1 = len(s1) // 2
# print(s1[m1 - 1 : m1 + 2])

# s2 = "JaSonAy"
# m2 = len(s2) // 2
# print(s2[m2 - 1 : m2 + 2])
#todo: tema 4
# s1 = "Ault"
# s2 = "Kelly"

# m = len(s1) // 2
# s3 = s1[:m] + s2 + s1[m:]

# print(s3)
# #todo:  tema 5
# str1 = input()

# chars = 0
# digits = 0
# symbols = 0

# for char in str1:
#     if char.isalpha():
#         chars += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         symbols += 1

# print(f"Chars = {chars}")
# print(f"Digits = {digits}")
# print(f"Symbol = {symbols}")
# #todo: tema 6
# str1 = input()

# total_sum = 0
# count = 0

# for char in str1:
#     if char.isdigit():
#         total_sum += int(char)
#         count += 1

# avg = total_sum / count

# print(f"Sum is: {total_sum} Average is  {avg}")
#todo: tema 7
# for i in range(1, 6):
#     print(*(str(i) * (6 - i)))
# #todo: tema 8
# list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# list1[1][2][2][1] = 3500
# print(list1)
# #todo: tema 9
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for x in numbers:
#     res.append(x * x)
# print(res)
#todo: tema 10
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res = [x + y for x in list1 for y in list2]
# print(res)
#todo: tema 11
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i in range(len(list1)):
#     print(list1[i], list2[-(i + 1)])
#todo: tema 12
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# res = []
# for x in list1:
#     if x != "":
#         res.append(x)
# print(res)
#todo: tema 13
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#todo: tema 14
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)
#todo: tema 15
# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
#     list1.remove(20)
# print(list1)