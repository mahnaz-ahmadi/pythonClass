numeric_list = [8,4,6,7,9,1,1,3,6,9,15,128,32,78,0]

def sort(list, sort_type):
    temp = 0
    repeat = False
    pointer = 1

    print("Origininal list", numeric_list)

    while pointer < len(list):
        for index, value in enumerate(numeric_list):
            if sort_type == "ASC":
               if (index + 1) != len(numeric_list) and value > list[index + 1]:
                  temp = value
                  list[index] = list[index + 1]
                  list[index + 1] = temp
               else:
                  continue
            elif sort_type == "DESC":
               if (index + 1) != len(numeric_list) and value < list[index + 1]:
                  temp = value
                  list[index] = list[index + 1]
                  list[index + 1] = temp
               else:
                  continue
        pointer += 1

    print("Sorted list", numeric_list)


sort(numeric_list, "ASC")
