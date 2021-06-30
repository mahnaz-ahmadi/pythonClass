
def recursive_sum(list, index, sum):
   if index == len(list):
       print(f"sum of list members is : {sum}")
   else:
       sum = list[index] + sum
       recursive_sum(list, index + 1, sum)

def main():
   list = [1, 2, 8, 16, 32, 64]
   index = 0
   sum = 0
   recursive_sum(list, index, sum)

main()
