
def select_shape():

    welcome_message = """hi, this is your shapes math operations assistant
    please select one of this shape types:
    for select please input number of shape or shape name!!!
    1.circle
    2.foursquare
    3.rectangle
    4.triangle
    """

    print(welcome_message)
    selected_shape = input("enter your shape : ")

    if selected_shape == "1" or selected_shape == "circle":
       selected_shape = "circle"
    elif selected_shape == "2" or selected_shape == "foursquare":
       selected_shape = "foursquare"
    elif selected_shape == "3" or selected_shape == "rectangle":
       selected_shape = "rectangle"
    elif selected_shape == "4" or selected_shape == "triangle":
       selected_shape = "triangle"
    else:
       print("invalid shape. please try again")
       select_shape()

    print(f"your selected shape is : {selected_shape}")

    return selected_shape


def select_operation():
    message = """select your operation:
    for select please input number of operation or name!!!
    1.circumference
    2.area
    """

    print(message)
    selected_operation = input("enter your operation : ")

    if selected_operation == "1" or selected_operation == "circumference" :
        selected_operation = "circumference"
    elif selected_operation == "2" or selected_operation == "area":
        selected_operation = "area"
    else:
        print("invalid operation. please try again")
        select_operation()

    print(f"your selected operation is : {selected_operation}")

    return selected_operation

def get_operation_parameters(selected_shape, selected_operation):
    radius = 0
    longitude = 0
    latitude = 0
    altitude = 0
    base = 0
    side1 = 0
    side2 = 0
    side3 = 0
    if selected_shape == "circle":
        radius = float(input("enter radius : "))
    elif selected_shape == "foursquare":
        longitude = float(input("enter side : "))
    elif selected_shape == "rectangle":
        longitude = float(input("enter longitude : "))
        latitude = float(input("enter latitude : "))
    elif selected_shape == "triangle":
        if selected_operation == "area":
            altitude = float(input("enter altitude : "))
            base = float(input("enter base : "))
        else:
            side1 = float(input("enter side 1 : "))
            side2 = float(input("enter side 2 : "))
            side3 = float(input("enter side 3 : "))

    return radius, longitude, latitude, altitude, base, side1, side2, side3

def calculate_shape_operation(selected_shape,
  selected_operation,
  radius,
  longitude,
  latitude,
  altitude,
  base,
  side1,
  side2,
  side3
):
   if selected_shape == "circle":
       if selected_operation == "area":
           result = 3.14 * (radius ** 2)
       else:
           result = 3.14 * radius * 2
   elif selected_shape == "foursquare":
       if selected_operation == "area":
           result = longitude ** 2
       else:
           result = longitude * 4
   elif selected_shape == "rectangle":
       if selected_operation == "area":
           result = longitude * latitude
       else:
           result = (longitude + latitude) * 2
   elif selected_shape == "triangle":
       if selected_operation == "area":
           result = (altitude * base) / 2
       else:
           result = side1 + side2 + side3

   print(f"{selected_operation} of {selected_shape} is : {result}")



def main():
    selected_shape = select_shape()
    selected_operation = select_operation()
    radius, longitude, latitude, altitude, base, side1, side2, side3 = get_operation_parameters(selected_shape = selected_shape, selected_operation = selected_operation)
    calculate_shape_operation(selected_shape = selected_shape,
    selected_operation = selected_operation,
    radius = radius,
    longitude = longitude,
    latitude = latitude,
    altitude = altitude,
    base = base,
    side1 = side1,
    side2 = side2,
    side3 = side3
    )

main()
