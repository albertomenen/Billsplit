money = float(input( "How much money is the bill"))
people = int(input ("How many people are you?"))

tip = int(input("how much tip do you want to give?"))

tip_as_percent = tip/100

total_tip = tip_as_percent * money

total_bill = money + total_tip

total_divided = total_bill//people

final_amount = round (total_divided, 2)

print(f"Tienes quendar {total_divided}")
