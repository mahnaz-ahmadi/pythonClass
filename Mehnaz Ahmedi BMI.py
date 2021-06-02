print("Let's Calculate Your BMI")
W=float(input("Please Enter Your Weight (kg)"))
H=float(input("Now Please Enter Your Height (m)"))
BMI=int((W/H**2))
if 15<BMI<25:
    print(f"Here is your BMI score: {BMI} \nYou're great")
elif BMI>25:
    print(f"Here is your BMI score: {BMI} \nOH MY GOD! Slow Down! Have Mercy for yourself")
elif BMI<15:
    print(f"Here is your BMI score: {BMI} \nEat Something immediately")
