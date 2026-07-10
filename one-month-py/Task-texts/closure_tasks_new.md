# 🧠 Python Closures – Practice Tasks (Set 2)

## 🟢 Beginner Level

### 1. 🎫 Ticket Generator
Create `create_ticket_generator()`:

- returns a function
- each call generates a new ticket number
- numbering starts from 1001

Example:
1001 → 1002 → 1003 ...

---

### 2. 💵 Fixed Tax Calculator
Create `create_tax_calculator(tax_percent)`:

- stores tax percentage inside closure
- returned function accepts product price
- returns final price including tax

---

### 3. 📝 Name Formatter
Create `create_name_formatter(prefix)`:

- stores prefix inside closure
- returned function accepts a name
- returns formatted string

Example:
Mr. + John → Mr. John

---

### 4. 🔢 Number Adder
Create `create_adder(number)`:

- stores a number
- returned function adds stored number to input

Example:
Stored: 10
Input: 5
Output: 15

---

### 5. ❤️ Like Counter
Create `create_like_counter()`:

- stores number of likes
- each call increases likes by 1
- returns current number of likes

---

## 🟡 Normal Level

### 6. 🏦 Bank Account Balance
Create `create_account(initial_balance)`:

Returned function should:

- accept deposit amount
- update balance
- return current balance

Balance must be stored inside closure.

---

### 7. 📧 Email Sender Simulator
Create `create_email_sender(sender_email)`:

Returned function:

- accepts receiver email
- accepts message
- prints simulated sending information

Sender email should be stored inside closure.

---

### 8. 🎮 Game Score Tracker
Create `create_score_tracker()`:

Returned function:

- accepts earned points
- updates total score
- returns current score

Score must persist between calls.

---

### 9. 🚀 API Rate Limiter
Create `create_rate_limiter(max_requests)`:

Returned function:

- tracks number of requests
- allows requests until limit is reached
- returns appropriate status

Request count must be stored in closure.

---

### 10. 🛒 Product Inventory Tracker
Create `create_inventory(initial_stock)`:

Returned function:

- accepts sold quantity
- decreases stock
- returns remaining stock

Stock should be stored inside closure.

---

## 🔥 Bonus Challenge

### 11. 🎓 Student Grade Book

Create `create_grade_book(student_name)`:

Returned function:

- accepts a new grade
- stores all grades
- returns current average grade

All grades must be stored inside the closure without using classes.