# Python Practice Tasks: Nested Functions

## 📖 Introduction: What is a Nested Function?

A **nested function** (or inner function) is a function defined inside another function. It can access variables from the enclosing (outer) function's scope.

```python
def outer():
    def inner():
        print("Hello from the inner function!")
    inner()

outer()
```

---

## 🟢 Easy Tasks (⭐)

### Task 1: User Greeting System
**Description:** Write a function `greet_user(name)` that takes a user's name. Inside it, create a nested function that generates and returns a greeting message.

* **Example Input:** `"Ali"`
* **Example Output:** `"Hello, Ali!"`

### Task 2: Online Store Discount
**Description:** Write a function `final_price(price)` that takes an original price. Inside it, create a nested function that calculates and applies a 10% discount.

* **Example Input:** `100`
* **Example Output:** `90.0`

### Task 3: Password Checker
**Description:** Write a function `check_password(password)` that validates a string. Inside it, create a nested function that checks whether the password length is at least 8 characters. Return `True` or `"Valid Password"` if it matches.

* **Example Input:** `"python123"`
* **Example Output:** `"Valid Password"`

---

## 🟡 Medium Tasks (⭐⭐)

### Task 4: Student Grade Report
**Description:** Write a function `student_report(grades)` that takes a list of numbers. Inside it, create two nested functions:
* `calculate_average()` — returns the mean score.
* `find_highest()` — returns the top score.

The main function should return both values as a tuple or a formatted string.

* **Example Input:** `[80, 90, 70, 100]`
* **Example Output:** `Average: 85, Highest: 100`

### Task 5: Employee Salary Calculator
**Description:** Write a function `salary_report(base_salary)`. Inside it, create two nested functions:
* `tax()` — calculates a 15% tax deduction.
* `bonus()` — calculates a 20% bonus based on the base salary.

The main function should calculate and return the final salary (`base_salary - tax + bonus`).

* **Example Input:** `5000`
* **Example Output:** `Final Salary: 5250.0`

### Task 6: E-Commerce Order Summary
**Description:** Write a function `order_summary(prices)` that takes a list of item prices. Inside it, create nested functions to compute the total price and the average item price. Return both results.

* **Example Input:** `[100, 200, 300]`
* **Example Output:** `Total: 600, Average: 200`

### Task 7: Text Analytics
**Description:** Write a function `analyze_text(text)` that accepts a string sentence. Inside it, define two nested functions:
* `word_count()` — counts the total number of words.
* `longest_word()` — finds the longest word in the text.

* **Example Input:** `"Python is very powerful"`
* **Example Output:** `Words: 4, Longest: powerful`

---

## 🔴 Hard Tasks (⭐⭐⭐)

### Task 8: Bank Account System
**Description:** Write a function `bank_account(initial_balance)`. Inside it, define two nested functions:
* `deposit(amount)` — increases the balance.
* `withdraw(amount)` — decreases the balance if there are sufficient funds.

**Bonus Challenge:** Return these inner functions as a tuple or dictionary so they can be called from outside the `bank_account` function (Closure concept).

* **Example Setup:**
  ```python
  deposit_fn, withdraw_fn = bank_account(1000)
  deposit_fn(500)   # New balance: 1500
  withdraw_fn(200)  # New balance: 1300
  ```

### Task 9: Secure Calculator (Closures)
**Description:** Create a function `make_multiplier(factor)`. Inside it, define a nested function `multiply(number)` that multiplies its input by the `factor` provided to the outer function. Return the inner function.

* **Example Setup:**
  ```python
  double = make_multiplier(2)
  print(double(5)) # Output: 10
  
  triple = make_multiplier(3)
  print(triple(5)) # Output: 15
  ```
