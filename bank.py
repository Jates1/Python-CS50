def bank():
    x = input("Greetings ").casefold()
    if x.startswith("hello"):
        return 0
    elif x.startswith("h"):
        return 20
    else:
        return 100

#bank() 
amount = 0
for i in range(5):
    amount += bank()
    print("$", amount)





#In a file called bank.py, implement a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” 
# (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace 
# in the user’s greeting, and treat the user’s greeting case-insensitively.