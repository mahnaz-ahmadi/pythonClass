number = 0
print(f"{number}")
while number <= 100:
    command = input(f"up or down or stop? : ")
    if command == "up":
       number += 1
       print(f"{number}")
    elif command == "down":
       number -= 1
       print(f"{number}")
    elif command == "stop":
       break

print("end of loop")
