# 8.Electricity Bill Splitter
# •	Given the monthly electricity bill and unit usage by 3 different tenants, 
# proportionally calculate each person's share based on their consumption using 
# division, multiplication, and assignment operators.


total_bill = float(input("Enter total electricity bill amount: "))
unit1 = float(input("Enter units used by Tenant 1: "))
unit2 = float(input("Enter units used by Tenant 2: "))
unit3 = float(input("Enter units used by Tenant 3: "))

total_units = unit1 + unit2 + unit3

share1 = share2 = share3 = 0

share1 += (unit1 / total_units) * total_bill
share2 += (unit2 / total_units) * total_bill
share3 += (unit3 / total_units) * total_bill

print("\n--- Electricity Bill Split ---")
print("Tenant 1 pays: ₹", round(share1, 2))
print("Tenant 2 pays: ₹", round(share2, 2))
print("Tenant 3 pays: ₹", round(share3, 2))
