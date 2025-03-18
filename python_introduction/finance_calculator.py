# Financial Details and Savings Projection

# User Input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
annual_interest_rate = 0.05  # 5%
annual_savings_before_interest = monthly_savings * 12
projected_annual_savings = annual_savings_before_interest + (annual_savings_before_interest * annual_interest_rate)

# Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")