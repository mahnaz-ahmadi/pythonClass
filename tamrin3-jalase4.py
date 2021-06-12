user_number = int(input("Plz enter your number between 1 and 10:\n"))
print(f"your number :{user_number}")
number = 0
while number <= 1000:
    number += 1
    result = number % user_number
    if result == 0:
        print(f"{number} is divisible {user_number}")
    else:
        continue
