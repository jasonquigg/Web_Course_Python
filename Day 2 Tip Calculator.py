# Prints a welcome statement
print("Welcome to the tip calculator!")
# Gets input from user for the cost of the entire bill
total_bill = float(input("What was the total bill? "))
# Gets input from the user for how much they want to tip
tip = float(input("How much of a tip would you like to give? 0, 10, 12, 15 or 20? "))
# Gets input from the user for how many people are splitting the bill
num_people = int(input("How many people would you like to split the bill with? "))
# Math to get the answer to how much percentage the tip is = too
percent = (total_bill * tip) / 100
# calculates the total amount to pay for each person
amount_to_pay = (total_bill + percent) / num_people
print(f"Each person pays {amount_to_pay:.2f}")
