"""
Practice 2 OP
"""

list_coordinates = list()
while True:
    coordinates = tuple(map(int, input('Please enter the coordinates of the point ').split()))
    print(coordinates)
    if len(list_coordinates) != 3:
        print("I'm sorry, but you didn't enter the coordinates completely")
    for elem in list_coordinates:
        if 0 >= elem >= 20:
            print("Sorry, but the coordinates of the point go beyond the specified parameter")
            break
    parametr = input("Вы хотите продолжить ввод координат? (Y/N)")

    list_coordinates.append(coordinates)

