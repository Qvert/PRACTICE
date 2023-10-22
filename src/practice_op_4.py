from slovar_alph import *


def read_file(name_file: str) -> list[str]:
    with open(name_file, encoding="utf8") as file:
        file_read = file.readlines()
    return file_read


def write_file_enc(text: str, key: str) -> None:
    with open("Encrypt.txt", encoding="utf8", mode="w") as file:
        file.writelines(key)
        file.writelines(text)


def write_file_decode(text: str, key: str) -> None:
    with open("Decode.txt", encoding="utf8", mode="w") as file:
        file.writelines(text)
        file.writelines(key)


def check_text_key(text: str, key: str) -> bool:
    flag_rus = False
    flag_eng = False
    for elem_t, elem_k in zip(text, key):
        if elem_t.upper() in rus_symbol or elem_k.upper() in rus_symbol:
            flag_rus = True
        if elem_t.upper() in eng_symbol or elem_k.upper() in eng_symbol:
            flag_eng = True
    if flag_eng == flag_rus:
        return False
    return True


def encrypt_decode_word(text: str, key: str, parameter=None) -> str:
    """
    :param parameter: Parameter for encryption or decryption
    :param text: Source text
    :param key: Encryption key
    :return: Decode text
    """
    string_new_key = ""
    string_new_text = ""
    while True:
        string_new_key += key
        if len(text) < len(string_new_key):
            break
    string_new_key = string_new_key[: len(text)]

    for i, j in zip(text, string_new_key):
        if i.upper() in rus_symbol:
            new_index_symbol = 0
            index_key_dict, index_text_dict = (
                dict_rus_symbol_upper[j.upper()],
                dict_rus_symbol_upper[i.upper()],
            )
            if parameter == "encrypt":
                new_index_symbol = index_text_dict + index_key_dict
            if parameter == "decode":
                new_index_symbol = abs(index_text_dict - index_key_dict)

            if new_index_symbol > 33 or new_index_symbol <= 0:
                new_index_symbol = abs(new_index_symbol - 33)
            if i.isupper():
                string_new_text += list(dict_rus_symbol_upper.keys())[
                    new_index_symbol - 1
                ]
            else:
                string_new_text += list(dict_rus_symbol_upper.keys())[
                    new_index_symbol - 1
                ].lower()

        if i.upper() in eng_symbol:
            index_key_dict, index_text_dict = (
                dict_eng_symbol_upper[j.upper()],
                dict_eng_symbol_upper[i.upper()],
            )
            new_index_symbol = 0

            if parameter == "encrypt":
                new_index_symbol = index_text_dict + index_key_dict
            if parameter == "decode":
                new_index_symbol = abs(index_text_dict - index_key_dict)

            if new_index_symbol > 26 or new_index_symbol <= 0:
                new_index_symbol = abs(new_index_symbol - 26)
            if i.isupper():
                string_new_text += list(dict_eng_symbol_upper.keys())[
                    new_index_symbol - 1
                ]
            else:
                string_new_text += list(dict_eng_symbol_upper.keys())[
                    new_index_symbol - 1
                ].lower()

        if i.upper() not in eng_symbol and i.upper() not in rus_symbol:
            string_new_text += i
    return string_new_text


def main() -> None:
    """Main function"""
    source_text, key = read_file("text.txt")
    source_text_enc, key = read_file("Encrypt.txt")
    while True:
        action = input(
            "Select an action.\n"
            "1.Encrypt the string\n"
            "2.Decode the string\n"
            "3.Exit the program\n"
        )
        match action:
            case "1":
                if check_text_key(source_text, key):
                    write_file_enc(
                        encrypt_decode_word(source_text, key, "encrypt"), key
                    )
                else:
                    print(
                        "There are letters of different alphabet in the key or text\n"
                    )
            case "2":
                write_file_decode(
                    encrypt_decode_word(source_text_enc, key, "decode"), key
                )
            case "3":
                break


if __name__ == "__main__":
    main()
