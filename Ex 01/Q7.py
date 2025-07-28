# 7. Currency Conversion Calculator
# •	Accept values of different foreign currencies (USD, EUR, JPY) and 
# their respective conversion rates to INR. Calculate the total amount 
# in INR using arithmetic and assignment operators.

usd = float(input("Enter amount in USD: "))
eur = float(input("Enter amount in EUR: "))
jpy = float(input("Enter amount in JPY: "))

usd_to_inr = float(input("Enter conversion rate of 1 USD to INR: "))
eur_to_inr = float(input("Enter conversion rate of 1 EUR to INR: "))
jpy_to_inr = float(input("Enter conversion rate of 1 JPY to INR: "))

total_inr = 0

total_inr += usd * usd_to_inr
total_inr += eur * eur_to_inr
total_inr += jpy * jpy_to_inr

print("Total Amount in INR: ", total_inr)
