"""
Provides some arithmetic functions
"""
import argparse
import math


def calculate_formula(number: int) -> float:
    """
    :param number: Input value
    :return: Output value
    """
    answer = (
        (math.tan(number) / math.sqrt(2 * number))
        + 2 * ((2 * number) / math.sqrt(math.log(number**9)))
        + (math.sin(number) / math.sqrt(math.cos(number**9)))
    )
    return answer


parser = argparse.ArgumentParser(
    prog="Counting script",
    description="This program reads the"
    " value and outputs the calculated value from the formula",
)
parser.add_argument(
    "-c",
    "--count",
    type=int,
    help="Enter a number to get the result from the formula",
)

count_value = parser.parse_args().count

try:
    answer_number = calculate_formula(count_value)
    print(f"Your answer is: {answer_number}")
except ValueError:
    print("With this number, the formula cannot be calculated")
except ZeroDivisionError:
    print("With this number in the formula, division by zero occurs")
