print("This is a Smart Calculator")
print("Select operation.")
print("1=+")
print("2=-")
print("3=*")
print("4=/")
selection=input()
# if selection > 4:
#     print("fuck you")
num1=float(input("Enter the First number"))
num2=float(input("Enter the Second number"))
if selection == '1':
    print(num1, "+", num2, "=", num1+num2)
elif selection == '2':
            print(num1, "-", num2, "=", num1-num2)
elif selection == '3':
            print(num1, "*", num2, "=", num1*num2)
elif selection == '4':
            print(num1, "/", num2, "=", num1/num2)
#    else:
#            print("Invalid Input")
