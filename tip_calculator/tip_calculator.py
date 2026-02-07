"""
Project: Tip Calculator
Description: Calculates how much each person should pay when splitting
a bill, including a chosen tip percentage.
"""

print("💰 Welcome to the Tip Calculator!")

# Get user inputs
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? (10, 12, 15): "))
people = int(input("How many people to split the bill? "))

# Calculate total bill including tip
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount

# Calculate amount per person
bill_per_person = total_bill / people

# Round to 2 decimal places for currency
final_amount = round(bill_per_person, 2)

# Display result
print(f"\nEach person should pay: ${final_amount}")

