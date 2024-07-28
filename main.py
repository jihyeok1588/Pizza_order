print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N: ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size == "S":
    first_bill = 15
    if add_pepperoni == "Y":
        second_bill = first_bill + 2
        if extra_cheese == "Y":
            final_bill = second_bill + 1
        elif extra_cheese == "N":
            first_bill = second_bill
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            final_bill = first_bill + 1
        elif extra_cheese == "N":
            final_bill = first_bill

if size == "M":
    first_bill = 20
    if add_pepperoni == "Y":
        second_bill = first_bill + 3
        if extra_cheese == "Y":
            final_bill = second_bill + 1
        elif extra_cheese == "N":
            first_bill = second_bill
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            final_bill = first_bill + 1
        elif extra_cheese == "N":
            final_bill = first_bill

if size == "L":
    first_bill = 25
    if add_pepperoni == "Y":
        second_bill = first_bill + 3
        if extra_cheese == "Y":
            final_bill = second_bill + 1
        elif extra_cheese == "N":
            first_bill = second_bill
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            final_bill = first_bill + 1
        elif extra_cheese == "N":
            final_bill = first_bill

print(f"your total bill: ${final_bill}")