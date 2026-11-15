# Task 3: Inventory of four items, print only Low stock or Out of stock

def stock_status(quantity):
    """Return the stock level for a given quantity."""
    if quantity == 0:
        return "Out of stock"
    elif quantity < 5:
        return "Low stock"
    else:
        return "In stock"


inventory = [
    {"name": "Laptop", "quantity": 0},
    {"name": "Mouse", "quantity": 3},
    {"name": "Keyboard", "quantity": 12},
    {"name": "Monitor", "quantity": 2},
]

print("Items that need restocking:")
for item in inventory:
    status = stock_status(item["quantity"])
    if status in ("Low stock", "Out of stock"):
        print(f"{item['name']} ({item['quantity']}) - {status}")