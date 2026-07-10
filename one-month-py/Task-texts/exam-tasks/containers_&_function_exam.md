## Task 1. Word Count

### 🇬🇧 English
Write a function:

```python
count_words(text)
```

The function receives a string consisting of words separated by spaces.

Print the number of words in the string.

### 🇷🇺 Русский
Напишите функцию:

```python
count_words(text)
```

Функция получает строку, состоящую из слов, разделённых пробелами.

Выведите количество слов в строке.

### Input

```text
lorem ipsum dolor
```

### Output

```text
3
```

---

## Task 2. Longest Word

### 🇬🇧 English
Write a function:

```python
longest_word(text)
```

The function receives a string.

Print:

1. The longest word
2. Its length

If there are several longest words, print the first one.

### 🇷🇺 Русский
Напишите функцию:

```python
longest_word(text)
```

Функция получает строку.

Выведите:

1. Самое длинное слово
2. Его длину

Если таких слов несколько, выведите первое.

### Input

```text
one two three four five six
```

### Output

```text
three
5
```

---

## Task 3. Smallest Odd Number

### 🇬🇧 English
Write a function:

```python
smallest_odd(numbers)
```

The function receives a list of integers.

Return the smallest odd number.

If there are no odd numbers, return `0`.

### 🇷🇺 Русский
Напишите функцию:

```python
smallest_odd(numbers)
```

Функция получает список целых чисел.

Верните наименьшее нечётное число.

Если нечётных чисел нет, верните `0`.

### Input

```text
0 1 2 3 4
```

### Output

```text
1
```

---

## Task 4. Unique Visitors (SET)

### 🇬🇧 English
Write a function:

```python
unique_visitors(visitors)
```

The function receives a list of website visitors.

Return the number of unique visitors.

### 🇷🇺 Русский
Напишите функцию:

```python
unique_visitors(visitors)
```

Функция получает список посетителей сайта.

Верните количество уникальных посетителей.

### Input

```python
["Ali", "Ali", "Sara", "Kamol"]
```

### Output

```text
3
```

---


## Task 5. Vowel Sum (DICT)

### 🇬🇧 English
Write a function:

```python
vowel_sum(text)
```

Use the dictionary:

```python
{
    "A": 4,
    "E": 3,
    "I": 1,
    "O": 0,
    "U": 0
}
```

Calculate and return the total vowel score.

### 🇷🇺 Русский
Напишите функцию:

```python
vowel_sum(text)
```

Используйте словарь:

```python
{
    "A": 4,
    "E": 3,
    "I": 1,
    "O": 0,
    "U": 0
}
```

Посчитайте и верните сумму гласных.

### Input

```text
Do I get the correct output?
```

### Output

```text
10
```

---

## Task 6. Censor Words

### 🇬🇧 English
Write a function:

```python
censor_words(text)
```

Replace every word longer than 4 characters with:

```text
*****
```

Return the modified sentence.

### 🇷🇺 Русский
Напишите функцию:

```python
censor_words(text)
```

Замените каждое слово длиной более 4 символов на:

```text
*****
```

Верните изменённую строку.

### Input

```text
The code is fourty
```

### Output

```text
The code is *****
```

---

## Task 7. Product Price Lookup (DICT)

### 🇬🇧 English
Write a function:

```python
get_price(products, product_name)
```

The function receives a dictionary of products and prices.

Return the price of the requested product.

If the product does not exist, return:

```text
Not Found
```

### 🇷🇺 Русский
Напишите функцию:

```python
get_price(products, product_name)
```

Функция получает словарь товаров и цен.

Верните цену указанного товара.

Если товар не найден, верните:

```text
Not Found
```

### Input

```python
products = {
    "Laptop": 8000,
    "Mouse": 150
}

product_name = "Laptop"
```

### Output

```text
8000
```

---

## Task 8. Common Friends (SET)

### 🇬🇧 English
Write a function:

```python
common_friends(user1, user2)
```

Return all common friends.

### 🇷🇺 Русский
Напишите функцию:

```python
common_friends(user1, user2)
```

Верните всех общих друзей.

### Input

```python
{"Ali", "Sara", "Kamol"}
{"Sara", "Madina", "Ali"}
```

### Output

```python
{"Ali", "Sara"}
```

---


## Task 9. Employee Performance Report

### 🇬🇧 English
Write a function:

```python
employee_report(employees)
```

The function receives a dictionary where:

- key = employee name
- value = completed tasks

Return the name of the most productive employee and the number of completed tasks.

### 🇷🇺 Русский
Напишите функцию:

```python
employee_report(employees)
```

Функция получает словарь, где:

- ключ = имя сотрудника
- значение = количество выполненных задач

Верните имя самого продуктивного сотрудника и количество выполненных задач.

### Input

```python
{
    "Ali": 15,
    "Sara": 22,
    "Kamol": 18,
    "Madina": 20
}
```

### Output

```text
Sara
22
```

---

## Task 10. Stock Profit Maximization

### 🇬🇧 English
Write a function:

```python
max_profit(prices)
```

You are given a list where `prices[i]` is the stock price on day `i`.

Return the maximum profit from one buy and one sell operation.

If profit is impossible, return `0`.

### 🇷🇺 Русский
Напишите функцию:

```python
max_profit(prices)
```

Дан список цен акций, где `prices[i]` — цена в день `i`.

Верните максимальную прибыль от одной покупки и одной продажи.

Если прибыль получить невозможно, верните `0`.

### Input

```python
[7, 1, 5, 3, 6, 4]
```

### Output

```text
5
```