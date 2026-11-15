# Create a list of five item names. Add one, remove one, then print each item with
# its number using a for loop.


items = ["pen", "book", "ruler", "bag", "eraser"]
print("Original list:", items)


# Add one item to the end of the list
items.append("marker")
print("After adding:", items)


# Remove one item by its name
items.remove("ruler")
print("After removing:", items)

# Print each item with its number, starting from 1
print ("""Final items:""")
for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")