list1 = ["mahnaz", "paniz", "anahita"]
list2 = ["ahmadi", "sedaghat", "zolghadr"]

target_list = []
for index1, item1 in enumerate(list1):
    target_list.append(item1)
    target_list.append(list2[index1])

print(target_list)
