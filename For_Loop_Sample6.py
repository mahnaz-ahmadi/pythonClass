
students =  "mahnaz paniz mehrana farokh mohammad amin reza".split(' ')

for index, item in enumerate(students):
    if (index + 1) % 3 == 0:
       print(f"{item}")
