
point = (0,5)

match point:
    case (0 , 0):
        print("Origin")
    case (0 , y):
        print("Y-axis")
    case(x , 0):
        print(x-axis)
    case _:
        print("Sowhere Else")

