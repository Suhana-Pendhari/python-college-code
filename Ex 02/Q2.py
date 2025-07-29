# Q2) BMI Calculator:
# Create a BMI (Body Mass Index) calculator that takes user inputs 
# for height and weight, computes the BMI, and categorizes the result 
# into underweight, normal weight, overweight, or obese categories.

print("------BMI Calculator-------")
w = float(input("Enter Weight in KG: "))
h = float(input("Enter height in CM: "))
h = h/100
bmi = w/(h**2)

print("BMI is: ", bmi)

if(bmi < 18.5):
    print("Underweight")
elif(18.5 <= bmi and bmi < 30):
    print("Normal weight")
elif(25 <= bmi and bmi < 30):
    print("Overweight")
else:
    print("Obese")
print("----------------------------")
