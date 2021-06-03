def BMI():
   weight = input("please enter your weight: (kg):")
   height = input("please enter your height: (m):")
   numeric_weight = float(weight)
   numeric_height = float(height)
   print(f"your BMI with weight:{weight} kg and height:{height} is: {numeric_weight/numeric_height**2}")


BMI()
