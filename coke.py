amount = 0 
while amount < 50:
    coins = input("Insert a coin ")
    if coins == "5" or coins == "10" or coins == "25":
        amount += int(coins)
        print("Total:", amount)
    else:
        print("Insert a valid coin")
if amount >= 50:
    change = amount - 50 
    print("Total change = ", change , " cents")
        
