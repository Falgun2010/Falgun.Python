while True:
    print("Welcome to the Bill Spiter App! \n")

    amount = float(input("Enter total bill amount:"))
    if  amount<0:
        print(" total amount must ve be possitive:")
        continue

    people = int(input("Enter number of people:"))
    if people<=0:
        print(" NUmber of people must be greater than 0.")
        continue
    tip_percentage = int(input("Enter tip percentage  (0 / 5 / 10 / 15 / 20): "))
    if tip_percentage not in [0 , 5 , 10 , 15 , 20]:
        print("tip must be one of 0 , 5 , 10 , 15 , 20.")
        continue
    

    tip = (tip_percentage/100)*amount
    total_amount = amount+tip
    Per_person = total_amount / people

    print(f"Tip amount: ₹",tip )
    print(f"Total Amount with tip: ₹",total_amount )
    print(f"Each person should pay: ₹",total_amount / people )

    print(input ("\n Would you like to calculater another bill ? ( y/n):"))
    print("...")
    
    

    