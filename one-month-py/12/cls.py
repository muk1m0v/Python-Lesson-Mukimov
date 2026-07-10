# numbers = [int(i) for i in input().split() if int(i)%2==0]
# print(numbers)
#? TASK 1
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# lict = []
# while a<=b:
#     lict.append(a)
#     a-=1

# print('-----Your List-----')
# print(lict)
#? TASK 2
# a = int(input('Enter the number: '))
# i = 1
# cnt = 0
# while i <= a:
#     if a%i == 0:
#         cnt+=1
#     i+=1

# if cnt> 2:
#     print('Number is not Prime')
# else:
#     print('Number is Prime')
#? TASK 3
# dict = {12:34, 43:32}
# for i in dict:
#     print(i)
my_set = set()
my_set1 = {1,2,'bye',3,4,5}
for i in my_set1:
    print(f'Result: {i}')