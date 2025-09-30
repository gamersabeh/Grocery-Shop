Groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2,
}

item = input("What do you want to buy? ").strip().lower()
total = 0
cart = {}

while item != "done":
    found = 0
    for i in Groceries:
        if item == i:
            found = 1
