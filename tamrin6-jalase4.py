length =int(input("How long is this list? "))
user_list = []
print(f"plz enter {len} number")
while length > 0:
    number = int(input("enter number: "))
    user_list.append(number)
    length -= 1
input_list =print('original_list : ', user_list)

counter = 0
unique_user_list = []
while counter < len(user_list):
    if user_list[counter] not in unique_user_list:
       unique_user_list.append(user_list[counter])
    counter += 1
print('unique_list : ',  unique_user_list)
