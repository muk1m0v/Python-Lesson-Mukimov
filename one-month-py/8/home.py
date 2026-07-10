'''
1. Removing Duplicates / Удаление дубликатов

**Problem / Задача**
Given a list of numbers with duplicate values, create a new list without duplicates.

Дан список чисел с повторяющимися значениями. Создайте новый список без дубликатов.

---
'''
#?task 1
# numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 7, 7, 8, 9, 8, 9]
# result = list(set(numbers))
# print(result)
'''
### 2. Finding Common Elements / Поиск общих элементов

#### **Problem / Задача**
Given two lists, find all elements that appear in both.

Даны два списка. Найдите все элементы, которые встречаются в обоих.

---
'''
#?task 2
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements = list(set(list1).intersection(list2))

# print(common_elements)
"""
### 3. Finding Common Elements in Multiple Lists / Поиск общих элементов в нескольких списках

#### **Problem / Задача**
Given multiple lists, find all elements that appear in all of them.

Дано несколько списков. Найдите все элементы, которые встречаются во всех.

---
"""
#?task 3
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 4, 6, 7]
# list3 = [3, 4, 5, 8, 9]

# common_elements = set(list1).intersection(list2, list3)
# list_menu = list(common_elements)
# count = len(common_elements)

# print(f"Общие элементы: {list_menu}")
# print(f"Количество общих чисел: {count}")
'''
### 4. Difference Between Multiple Lists / Разница между несколькими списками

#### **Problem / Задача**
Given multiple lists, find elements that are in the first but not in any of the others.

Дано несколько списков. Найдите элементы, которые есть в первом, но нет ни в одном из остальных.

---
'''
#?task 4
# list1 = [1, 2, 3, 4, 5, 6]

# other_lists = [[3, 4, 7], [5, 8, 9], [6, 10]]

# result_set = set(list1)

# result = list(result_set.difference(*other_lists))

# print(result)
'''

### 5. Checking for Unique Elements / Проверка на уникальные элементы

#### **Problem / Задача**
Check if all elements in a list are unique.

Проверьте, содержатся ли в списке только уникальные элементы.

---
'''
#? task 5
# my_list = [1, 2, 3, 2, 5]

# if len(my_list) == len(set(my_list)):
#     print("no")
# else:
#     print("yes")
