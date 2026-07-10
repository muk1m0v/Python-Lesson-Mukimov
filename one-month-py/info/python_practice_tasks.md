# Python Practice Tasks / Задачи для практики по Python

*Tasks in each topic are ordered from simpler to more challenging.*
*Задачи в каждой теме расположены от простых к более сложным.*

---

## 1. Input / Output — 5 tasks / 5 задач

### 1.1
**EN:** Write a program that reads a user's name from input and prints a personalized greeting.
**RU:** Напишите программу, которая считывает имя пользователя и выводит персональное приветствие.

```
Input:  Alice
Output: Hello, Alice! Welcome!
```

### 1.2
**EN:** Read two integers from input, on one line separated by a space, and print their sum.
**RU:** Считайте два целых числа из ввода (в одной строке через пробел) и выведите их сумму.

```
Input:  7 15
Output: 22
```

### 1.3
**EN:** Read the total bill amount and the number of people (comma separated), calculate and print how much each person should pay, rounded to 2 decimal places.
**RU:** Считайте сумму счёта и количество человек (через запятую), вычислите и выведите сумму на каждого, округлённую до 2 знаков после запятой.

```
Input:  1500, 4
Output: Each person pays: 375.00
```

### 1.4
**EN:** Read multiple lines of text until an empty line is entered, then print the total number of words.
**RU:** Считайте несколько строк текста до пустой строки, затем выведите общее количество слов.

```
Input:
Python is great
I love programming
(empty line)

Output: Total words: 6
```

### 1.5
**EN:** Read a log line in the format `TIMESTAMP|LEVEL|MESSAGE` (e.g. `2024-05-01 10:23:00|ERROR|Disk full`) and print a nicely formatted report line.
**RU:** Считайте строку лога в формате `TIMESTAMP|LEVEL|MESSAGE` и выведите красиво отформатированную строку отчёта.

```
Input:  2024-05-01 10:23:00|ERROR|Disk full
Output: [ERROR] at 2024-05-01 10:23:00 -> Disk full
```

---

## 2. Conditions (if / match) — 6 tasks / 6 задач

### 2.1 — `if`
**EN:** Write a function that takes a number and returns whether it is positive, negative, or zero.
**RU:** Напишите функцию, которая принимает число и возвращает, является ли оно положительным, отрицательным или нулём.

```
Input:  -5
Output: Negative
```

### 2.2 — `if / elif`
**EN:** Given a package weight in kg and a destination (`"local"` or `"international"`), calculate the shipping cost with the following rules: local & <5kg = $5, local & ≥5kg = $10, international & <5kg = $20, international & ≥5kg = $35.
**RU:** По весу посылки (кг) и пункту назначения (`"local"`/`"international"`) рассчитайте стоимость доставки по правилам: local и <5кг = $5, local и ≥5кг = $10, international и <5кг = $20, international и ≥5кг = $35.

```
Input:  weight=6, destination="international"
Output: Shipping cost: $35
```

### 2.3 — nested `if`
**EN:** Write a function that checks a password's strength using nested `if` statements based on four criteria: length ≥ 8, has an uppercase letter, has a digit, has a special character. Return `"Weak"`, `"Medium"`, or `"Strong"` depending on how many criteria are met.
**RU:** Напишите функцию проверки силы пароля с вложенными `if` по четырём критериям: длина ≥ 8, есть заглавная буква, есть цифра, есть спецсимвол. Верните `"Weak"`, `"Medium"` или `"Strong"` в зависимости от количества выполненных критериев.

```
Input:  "Pass123!"
Output: Strong
```

### 2.4 — `match`
**EN:** Using `match`-`case`, given a traffic light color (`"red"`, `"yellow"`, `"green"`), print the corresponding driver action.
**RU:** Используя `match`-`case`, по цвету светофора выведите соответствующее действие водителя.

```
Input:  "yellow"
Output: Slow down, prepare to stop
```

### 2.5 — `match`
**EN:** Using `match`-`case`, implement a calculator that takes two numbers and an operator string (`"+"`, `"-"`, `"*"`, `"/"`) and returns the result.
**RU:** Используя `match`-`case`, реализуйте калькулятор, принимающий два числа и оператор, и возвращающий результат.

```
Input:  10, 4, "*"
Output: 40
```

### 2.6 — `match` with guards
**EN:** Using `match`-`case` with guards (`case _ if ...`), classify an HTTP status code into categories: Informational (1xx), Success (2xx), Redirection (3xx), Client Error (4xx), Server Error (5xx), Unknown.
**RU:** Используя `match`-`case` с условиями (`guards`), классифицируйте HTTP-код статуса по категориям: Informational (1xx), Success (2xx), Redirection (3xx), Client Error (4xx), Server Error (5xx), Unknown.

```
Input:  404
Output: Client Error
```

---

## 3. Loops (while / for) — 6 tasks / 6 задач

### 3.1 — `while`
**EN:** Write a program that counts down from a given number N to 1 using a `while` loop, printing each number, then prints `"Liftoff!"`.
**RU:** Напишите программу обратного отсчёта от N до 1 с помощью цикла `while`, затем выведите `"Liftoff!"`.

```
Input:  5
Output:
5
4
3
2
1
Liftoff!
```

### 3.2 — `while`
**EN:** Given a secret number and a list of guesses, simulate a guessing game with a `while` loop: for each guess print `"Too high"`, `"Too low"`, or `"Correct!"`, and stop as soon as the guess is correct.
**RU:** Дано загаданное число и список попыток. Смоделируйте игру угадывания с помощью `while`: выводите подсказку `"Too high"`, `"Too low"` или `"Correct!"` для каждой попытки и остановитесь при правильной попытке.

```
Input:  secret=7, guesses=[3, 9, 7, 5]
Output:
3 -> Too low
9 -> Too high
7 -> Correct!
```

### 3.3 — `while`
**EN:** Simulate an ATM that allows a maximum of 3 PIN attempts using a `while` loop. Given the correct PIN and a list of entered PINs, print the result for each attempt and stop early on success, or after 3 failures the card is blocked.
**RU:** Смоделируйте банкомат с максимум 3 попытками ввода PIN с помощью `while`. Выведите результат для каждой попытки, остановитесь при успехе или заблокируйте карту после 3 неудач.

```
Input:  correct_pin="4521", attempts=["1111", "4521"]
Output:
Attempt 1: Incorrect PIN
Attempt 2: Access granted
```

### 3.4 — `for`
**EN:** Write a function using a `for` loop that calculates the sum of all numbers in a list.
**RU:** Напишите функцию с циклом `for`, вычисляющую сумму всех чисел в списке.

```
Input:  [1, 2, 3, 4, 5]
Output: 15
```

### 3.5 — `for`
**EN:** For numbers 1 to N, print `"Fizz"` if divisible by 3, `"Buzz"` if divisible by 5, `"FizzBuzz"` if divisible by both, otherwise print the number.
**RU:** Для чисел от 1 до N выведите `"Fizz"` при делении на 3, `"Buzz"` при делении на 5, `"FizzBuzz"` при делении на оба, иначе — само число.

```
Input:  15
Output: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
```

### 3.6 — nested `for`
**EN:** Given a matrix (a list of lists), use nested `for` loops to compute and print its transpose.
**RU:** Дана матрица (список списков), с помощью вложенных циклов `for` вычислите и выведите её транспонирование.

```
Input:  [[1, 2, 3], [4, 5, 6]]
Output: [[1, 4], [2, 5], [3, 6]]
```

---

## 4. Containers (list, tuple, dict, set) — 12 tasks / 12 задач

### 4.1 — `list`
**EN:** Write a function that removes duplicate elements from a list while preserving the original order.
**RU:** Напишите функцию удаления дубликатов из списка с сохранением исходного порядка.

```
Input:  [3, 1, 3, 2, 1, 5]
Output: [3, 1, 2, 5]
```

### 4.2 — `list`
**EN:** Write a function that finds the second largest distinct number in a list.
**RU:** Напишите функцию поиска второго по величине уникального числа в списке.

```
Input:  [10, 5, 8, 10, 3]
Output: 8
```

### 4.3 — `list`
**EN:** Given a list of intervals (as tuples), merge all overlapping intervals and return the result sorted.
**RU:** Дан список интервалов (кортежей), объедините все пересекающиеся интервалы и верните отсортированный результат.

```
Input:  [(1, 3), (2, 6), (8, 10), (15, 18)]
Output: [(1, 6), (8, 10), (15, 18)]
```

### 4.4 — `tuple`
**EN:** Using tuple unpacking, write code that swaps the values of two variables without a temporary variable.
**RU:** Используя распаковку кортежей, напишите код обмена значениями двух переменных без временной переменной.

```
Input:  a=5, b=10
Output: a=10, b=5
```

### 4.5 — `tuple`
**EN:** Given two points as tuples `(x, y)`, write a function that calculates the Euclidean distance between them.
**RU:** Даны две точки в виде кортежей `(x, y)`, напишите функцию вычисления евклидова расстояния между ними.

```
Input:  (0, 0), (3, 4)
Output: 5.0
```

### 4.6 — `tuple`
**EN:** Given a list of tuples `(course_name, grade, credit_hours)`, calculate the weighted GPA — `sum(grade * credits) / sum(credits)` — rounded to 2 decimal places.
**RU:** Дан список кортежей `(курс, оценка, кредит-часы)`, вычислите средневзвешенный балл GPA, округлённый до 2 знаков.

```
Input:  [("Math", 4.0, 3), ("History", 3.0, 2), ("Art", 3.5, 1)]
Output: GPA: 3.67
```

### 4.7 — `dict`
**EN:** Write a function that counts how many times each word appears in a sentence and returns a dictionary.
**RU:** Напишите функцию подсчёта частоты слов в предложении, возвращающую словарь.

```
Input:  "the cat sat on the mat the cat ran"
Output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'ran': 1}
```

### 4.8 — `dict`
**EN:** Write a function that inverts a dictionary, so that values become keys and keys become values (assume all values are unique).
**RU:** Напишите функцию инвертирования словаря, чтобы значения стали ключами, а ключи — значениями (значения уникальны).

```
Input:  {'a': 1, 'b': 2, 'c': 3}
Output: {1: 'a', 2: 'b', 3: 'c'}
```

### 4.9 — `dict`
**EN:** Given a list of employee dictionaries with keys `"name"`, `"department"`, `"salary"`, group them by department and calculate the average salary per department.
**RU:** Дан список словарей сотрудников с ключами `"name"`, `"department"`, `"salary"`, сгруппируйте их по отделу и посчитайте среднюю зарплату по каждому отделу.

```
Input:  [{"name": "Ann", "department": "IT", "salary": 3000},
         {"name": "Bob", "department": "IT", "salary": 4000},
         {"name": "Cara", "department": "HR", "salary": 2500}]
Output: {'IT': 3500.0, 'HR': 2500.0}
```

### 4.10 — `set`
**EN:** Write a function using sets that finds the common elements between two lists.
**RU:** Напишите функцию с использованием множеств для поиска общих элементов двух списков.

```
Input:  [1, 2, 3, 4], [3, 4, 5, 6]
Output: {3, 4}
```

### 4.11 — `set`
**EN:** Write a function using a set that checks whether all characters in a string are unique.
**RU:** Напишите функцию с использованием множества, проверяющую, все ли символы в строке уникальны.

```
Input:  "python"
Output: True
```

### 4.12 — `set`
**EN:** Given a dictionary mapping each person to a set of their friends, write a function that recommends new friends for a person — friends-of-friends who are not already their friends (and not the person themselves).
**RU:** Дан словарь, отображающий каждого человека на множество его друзей, напишите функцию рекомендации новых друзей — друзья друзей, которые ещё не являются друзьями (и не сам человек).

```
Input:  friends = {"Alice": {"Bob", "Carl"}, "Bob": {"Alice", "Dave"},
                   "Carl": {"Alice"}, "Dave": {"Bob"}}
        person = "Alice"
Output: {'Dave'}
```

---

## 5. Functions (simple, nested, closure, recursion, decorator) — 10 tasks / 10 задач

### 5.1 — simple function
**EN:** Write a simple function that calculates the area of a rectangle given its width and height.
**RU:** Напишите простую функцию вычисления площади прямоугольника по ширине и высоте.

```
Input:  width=5, height=3
Output: 15
```

### 5.2 — simple function with default/keyword args
**EN:** Write a function with default and keyword arguments that calculates the final price after a discount (default `discount=10`) and returns a formatted string.
**RU:** Напишите функцию со значением по умолчанию и именованными аргументами, вычисляющую итоговую цену со скидкой (по умолчанию `discount=10`).

```
Input:  price=200, discount=25
Output: Final price: $150.00
```

### 5.3 — nested function
**EN:** Write a function `calculate_total(price)` that contains a nested function `add_tax(amount)` which adds 8% tax, and returns the total.
**RU:** Напишите функцию `calculate_total(price)`, содержащую вложенную функцию `add_tax(amount)`, добавляющую налог 8%, и возвращающую итоговую сумму.

```
Input:  price=100
Output: Total: 108.0
```

### 5.4 — nested function
**EN:** Write a function `make_table(n)` that uses a nested function to generate and print the multiplication table for `n` (for multipliers 1 to 10).
**RU:** Напишите функцию `make_table(n)`, использующую вложенную функцию для генерации и вывода таблицы умножения для `n` (для множителей от 1 до 10).

```
Input:  n=3
Output: 3 6 9 12 15 18 21 24 27 30
```

### 5.5 — closure
**EN:** Write a function `make_counter()` that returns a closure which increments and returns a counter value each time it is called.
**RU:** Напишите функцию `make_counter()`, возвращающую замыкание, увеличивающее и возвращающее значение счётчика при каждом вызове.

```
Input:  counter = make_counter()
        counter(); counter(); counter()
Output: 1, 2, 3
```

### 5.6 — closure
**EN:** Write a function `make_fibonacci()` that returns a closure using an internal cache (dict) to compute Fibonacci numbers efficiently via memoization.
**RU:** Напишите функцию `make_fibonacci()`, возвращающую замыкание с внутренним кэшем (словарём) для эффективного вычисления чисел Фибоначчи через мемоизацию.

```
Input:  fib = make_fibonacci()
        fib(10)
Output: 55
```

### 5.7 — recursion
**EN:** Write a recursive function to calculate the factorial of a number.
**RU:** Напишите рекурсивную функцию вычисления факториала числа.

```
Input:  5
Output: 120
```

### 5.8 — recursion
**EN:** Write a recursive function that flattens an arbitrarily nested list into a single flat list.
**RU:** Напишите рекурсивную функцию, разворачивающую произвольно вложенный список в один плоский список.

```
Input:  [1, [2, 3, [4, [5, 6]], 7]]
Output: [1, 2, 3, 4, 5, 6, 7]
```

### 5.9 — decorator
**EN:** Write a decorator `@timer` that measures and prints how long a function takes to execute.
**RU:** Напишите декоратор `@timer`, измеряющий и выводящий время выполнения функции.

```
Input:  @timer applied to a function that sleeps for 1 second
Output: Function 'slow_func' took 1.00 seconds
```

### 5.10 — decorator with arguments
**EN:** Write a decorator factory `@retry(times=3)` that retries a function up to N times if it raises an exception, before finally giving up.
**RU:** Напишите фабрику декораторов `@retry(times=3)`, повторяющую вызов функции до N раз при возникновении исключения, прежде чем сдаться.

```
Input:  @retry(times=3) applied to a function that fails twice, then succeeds
Output:
Attempt 1 failed: ConnectionError
Attempt 2 failed: ConnectionError
Attempt 3 succeeded: Data loaded
```

---

## 6. Datetime and Random — 3 tasks / 3 задачи

### 6.1
**EN:** Write a function that takes a birth date and calculates the current age in years using the `datetime` module.
**RU:** Напишите функцию, вычисляющую текущий возраст в годах по дате рождения с использованием модуля `datetime`.

```
Input:  birth_date="2000-05-15"
Output: Age: 25   (based on today's date, e.g. 2026-07-02)
```

### 6.2
**EN:** Write a function that generates a random password of a given length using letters, digits, and punctuation from the `random` and `string` modules.
**RU:** Напишите функцию генерации случайного пароля заданной длины, используя буквы, цифры и символы из модулей `random` и `string`.

```
Input:  length=10
Output: aB3!kZ9$mQ   (result varies on every run)
```

### 6.3
**EN:** Write a program that generates N test events with random start times within a day (use `random.seed(...)` for reproducibility), and checks for scheduling conflicts using `datetime` comparisons.
**RU:** Напишите программу, генерирующую N тестовых событий со случайным временем начала в течение дня (используйте `random.seed(...)` для воспроизводимости), и проверяющую конфликты расписания с помощью сравнения `datetime`.

```
Input:  random.seed(42); generate 3 events, each 1 hour long
Output:
Event 1: 09:00-10:00
Event 2: 09:30-10:30 -> Conflict with Event 1
Event 3: 14:00-15:00 -> No conflict
```

---

**Total: 42 tasks / 42 задачи**
(Input/Output: 5, Conditions: 6, Loops: 6, Containers: 12, Functions: 10, Datetime & Random: 3)
