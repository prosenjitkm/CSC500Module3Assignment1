
# declaring the constants
tip_rate = 0.18
sales_tax_rate = 0.07

# initialiazing the variables
tip_amount = 0
sales_tax_amount = 0
total_price = 0
prompt_message = "Enter the charge for the food: "

# asking the user for input
food_charge = float(input(prompt_message))

# calculations
tip_amount = food_charge * tip_rate
sales_tax_amount = food_charge * sales_tax_rate
total_price = food_charge + tip_amount + sales_tax_amount

print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip Amount (18%): ${tip_amount:.2f}")
print(f"Sales Tax (7%): ${sales_tax_amount:.2f}")
print(f"Total Price: ${total_price:.2f}")