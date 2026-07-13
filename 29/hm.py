# #! TASK 1:
# n = input('Enter the num: ').split() 
# cnt = 0 
# i = 0 

# while i < len(n): 
#     cnt += int(n[i]) 
#     i += 1 

# print(f'Total: {cnt}')
#! TASK 2:
# n = input('Enter: ').split()
# print(f'Len - List: {len(n)}')
#! TASK 3:
# n = input().split()
# m = int(n[0]) 

# i = 1
# while i < len(n):
#     if int(n[i]) > m: 
#         m = int(n[i])
#     i += 1

# print(f'Maximal: {m}')
#! TAKS 4:
# n = input().split()
# m = int(n[0]) 

# i = 1
# while i < len(n):
#     if int(n[i]) < m: 
#         m = int(n[i])
#     i += 1

# print(f'Minimal: {m}')
#! Tasks 5:
# n = input().split()
# cnt = 0
# for i in n:
#     k = int(i)
#     if k > 0:
#         cnt+=1

# print(f'Positive: {cnt}')
#! TASKS 6:
# n = input().split()
# cnt = 0
# for i in n:
#     k = int(i)
#     if k % 2 == 0:
#         cnt+=1

# print(f'Even: {cnt}')
#! Tasks 7:
# lst = [1, 2, 3]
# lst.reverse()
#! TASKS 8:
# n = [5,3,1,2,4]
# n.sort()
# print(n)
#! TASKS 9:
# numbers = list(map(int, input().split()))
# numbers.sort()
# print(numbers[::-1])
#! TASKS 10:
# n = input().split()
# n.pop()
# print(n)
#! Tasks 11:
# n = input().split()
# x = int(input())
# n.pop(x)
# print(n)
#! TASKS 12:
# n = input().split()
# x = input()
# cnt = 0
# for i in n:
#     if i == x:
#         cnt+=1

# print(f'Всего встреч: {cnt}')
#! TASKS 13:
# n = input().split()
# x = input()
# for i  in n:
#     if i == x:
#         print(f'Index: {n.index(i)}')
#! TAKS 14:
# n = input().split()
# x = input()
# n.append(x)
# print(n)
#! TASKS 15:
# n = input().split()
# l = []
# for i in n:
#     o = int(i)
#     if o > 0:
#         l.append(o)

# print(l)
#! TASKS 16:
# n = input().split()
# cnt = 0
# for i in n:
#     o = int(i)
#     if o % 2 == 0:
#         cnt+=o

# print(f'Total: {cnt}')
#! TASKS 17:
# i = list(map(int, input().split()))
# o = []

# for item in i:
#     if item not in o:
#         o.append(item)

# print(o)
#! TASKS 18:
# l = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     l.append(n)

# print(l)
#! TASKS 19:
# n = input().split()
# cnt = 0
# for i in n:
#     k = int(i)
#     cnt+=k
#     j = cnt // len(n)

# print(f'Среднее арифметическое: {j}')
#! Task 20
# n = input().split()
# t = []
# for i in n:
#     u = int(i)
#     l = u * u
#     t.append(l)
# print(t)