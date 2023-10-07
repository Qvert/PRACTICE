"""
Practice 2 OP
"""


def calculate_function(list_all_coord: list) -> None:
    """
    :param list_all_coord: List all coordinates
    :return: None
    """
    list_coord_x, list_coord_y, list_coord_z = [], [], []
    for element in list_all_coord:
        list_coord_x.append(element[0])
        list_coord_y.append(element[1])
        list_coord_z.append(element[2])

    tuple_coord = (list_coord_x, list_coord_y, list_coord_z)
    tuple_math_ex = calculating_the_mathematical_expectation(tuple_coord)
    response_output(
        tuple_expectation=tuple_math_ex,
        tuple_variance=calculating_the_variance(
            tuple_coord=tuple_coord, tuple_math_expectation=tuple_math_ex
        ),
    )


def calculating_the_variance(
    tuple_math_expectation: tuple, tuple_coord: tuple
) -> tuple:
    """
    :param tuple_math_expectation: Tuple mathematical expectation
    :param tuple_coord: Tuple of lists the coordinates
    :return: Tuple variance
    """
    variance_x, variance_y, variance_z = (
        sum((x - tuple_math_expectation[0]) ** 2 for x in tuple_coord[0])
        / len(tuple_coord[0]),
        sum((y - tuple_math_expectation[1]) ** 2 for y in tuple_coord[1])
        / len(tuple_coord[1]),
        sum((z - tuple_math_expectation[2]) ** 2 for z in tuple_coord[2])
        / len(tuple_coord[2]),
    )
    return variance_x, variance_y, variance_z


def calculating_the_mathematical_expectation(tuple_coord: tuple) -> tuple:
    """
    :param tuple_coord: Tuple coordinates
    :return: Tuple mathematical expectation
    """
    expectation_math_x, expectation_math_y, expectation_math_z = (
        sum(tuple_coord[0]) / len(tuple_coord[0]),
        sum(tuple_coord[1]) / len(tuple_coord[1]),
        sum(tuple_coord[2]) / len(tuple_coord[2]),
    )
    return expectation_math_x, expectation_math_y, expectation_math_z


def response_output(tuple_expectation: tuple, tuple_variance: tuple) -> None:
    """
    :param tuple_expectation: Tuple of average values
    :param tuple_variance: Tuple of variances
    :return: None
    """
    list_axis = ["x", "y", "z"]
    dict_response = {
        "Estimation_of_mathematical_expectation": dict(zip(list_axis,
                                                           tuple_expectation)),
        "Estimation_of_variances": dict(zip(list_axis, tuple_variance)),
    }
    print(f'\n{dict_response}\n')


list_coordinates = []
while True:
    try:
        coordinates = tuple(
            map(int, input("Please enter the coordinates of the point"
                           " (x <= 20, y <= 30, z <= 10)").split())
        )
    except ValueError:
        print("You didn't enter a number")
        continue
    if len(coordinates) != 3:
        print("I'm sorry, but you didn't enter the coordinates completely")
        continue

    if coordinates[0] > 20 or coordinates[1] > 30 or coordinates[2] > 10:
        print(
            "Sorry, but the coordinates of "
            "the point go beyond the specified parameter"
        )
        continue

    list_coordinates.append(coordinates)
    FLAG = False

    while True:
        parameter = input(
            "Select the following action:\n"
            f"Your list of entered coordinates: {list_coordinates}\n"
            "1. Exit the program: 1\n"
            "2. Enter coordinates: 2\n"
            "3. Go to the calculations: 3\n"
            "4. Clearing the list of coordinates: 4\n"
            "5. Delete the last coordinates: 5\n"
        )
        if parameter == "1":
            FLAG = True
            break

        if parameter == "2":
            break

        if parameter == "3":
            calculate_function(list_coordinates)
            continue

        if parameter == "4":
            list_coordinates = []

        if parameter == "5":
            if len(list_coordinates) != 0:
                del list_coordinates[-1]
            else:
                print("")

        else:
            print("You have entered something else try again")
            continue

    if FLAG:
        break
