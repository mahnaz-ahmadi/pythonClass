what_shape = input("what shape are you need ?\nchoice one of this shapes :\
\nRectangle\nSquare\nTriangle\nCircle\nTrapezius\nParallelogram\n*")
what_calculate = input("What to calculate?\nchoice one of this opr :\
\nArea\nEnvironment\n*")

def student_assistant(what_shape, what_calculat):
    if what_shape == "Triangle" and what_calculate == "Area":
        rule = float(input("plz enter rule value : "))
        height = float(input("plz enter height value : "))
        #print(f"Arae is = {rule * height / 2}")
        Area = rule * height / 2
        return Area
    if what_shape == "Triangle" and what_calculate == "Environment":
        edge_one = float(input("plz enter edge_one value : "))
        edge_two = float(input("plz enter edge_two value : "))
        edge_three = float(input("plz enter edge_three value : "))
        #print(f"Environment is = {edge_one + edge_two + edge_three}")
        Environment = edge_one + edge_two + edge_three
        return Environment
    if what_shape == "Circle" and what_calculate == "Area":
        redios = float(input("plz enter redios value : "))
        #print(f"Arae is = {redios **2 * 3.14}")
        Area = redios **2 * 3.14
        return Area
    if what_shape == "Circle" and what_calculate == "Environment":
        redios = float(input("plz enter redios value : "))
        #print(f"Environment is = {redios * 2 * 3.14}")
        Environment = redios * 2 * 3.14
        return Environment


print(student_assistant(what_shape, what_calculate))
