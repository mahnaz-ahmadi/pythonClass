start = 0
while start < 100:
    start += 1
    if (start % 2 == 0 and start % 3 == 0) or start % 2 == 0 or start % 4 == 0 or start % 9 == 0:
        print(f" **{start}** bahale!")

    else:
        continue
