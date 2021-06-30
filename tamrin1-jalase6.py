person_list = ["mahnaz", "maryam", "maryam", "senobar", "malihe", "maryam", "maryam"]
print(f"original list is : {person_list}")

duplicate_index_list = []
for index, value in enumerate(person_list):
    if index != person_list.index(value):
        duplicate_index_list.append(index);

duplicate_index_list = sorted(duplicate_index_list, reverse=True)

for duplicate_index in duplicate_index_list:
    del person_list[duplicate_index]
print(f"unique list after del command is : {person_list}")
