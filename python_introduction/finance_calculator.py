monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly saving are {monthly_savings}.")
print(f"Your personal annual savings after including 5% interest is: {projected_savings:}.")