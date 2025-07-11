#monthly income
monthly_income =int(input("Enter your monthly income:"))

# expenses
monthly_expenses = int(input("Enter your total monthly expenses:"))

#calculate savings
monthly_savings = monthly_income - monthly_expenses

#project annual savings
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}")

print(f"Projected savings after one year, with interest is: ${projected_savings}")