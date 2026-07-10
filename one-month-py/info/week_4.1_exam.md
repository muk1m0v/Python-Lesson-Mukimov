# EXAM FOR WEEK 4
## RULES:
> No interner, no help to each other!
> Make one file and place all your work there (e.g. odina_kholiqov.py)
> Send the file at 
> You have 2 hours only
# TASK 1,2,3,6 ✅
### 4 Task
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. / Учитывая целочисленный массив nums и целое число k, верните k наиболее часто встречающихся элементов. Вы можете вернуть ответ в любом порядке.

#### Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]


### 5 Task
Случайный лотерейный выбор. Создайте 100 случайных лотерейных билетов и выберите из них два счастливых билета в качестве победителя.
    что необходимо соблюдать следующие условия::
    Номер лотереи должен состоять из 10 цифр.
    Все 100 номеров билетов должны быть уникальными.

### 7 Task
Create a recursion fucntion which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
Создайте рекурсивный функция, который может перебирать числа, кратные 7, в заданном диапазоне от 0 до n.
Input:
n = 30
Output:
7 14 21 28

### 8 Task
Write a Python program to create a calculator class. Include methods for basic arithmetic operations. / Напишите программу на Python для создания класса калькулятора. Включите методы для основных арифметических операций.

### 9 Task
Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. / Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. 



### 10 Tasks
Create a decorator premium_required that checks whether a user has a Premium subscription before allowing access to a function.

Создайте декоратор premium_required, который проверяет, есть ли у пользователя Premium-подписка.

##### Requirements / Требования
Create a decorator premium_required. / Создайте декоратор premium_required.
The decorated function receives: / Декорируемая функция принимает:

- username
- is_premium (True or False)
If is_premium is True: execute the function and return its result.(Если is_premium == True:
выполнить функцию; вернуть результат.)
If False: do not execute the function and  print: (Если False: не выполнять функцию и вывести:)
Access denied. Premium subscription required.
##### Example
```
@premium_required
def watch_course(username, is_premium):
    return f"{username} started watching the course."
```

