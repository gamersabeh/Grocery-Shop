store = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

cart = []
total = 0
item = input("What do you wanna buy: ").lower()

while item != "done":
    found = False
    for i in store:
        if item == i:
            found = True
    
    if found:
        cart.append(item)
    else:
        print("Sorry, item is not available.")
    
    item = input("What do you wanna buy: ").lower()

for i in cart:
    total += store[i]
    
print("Your total is:", total)
