def main():
    dollars = input("How much was the meal? ")
    dollars = dollars_to_float(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
   # print(f"Leave ${tip:.2f}")
    tip = round(tip,2)
    print("$",tip,sep="")

# $14.15 
def dollars_to_float(d):
    d = d.replace("$","")
    d = float(d)
    return d

def percent_to_float(p):
    p = p.replace("%","")
    p = float(p)
    p = p/100
    


    return p

main()