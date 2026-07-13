# #! Exam Tasks 1:
# a = int(input())
# b = int(input())
# for i in range(b-1,a,-1):
#     print(i)
#! Exam Tasks 2:
# cnt = 0
# n = int(input())
# for i in range(1,10):
#     if n % i == 0:
#         cnt+=1
# if cnt > 2:
#     print('Is Not Prime number')
# else:
#     print('Is Prime Number')
#! Exam Tasks 3;
# num = input()
# ok = 0
# for i in num:
#     it = int(i)
#     ok+=it
# print(f'Total: {ok}')
#! Exam Tasks 4;
# ok = int(input())
# it = 0
# for i in range(1,ok + 1,+1):
#     k = i * i
#     print(f'{i}*{i} = {k}')
#     it+=k
# print(f'The sum of the above series is: {it}')
#! Exam tasks 5:
# n = int(input())
# print('The non-prime numbers are:')
# for i in range(1,10):
#     if n % i == 0:
#         cnt+=1
#     cnt = 0
#     for o in range(1,n+1):
#         if cnt > 3:
#             print(i)
#! Exam Tasks 6:
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(a,b + 1):
#     if i % d == c:
#         print(i,end=' ')
#!Exam Tasks 7;
# x = input()
# d = input()
# cnt = 0
# for i in x:
#     if i == d:
#         cnt+=1
# print(f'Total: {cnt}')
#!Exam Tasks 8:
# num = input('Input the num:\n>>> ')

# i = len(num)
# while i>0:
#     print(num[i-1],end='')
#     i-=1
#! Exam Tasks 9:
# n = int(input("Input number: "))
# result = []
# for i in range(n):
#     result.append(2 * i + 1)
# total = sum(result)

# print('The odd numbers are:')
# for i in result:
#     print(i, end=' ')
# print()

# print(f"The Sum of odd Natural Numbers upto {n} terms: {total}")
#! Exam Tasks 10:
# n = int(input())
# m = int(input())
# cnt = 0
# print(f'Numbers between {n} and {m}, divisible by 9:')
# for i in range(n,m):
#     if i % 9 == 0:
#         print(i,end=' ')
#         cnt+=i
# print(f'\nThe sum: {cnt}')