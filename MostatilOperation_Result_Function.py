def mostatil_operation(tool, arz, dastoor):
    result = 0;
    if dastoor == "mohit":
        mohit = (int(tool) + int(arz)) * 2
        result = mohit
    elif dastoor == "masahat":
        masahat = int(tool) * int(arz)
        result = masahat

    return result


tool = input("tool ra vared konid: ")
arz = input("arz ra vared konid: ")
dastoor = input("dastoore mohit ya masahat ra vared konid: ")
print(f"{dastoor} : ", mostatil_operation(tool, arz, dastoor))
