# 🧠 Python Closures – Practice Tasks

## 🟢 Beginner Level (Very Easy)

### 1. ➕ Counter
Create `make_counter()`:
- returns a function
- each call increases value by 1
- returns current count

---

### 2. 🎯 Greeter
Create `make_greeter(name)`:
- returns a function
- always prints `"Hello, {name}"`

---

### 3. ✖️ Multiplier
Create `make_multiplier(x)`:
- returns a function
- multiplies input number by `x`

---

### 4. 🔒 Password Checker
Create `make_password_checker(password)`:
- returns a function
- checks if input matches stored password
- returns True/False

---

### 5. 📦 Last Value Storage
Create `make_last_value()`:
- stores last given value inside closure
- returns last value when called

---

## 🟡 Normal Level (Real Case Practice)

### 6. 📊 Logger with Level Filter
Create `create_logger(min_level)`:
- log levels: debug < info < warning < error
- prints message only if level >= min_level
- level is stored in closure

---

### 7. 💰 Discount System
Create `create_discount_system(customer_type)`:
- regular → 5%
- vip → 15%
- premium → 25%
- returns function that calculates final price

---

### 8. 📦 Shopping Cart
Create `create_cart()`:
- adds item prices
- keeps total inside closure
- returns current total

---

### 9. 🔁 API Cache Wrapper
Create `cache_api_request(func)`:
- caches results by arguments
- if same args used again → return cached result
- otherwise execute function and store result

---

### 10. 📈 Progress Tracker
Create `create_progress(total)`:
- stores total steps inside closure
- each call increases progress
- returns completion percentage

---