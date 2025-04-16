print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? %"))
people = int(input("How many people to split the bill? "))

tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
