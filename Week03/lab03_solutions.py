# Lab 03 Solutions: Python Collections Practice
# Covers: Lists, Tuples, Sets, Dictionaries

# ============================================================
# Question 1: Student Grades List (Lists - Basic Operations)
# ============================================================
print("=" * 50)
print("Question 1: Student Grades List")
print("=" * 50)

# 1. Create a list with initial grades
grades = [85, 92, 78, 95, 88]

# 2. Append a new grade
grades.append(90)

# 3. Sort the grades in ascending order
grades.sort()

# 4. Print the sorted list
print("Sorted grades:", grades)

# 5. Print highest grade (last element using negative indexing)
print("Highest grade:", grades[-1])

# 6. Print lowest grade (first element)
print("Lowest grade:", grades[0])

# 7. Print total number of grades
print("Total number of grades:", len(grades))

print()

# ============================================================
# Question 2: Shopping Cart (Lists - Searching and Removal)
# ============================================================
print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)

# 1. Create a shopping cart list
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

# 2. Count how many times "apple" appears
apple_count = cart.count("apple")
print("Number of apples:", apple_count)

# 3. Find position of "milk"
milk_position = cart.index("milk")
print("Position of milk:", milk_position)

# 4. Remove one "apple" from the cart
cart.remove("apple")

# 5. Pop the last item
removed_item = cart.pop()
print("Removed item using pop:", removed_item)

# 6. Check if "banana" is in the cart
print("Is banana in cart?", "banana" in cart)

# 7. Print the final cart
print("Final cart:", cart)

print()

# ============================================================
# Question 3: Coordinate System (Tuples)
# ============================================================
print("=" * 50)
print("Question 3: Coordinate System")
print("=" * 50)

# 1. Create tuple point1
point1 = (3, 5)
print("Point 1:", point1)

# 2. Create tuple point2
point2 = (7, 2)
print("Point 2:", point2)

# 3. Unpack point1
x1, y1 = point1
print("x1 =", x1, ", y1 =", y1)

# 4. Unpack point2
x2, y2 = point2
print("x2 =", x2, ", y2 =", y2)

# 5. Calculate distance
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between points:", distance)

# 6. Create tuple from string
char_tuple = tuple("PYTHON")
print("Characters tuple:", char_tuple)

# 7. Print each character using for loop
for char in char_tuple:
    print(char)

print()

# ============================================================
# Question 4: Class Attendance (Sets)
# ============================================================
print("=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)

# 1. Create Monday class set
monday_class = {"Alice", "Bob", "Charlie", "Diana"}

# 2. Create Wednesday class set
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

# 3. Add Grace to Monday class
monday_class.add("Grace")

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

# 4. Intersection - students who attended both classes
both_classes = monday_class & wednesday_class
print("Attended both classes:", both_classes)

# 5. Union - students who attended either class
all_students = monday_class | wednesday_class
print("Attended either class:", all_students)

# 6. Difference - students who attended only Monday
only_monday = monday_class - wednesday_class
print("Only Monday:", only_monday)

# 7. Symmetric difference - students who attended only one class
only_one = monday_class ^ wednesday_class
print("Only one class (not both):", only_one)

# 8. Check if Monday is subset of all students
print("Is Monday subset of all students?", monday_class <= all_students)

print()

# ============================================================
# Question 5: Contact Book (Dictionaries)
# ============================================================
print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)

# 1. Create contacts dictionary
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# 2. Print Alice's phone number
print("Alice's number:", contacts["Alice"])

# 3. Add Diana
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

# 4. Update Bob's number
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

# 5. Delete Charlie
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

# 6. Print all names using keys()
print("All names:", contacts.keys())

# 7. Print all numbers using values()
print("All numbers:", contacts.values())

# 8. Print total number of contacts
print("Total contacts:", len(contacts))

print()

# ============================================================
# Question 6: Inventory Management System (Combined)
# ============================================================
print("=" * 50)
print("Question 6: Inventory Management System")
print("=" * 50)

# 1. Create inventory dictionary with tuples as values
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

# 2. Print inventory using for loop with items()
print("=== Current Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))

print()

# 3. Create category sets
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

# 4. Find all products using union
all_products = electronics | accessories
print("All product categories:", all_products)

print()

# 5. Create list of all prices
prices = []
for product in inventory:
    price = inventory[product][0]
    prices.append(price)
print("Price list:", prices)

# 6. Sort prices and print lowest/highest
prices.sort()
print("Sorted prices:", prices)
print("Lowest price: $" + str(prices[0]))
print("Highest price: $" + str(prices[-1]))

print()

# 7. Add new product
inventory["Headphones"] = (49.99, 20)

# 8. Update Mouse quantity (keep same price)
mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

# 9. Remove Monitor
del inventory["Monitor"]

# 10. Print final inventory
print("=== Final Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))
