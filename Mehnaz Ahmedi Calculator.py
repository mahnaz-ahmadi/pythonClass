print("This is a Smart Calculator")
num1 = float(input("Enter the First number:"))
print("Select operation!")
print("+")
print("-")
print("*")
print("/")
selection = input()
if  selection != '+' and selection !='-'  and selection !='/' and selection !='*' :
    print("invalid input!")
    print("Now Select valid operation:")
    print("+")
    print("-")
    print("*")
    print("/")
    selection = input()
num2 = float(input("Enter the Second number:"))
if selection == '+':
    print(num1, "+", num2, "=", num1+num2)
elif selection == '-':
    print(num1, "-", num2, "=", num1-num2)
elif selection == '*':
    print(num1, "*", num2, "=", num1*num2)
elif selection == '/':
    if num2 != 0:
            print(num1, "/", num2, "=", num1/num2)
    else:
            print("invalid division!")
