def Mohite_Mostatil(tool, arz):
    try:
        mohit = (int(tool) + int(arz)) * 2
        print("mohite mostatil = ", mohit)
    except:
        print("an exception occured!")

tool = input("tool ra vared konid:")
arz = input("arz ra vared konid:")
Mohite_Mostatil(tool, arz)
