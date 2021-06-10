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
def addition(num1, num2):
    if selection == '+':
            result = num1 + num2
            return result

def subtraction(num1, num2):
    if selection == '-':
            result = num1 - num2
            return result

def multiplication(num1, num2):
    if selection == '*':
            result = num1 * num2
            return result

def division(num1, num2):
    if selection == '/' and num2 != 0:
            result = num1 / num2
            return result
    else:
            print("invalid division!")
if selection == "+":
    print(addition(num1, num2))
elif selection == "-":
    print(subtraction(num1, num2))
elif selection == "*":
    print(multiplication(num1, num2))
elif selection == "/":
    print(division(num1, num2))
