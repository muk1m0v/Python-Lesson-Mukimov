# # #? tema 1
# age_user = int(input("Enter your age: "))

# print(age_user * 365)
# #? tema 2
# chicken_user = int(input("Enter chickens: "))
# cow_user = int(input("Enter cows: "))
# pig_user = int(input("Enter pigs: "))
# chicken = 2 * chicken_user
# cow = 4 * cow_user
# pig = 4 * pig_user

# sum = pig + cow + chicken
# print(f"{chicken} chickens, {cow} cows, {pig} pigs = {sum} legs")
# #? tema 3
# first_user_number = int(input("Enter your first number: "))
# second_user_number = int(input("Enter your second number: "))

# one = first_user_number
# two = second_user_number
# sum = two ** two

# if sum == one:
#     print(f"True (two^two = {two**two})")
# else:
#     print(False)
# #? tema 4
# first_input_user = str(input("Enter your text: "))
# second_input_user = str(input("Enter your text: "))

# count_first = 0
# count_second = 0
# cnt_0 = 0
# cnt_1 = 0
# one = first_input_user
# two = second_input_user

# for text in one:
#     cnt_0+=1
# for text_2 in two:
#     cnt_1+=1

# if one == two:
#     print(f"True (2 characters in both strings)")
# else:
#     print(f"False ({cnt_0} characters in the first string, {cnt_1} characters in the second)")
# #? tema 5
# while True:
#     digits = int(input("Enter your number: "))
#     if digits == 0:
#         break
#     print(digits)
# #? tema 6
# try:
#     age_user = int(input("Enter your age: "))
#     age = age_user
#     i = 0
#     while i <=3:
#         if age >= 18:
#             print("Добро пожаловать на соревнования!")
#             i+=1
#         elif age <18:
#             print("Извините, вы слишком молоды для участия!")
#             break
# except:
#     print("Вводите число а не текст .Попробуйте с начало!")
# #? tema 7
# x = str(input("X = "))
# d = str(input("D = "))

# print(x.count(d))
# #? tema 8
# n = int(input("enter txt: "))

# total_sum = 0

# for i in range(1, n + 1):
#     square = i * i
#     total_sum += square
#     print(f"{i} * {i} = {square}")

# print(f"The sum of the above series is: {total_sum}")

# #? tema 9
# n = int(input("enter len-loop: "))
# i = 4
# while i <=n:
#     print(f"{i}", end=" ")
#     i+=1
