def Mohite_Mostatil(tool, arz, dastoor):
    if dastoor == "mohit":
        mohit = (int(tool) + int(arz)) * 2
        print("mohite mostatil = ", mohit)
    elif dastoor == "masahat":
        masahat = int(tool) * int(arz)
        print("masahate mostatil = ", masahat)


tool = input("tool ra vared konid: ")
arz = input("arz ra vared konid: ")
dastoor = input("dastoore mohit ya masahat ra vared konid: ")
Mohite_Mostatil(tool, arz, dastoor)
