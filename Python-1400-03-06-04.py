number = input("enter your number")
number_int = int(number)
if number_int % 3 == 0 and number_int % 2 == 0:
    print("your number mod 6 == 0")
else:
    print("your number mod 6 != 0")
