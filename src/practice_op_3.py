# pylint: disable=global-variable-not-assigned
# pylint: disable=global-statement

"""Practice 3 OP"""
from collections import Counter


LS_HAF = []
TEXT_INPUT = ""
CODE_STRING = ""


def recursion_make_code_symbol(string: str, element: str) -> None:
    """
    :param string: String code symbol
    :param element: Element iteration
    :return: None
    """
    global LS_HAF
    if isinstance(element, str):
        LS_HAF.append((element, string))
        return
    recursion_make_code_symbol(string + "0", element[0])
    recursion_make_code_symbol(string + "1", element[1])
    return


def make_tree_huffman_code(input_str: str) -> str:
    """
    :param input_str: Input stroke
    :return: Tuple tree huffman code
    """
    list_probabilities_ch = list(sorted(Counter(input_str).items(),
                                        key=lambda x: x[1]))

    while len(list_probabilities_ch) >= 2:
        sum_symbol = (
            (list_probabilities_ch[0][0], list_probabilities_ch[1][0]),
            list_probabilities_ch[0][1] + list_probabilities_ch[1][1],
        )
        if list_probabilities_ch[-1][1] < sum_symbol[1]:
            list_probabilities_ch.append(sum_symbol)
        else:
            for num in range(2, len(list_probabilities_ch)):
                if list_probabilities_ch[num][1] >= sum_symbol[1]:
                    list_probabilities_ch.insert(num, sum_symbol)
                    break
        list_probabilities_ch.pop(0)
        list_probabilities_ch.pop(0)
    return list_probabilities_ch[0][0]


def make_dict_huffman(text: str) -> dict:
    """
    :param text: Input string
    :return: Dict with symbols code
    """
    global LS_HAF
    list_probabilities_ch = make_tree_huffman_code(text)
    LS_HAF = []
    recursion_make_code_symbol("", list_probabilities_ch)
    return dict(LS_HAF)


def compress_code_huffman(text: str, dc_haf: dict) -> str:
    """
    :param text: Input string
    :param dc_haf: Dict with symbols code
    :return: Compressing string
    """
    str_result = ""
    for element in text:
        str_result = str_result + dc_haf[element]
    return str_result


def decompress_code_huffman(text: str, dc_haf: dict) -> str:
    """
    :param text: The string to be decoded
    :param dc_haf: Symbol code dictionary
    :return: Decode string
    """
    dc_decode = {dc_haf[key]: key for key in dc_haf}
    st_res = ""
    while len(text) > 0:
        num = 1
        while text[:num] not in dc_decode:
            num += 1
        st_res += dc_decode[text[:num]]
        text = text[num:]
    return st_res


def main() -> None:
    """Main function"""
    global TEXT_INPUT, CODE_STRING
    while True:
        parameter = input(
            "Select the following action:\n"
            "1. Enter the string: 1\n"
            "2. Encode the string using the Huffman method: 2\n"
            "3. Decode a string using the Huffman method: 3\n"
            "4. Exit the program: 4\n"
        )
        try:
            match parameter:
                case "1":
                    TEXT_INPUT = input(
                        "Please enter"
                        " the string you want to encode: "
                    )

                case "2":
                    CODE_STRING = compress_code_huffman(
                        TEXT_INPUT, make_dict_huffman(TEXT_INPUT)
                    )
                    print(f"Your coded string: {CODE_STRING}\n")
                case "3":
                    result_decoding = decompress_code_huffman(
                        CODE_STRING, make_dict_huffman(TEXT_INPUT)
                    )
                    print(f"Your decoded string: {result_decoding}\n")
                case "4":
                    break
        except IndexError:
            print("!!!Please enter a string!!!")
            continue


if __name__ == "__main__":
    main()
