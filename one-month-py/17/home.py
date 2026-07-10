# #! TASK 1
# def countdown(n):
#     if n <= 0:
#         return
#     print(n, end=" ")
#     countdown(n - 1)

# n = int(input('Enter the number: '))
# countdown(n)
#! TASK 2
# def folder_depth(n):
#     if n <= 0:
#         return ""
#     if n == 1:
#         return "Folder"
#     return "Folder -> " + folder_depth(n - 1)

# n = int(input('Введите кол-во папок: '))
# print(folder_depth(n))
#! TASK 3
# def triangle_pattern(n, current=1):
#     if current > n:
#         return
#     print("*" * current)
#     triangle_pattern(n, current + 1)

# n = int(input())
# triangle_pattern(n)
#! TASK 4
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     return s[-1] + reverse_string(s[:-1])

# s = input()
# print(reverse_string(s))
#! TASK 5
# def sum_of_list(lst):
#     if not lst:
#         return 0
#     return lst[0] + sum_of_list(lst[1:])

# print(sum_of_list([4, 8, 3]))
#! TASK 6
# def count_elements(lst):
#     if not isinstance(lst, list):
#         return 1
#     if not lst:
#         return 0
#     return count_elements(lst[0]) + count_elements(lst[1:])

# lst = [1, [2, 3], [4, [5, 6,3]]]
# print(count_elements(lst))
#! TASK 7