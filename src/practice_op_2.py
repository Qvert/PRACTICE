"""
Practice 2 OP
"""


def calculate_function(list_coord: list) -> None:
    pass


list_coordinates = []
while True:
    coordinates = tuple(
        map(int, input("Please enter the coordinates of the point ").split())
    )

    if len(coordinates) != 3:
        print("I'm sorry, but you didn't enter the coordinates completely")
        continue

    for elem in list_coordinates:
        for elem_inside in elem:
            if 0 >= elem_inside >= 20:
                print(
                    "Sorry, but the coordinates of the point go beyond the specified parameter"
                )
    list_coordinates.append(coordinates)
    parameter = input("Select the following action:\n"
                      "1. Exit the program: 1\n"
                      "2. Continue entering coordinates: 2\n"
                      "3. Go to the calculations: 3\n")
    FLAG = False

    while True:
        if parameter == '1':
            FLAG = True
            break
        if parameter == '2':
            break
        if parameter == '3':
            calculate_function(list_coordinates)

    if FLAG:
        break


