from collections import Counter
from functools import wraps


ls_haf = list()
text_input = ""
code_string = ""


def recursion_make_code_symbol(st, el):
    global ls_haf
    if type(el) == str:
        ls_haf.append((el, st))
        return
    recursion_make_code_symbol(st + "0", el[0])
    recursion_make_code_symbol(st + "1", el[1])
    return


def make_tree_huffman_code(input_str: str) -> str:
    """
    :param input_str: Input stroke
    :return: Tuple tree huffman code
    """
    ls = list(sorted(Counter(input_str).items(), key=lambda x: x[1]))

    while len(ls) >= 2:
        d = ((ls[0][0], ls[1][0]), ls[0][1] + ls[1][1])
        if ls[-1][1] < d[1]:
            ls.append(d)
        else:
            for num in range(2, len(ls)):
                if ls[num][1] >= d[1]:
                    ls.insert(num, d)
                    break
        ls.pop(0)
        ls.pop(0)
    return ls[0][0]


def make_dict_huffman(text: str) -> dict:
    """
    :param text: Input string
    :return: Dict with symbols code
    """
    global ls_haf
    ls = make_tree_huffman_code(text)
    ls_haf = []
    recursion_make_code_symbol("", ls)
    return dict(ls_haf)


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
    global text_input, code_string
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
                    text_input = input("Please enter the string you want to encode: ")
                    continue
                case "2":
                    code_string = compress_code_huffman(
                        text_input, make_dict_huffman(text_input)
                    )
                    print(
                        f"Your string '{text_input}' is in coded form: {code_string}\n"
                    )
                case "3":
                    result_decoding = decompress_code_huffman(
                        code_string, make_dict_huffman(text_input)
                    )
                    print(
                        f"Your string '{code_string}' is in decode form: {result_decoding}\n"
                    )
                case "4":
                    break
        except IndexError:
            print("!!!Please enter a string!!!")
            continue


if __name__ == "__main__":
    main()
