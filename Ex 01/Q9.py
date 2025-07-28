# 9.Net Salary Deduction
# •	Given an employee's gross salary, calculate deductions (PF, tax, etc.) 
# based on percentages, and use assignment operators to update net salary 
# after each deduction stage.

gross_salary = float(input("Enter Gross Salary: ₹"))
pf_percent = float(input("Enter PF deduction percentage: "))
tax_percent = float(input("Enter Tax deduction percentage: "))

net_salary = gross_salary

net_salary -= (pf_percent / 100) * gross_salary

net_salary -= (tax_percent / 100) * gross_salary

print("\nNet Salary after deductions: ₹", round(net_salary, 2))
