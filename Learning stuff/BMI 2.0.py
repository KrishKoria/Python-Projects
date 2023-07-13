height = float(input("Enter your height in metres :- "))
weight = float(input("Enter your weight in Kg :- "))

bmi = round(weight / (height * height))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are Under Weight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you are Normal Weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are Over Weight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are Obese")
else:
    print("You are almost dead")
