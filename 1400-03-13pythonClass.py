# def moarefi():
#     print("start function definition")
# moarefi()

# def moarefi():
#     print("salam")
#     a = 10
#     if a > 5:
#          print("ok!")
#     else:
#          print("not ok!")
# moarefi()

# def BMI():
#     height = float(input("ghad ra vared kon be cm: "))
#     weight = float(input("vazn ra vared kon be kg: "))
#     BMI = weight/height**2
#     print(f"your BMI is: {BMI}")
# BMI()

# def zarbdo():
#     adad = float(input("adad ra vared kon"))
#     print(f"javabe shoma : {adad*2}")
#
# zarbdo()

#
# def begu_salam(name):
#     print(f"{name}")
#
# begu_salam()
#
# def Age_Function(age):
#     print(f"your age is: {1400 - int(age)}")
# age = input("please enter you birth year:")
# Age_Function(age)
# age = input("please enter you birth year:")
# def Age_Function(age):
#     calculated = 1400 - int(age)
#     print(f"your age is: {calculated}")
# Age_Function(age)


# def mostatil_operation_namedParameter(tool, arz, dastoor):
#     if dastoor == "mohit":
#         mohit = (int(tool) + int(arz)) * 2
#         print("mohite mostatil = ", mohit)
#     elif dastoor == "masahat":
#         masahat = int(tool) * int(arz)
#         print("masahate mostatil = ", masahat)
#
#
# tool = input("tool ra vared konid: ")
# arz = input("arz ra vared konid: ")
# dastoor = input("dastoore mohit ya masahat ra vared konid: ")
# mostatil_operation_namedParameter(dastoor = dastoor, tool = tool, arz = arz)

def add_ba_yek(digit):

    return  digit + 1

digit = float(input("digit vared kon:"))
print(add_ba_yek(digit))
