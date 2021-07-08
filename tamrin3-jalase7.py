
number = int(input('please enter your number: '))
factorial = number
pointer = number

if number > 1:
    while pointer > 1:
        factorial *=  pointer - 1
        pointer -= 1

if factorial == 0:
    factorial = 1

print(f'{number}! = ', factorial)
