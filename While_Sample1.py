number = 1
while number <= 50:
    result = number
    if number % 3 == 0:
       result = f"{result} bar 3 bakhshpazir ast"
    else:
       result = f"{number}"
    print(result)
    number += 1
