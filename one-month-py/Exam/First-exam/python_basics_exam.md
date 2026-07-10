
# Task 1: Age in Days

## English Description

Write a program that takes the age in years and returns the age in days.
- Use 365 days as the length of a year for this challenge.
- Ignore leap years and days between last birthday and now.
- Expect only positive integer inputs.

## Описание задачи (на русском)

Напишите программу, которая принимает возраст в годах и возвращает возраст в днях.
- Используйте 365 дней в качестве продолжительности года для этой задачи.
- Игнорируйте високосные годы и дни между последним днем рождения и настоящим моментом.
- Ожидайте только положительные целые числа в качестве ввода.


### Example:
Input: 25  
Output: 9125




# Task 2: Counting Animal Legs

## English Description

In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

- Chickens have 2 legs
- Cows have 4 legs
- Pigs have 4 legs

The farmer has counted his animals and gives you a subtotal for each species. You have to calculate and return the total number of legs for all animals.

## Описание задачи (на русском)

В этой задаче фермер просит вас подсчитать, сколько всего ног у его животных. Фермер разводит три вида животных:

- У кур — 2 ноги
- У коров — 4 ноги
- У свиней — 4 ноги

Фермер подсчитал своих животных и дает вам промежуточные данные для каждого вида. Необходимо вычислить и вернуть общее количество ног всех животных.

### Example:
Input: 2 chickens, 3 cows, 5 pigs  
Output: 36



# Task 3: Exponentiation Check

## English Description

Write a program that prints True if \(k^k = n\) for the input \((n, k)\) and prints False otherwise.

- The `^` operator refers to the exponentiation operation (**), not the bitwise XOR operation.


## Описание задачи (на русском)

Напишите программу, которая возвращает True, если \(k^k = n\) для ввода \((n, k)\), и возвращает False в противном случае.

- Оператор `^` относится к операции возведения в степень (**), а не к побитовому исключающему ИЛИ.


### Example:
Input: (4, 2)  
Output: True (2^2 = 4)

Input: (387420489, 9)  
Output: True (9^9 = 387420489)

Input: (3124, 5)  
Output: False

Input: (17, 3)  
Output: False





# Task 4: Compare String Lengths

## English Description

Create a program that takes two strings from console and shows to console either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

You are not allowed to use built-in functions like `len`.

## Описание задачи (на русском)
Создайте программу, которая берет две строки с консоли и выводит на консоль значение True или False в зависимости от того, равно ли общее количество символов в первой строке общему количеству символов во второй строке.

Вам не разрешено использовать встроенные функции, такие как `len`.


### Example:
Input: ("AB", "CD")  
Output: True (2 characters in both strings)

Input: ("ABC", "DE")  
Output: False (3 characters in the first string, 2 characters in the second)

Input: ("hello", "edabit")  
Output: False (5 characters in the first string, 6 characters in the second)


# Task 5: Difference between largest and smallest

## English Description
The sequence consists of natural numbers and ends with the number 0. Calculate the difference between the largest and smallest numbers.

## Описание задачи (на русском)
Последовательность состоит из натуральных чисел и заканчивается цифрой 0. Вычислите разницу между наибольшим и наименьшим числами.

### Example:
##### input:
2 \
3 \
1 \
6 \
4 \
0 
##### output: 5



# Task 6: Age Check for Competition

## English Description

You want to organize a competition where participants must be older than 18 years to participate. The program should ask for the age of each participant, check if they are eligible, and handle possible errors (e.g., incorrect age input). The program should keep asking for age until at least 3 participants meet the requirements.

### Conditions:
1. The program must ask for the age of participants.
2. If the age entered is invalid (not a number), the program should print an error message and ask for the input again.
3. If the age of the participant is less than 18 years, the program should print the message "Sorry, you are too young to participate" and request a new age.
4. If the participant's age is 18 years or older, the program should print "Welcome to the competition!".
5. After a valid entry, the program should continue asking for the age of the next participant until at least 3 eligible participants are entered.


## Описание задачи (на русском)

Вы хотите организовать соревнования, где участники должны быть старше 18 лет, чтобы участвовать. Программа должна запрашивать возраст каждого участника, проверять, подходит ли он для участия, и обрабатывать возможные ошибки (например, если возраст введен некорректно). Программа должна запрашивать возраст до тех пор, пока не будет введено хотя бы 3 подходящих участника.

#### Условия задачи:
1. Программа должна запрашивать возраст участников.
2. Если введен некорректный возраст (не числовое значение), программа должна вывести сообщение об ошибке и запросить ввод снова.
3. Если возраст участника меньше 18 лет, программа должна вывести сообщение "Извините, вы слишком молоды для участия" и запросить новый возраст.
4. Если возраст участника больше или равен 18 лет, программа должна вывести сообщение "Добро пожаловать на соревнования!".
5. После успешного ввода, программа должна продолжать запрашивать возраст следующего участника до тех пор, пока не будет введено хотя бы 3 подходящих участника.


### Example:

**Input:**
Enter participant's age: 16
Sorry, you are too young to participate. 
Enter participant's age: 25 
Welcome to the competition! 
Enter participant's age: thirty 
Error: Age must be a number. Try again. 
Enter participant's age: 22 
Welcome to the competition!

**Output:**
Number of participants allowed to the competition: 2


# Task7: Count how many times a digit appears in a number

## English Description

You are given two numbers: `x` (a natural number) and `d` (a digit). You need to count how many times the digit `d` appears in the number `x`. The solution should not use strings.


## Описание задачи (на русском)

Даны два числа: `x` (натуральное число) и `d` (цифра). Нужно посчитать, сколько раз цифра `d` встречается в записи числа `x`. Решение не должно использовать строки.

### Example:
**Input:**

- `x` = 6323
- `d` = 3

**Output:**
2

**Explanation:**
- The program should output `2`, as the digit `3` appears two times in `6323`.




# Task 8: Sum of Series

## English Description

Write a program to calculate the sum of the series:
(1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n).

## Описание задачи (на русском)

Напишите программу для вычисления суммы ряда:
(1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n).

### Example:
##### Input:
- Input the value for the nth term: 5

##### Output:
1 * 1 = 1 \
2 * 2 = 4 \
3 * 3 = 9 \
4 * 4 = 16 \
5 * 5 = 25 \
The sum of the above series is: 55


# Task 9: List Non-Prime Numbers

## English Description

Write a program in Python to list non-prime numbers from 1 to an upperbound.

## Описание задачи (на русском)
Напишите программу на Python для вывода всех непростых чисел от 1 до заданного верхнего предела.


### Example:

**Input:**
- Input the upper limit: 25

**Output:**
- The non-prime numbers are: 4 6 8 9 10 12 14 15 16 18 20 21 22 24 25



# Task 10: Polindrome or not

## English Description
Find polindromes. A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise. 

## Описание задачи (на русском)
Найдите палиндромы. Фраза является палиндромом, если после преобразования всех прописных букв в строчные и удаления всех небуквенно-цифровых символов она читается одинаково и вперед, и назад. Буквенно-цифровые символы включают буквы и цифры. Учитывая строку s, верните true, если это палиндром, или false в противном случае.


#### Example 1:
**Input:**
s = "A man, a plan, a canal: Panama"

**Output:** 
true

**Explanation:** 
"amanaplanacanalpanama" is a palindrome.

---------

#### Example 2:
**Input:** 
s = "race a car"

**Output:** 
false


**Explanation:**
"raceacar" is not a palindrome.

--------

#### Example 3:
**Input:**
s = " "

**Output:** 
true

**Explanation:** 
s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.