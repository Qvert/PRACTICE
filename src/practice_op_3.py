dict_answer = dict()
ls_haf = list()


def recursion_cod(st, el):
    global ls_haf
    if type(el) == str:
        ls_haf.append((el, st))
        return
    recursion_cod(st + "0", el[0])
    recursion_cod(st + "1", el[1])
    return


def make_tree_huffman_code(input_str: str):
    """
    :param input_str: Input stroke
    :return:
    """
    se = set(input_str)
    ls = [(input_str.count(ch), ch) for ch in se]
    ls.sort()
    while len(ls) >= 2:
        d = (ls[0][0] + ls[1][0], (ls[0][1], ls[1][1]))
        if ls[-1][0] < d[0]:
            ls.append(d)
        else:
            for num in range(2, len(ls)):
                if ls[num][0] >= d[0]:
                    ls.insert(num, d)
                    break
        ls.pop(0)
        ls.pop(0)
    return ls[0][1]


def make_dict_huffman(text):
    global ls_haf
    ls = make_tree_huffman_code(text)
    ls_haf = []
    recursion_cod("", ls)
    print(dict(ls_haf))
    return dict(ls_haf)


def compress_code_huffman(text, dc_haf):
    str_result = ""
    for element in text:
        str_result = str_result + dc_haf[element]
    return str_result


def main():
    text = "привет"
    result = compress_code_huffman(text, make_dict_huffman(text))
    print(result, len(result))


if __name__ == "__main__":
    main()
