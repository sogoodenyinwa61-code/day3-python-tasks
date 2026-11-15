# Task 2: Get product details from the user, store in a dictionary, print with .items()

name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))    # convert text to a whole number
price = float(input("Enter price: "))    

product = {
    "name": name,
    "quantity": quantity,
    "price": price,
}

# Print every key and value
print("\nProduct details:")
for key, value in product.items():
    print(f"{key}: {value}")