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
            
    if found == 1:
        Q = input("choose how many: ").strip()
        if Q.isdigit():
            quantity = int(Q)
        else:
            print("Invalid quantity, using 1 instead.")
            quantity = 1

        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

        total += Groceries[item] * quantity
    else:
        print("Invalid Item.")

    item = input("What do you want to buy? ").strip().lower()

print("You bought: ", cart)
