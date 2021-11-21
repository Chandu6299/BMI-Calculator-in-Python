h=float(input("Enter your height in m: "))
w=float(input("Enter your weight in kg: "))
B= w/h**2
print(f"Your BMI is {round(B,2)}")
if B<18.5:
  print("You are underweight")
elif B<25:
  print("You have normal weight")
elif B<30:
  print("You are overweight")
elif B<35:
  print("You are obese")
else:
  print("You are clinically obese")
