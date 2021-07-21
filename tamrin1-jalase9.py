
number_list = [1,2,4,6,2,8,5,9,8,1,4,9,10,7,14,2,10,3,3,1,4,7]
number_count_list = []
counter = 1
pointer = 1

number_list = sorted(number_list)
for i, number in enumerate(number_list):
    if pointer < counter:
        pointer += 1
        continue
    else:
        pointer = 1
        counter = 1
    while i < len(number_list) - 1 and number_list[i + 1] == number:
        counter += 1
        i += 1
    number_count_list.append({'number':number, 'count': counter})
print(number_count_list)
