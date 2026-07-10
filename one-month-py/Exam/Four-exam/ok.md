# TASK 1,2,3,5,6,7,8,9 ✅ 10❌ 4💡
### Task completed ✅  |  Task not completed ❌ |  Task not understand 💡
### 4 Task
 Учитывая целочисленный массив nums и целое число k, верните k наиболее часто встречающихся элементов. Вы можете вернуть ответ в любом порядке.

#### Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

### 10 Tasks
Создайте декоратор premium_required, который проверяет, есть ли у пользователя Premium-подписка.
##### Требования
 Создайте декоратор premium_required.
 Декорируемая функция принимает:

- username
- is_premium (True или False)
Если is_premium == True:
выполнить функцию; вернуть результат.
Если False: не выполнять функцию и вывести: 
`Access denied. Premium subscription required.`
#### Example
```
@premium_required
def watch_course(username, is_premium):
    return f"{username} started watching the course."
```