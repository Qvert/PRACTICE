"""
Practice 2 OP
"""

list_coordinates = []
while True:
    coordinates = tuple(
        map(int, input("Please enter the coordinates of the point ").split())
    )
    print(coordinates)
    if len(coordinates) != 3:
        print("I'm sorry, but you didn't enter the coordinates completely")
        break

    for elem in list_coordinates:
        for elem_inside in elem:
            if 0 >= elem_inside >= 20:
                print(
                    "Sorry, but the coordinates of the point go beyond the specified parameter"
                )
                break

    list_coordinates.append(coordinates)
    parameter = input("Do you want to continue entering coordinates? (Y/N)")

    if parameter == "N":
        break
    if parameter == "Y":
        continue

print(list_coordinates)
