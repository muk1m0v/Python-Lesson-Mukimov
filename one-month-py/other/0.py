def price(products, name):
    if name in products:
        return products[name]
    else:
        return "Not Found"

products = {
    "Laptop": 8000,
    "Mouse": 150
}

print(price(products, "Laptop"))