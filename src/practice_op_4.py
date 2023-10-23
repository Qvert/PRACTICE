import os.path

from slovar_alph import *


def write_file_enc(text: str, key: str) -> None:
    """
    Function write finished encrypt string
    :param text: Encrypt text
    :param key: Key
    :return: None
    """
    with open("Encrypt string.txt", encoding="utf8", mode="w+") as file:
        file.write(f"{key}\n")
        file.writelines(text)


def write_file_decode(text: str, key: str) -> None:
    """
    Function write decoding text
    :param text: Decode text
    :param key: Key
    :return: None
    """
    with open("Decode string.txt", encoding="utf8", mode="w+") as file:
        file.write(f"{key}\n")
        file.writelines(text)


def check_text_key(text: str, key: str) -> bool:
    """
    Check that the key and the source text are of the same alphabet
    :param text: Source text
    :param key: Key
    :return: True or False
    """
    flag_rus, flag_eng = False, False
    for elem_t, elem_k in zip(text, key):
        if elem_t.upper() in rus_symbol or elem_k.upper() in rus_symbol:
            flag_rus = True
        if elem_t.upper() in eng_symbol or elem_k.upper() in eng_symbol:
            flag_eng = True
    if flag_eng == flag_rus:
        return False
    return True


def encrypt_decode_string(text: str, key: str, parameter=None) -> str:
    """
    :param parameter: Parameter for encryption or decryption
    :param text: Source text
    :param key: Encryption key
    :return: Decode text
    """
    string_new_text = string_new_key_new = ""
    string_new_key = key * len(text)
    count_ = 0
    for element in range(len(text)):
        if text[element].upper() in rus_symbol or text[element].upper() in eng_symbol:
            string_new_key_new += string_new_key[element - count_]
        else:
            count_ += 1
            string_new_key_new += text[element]

    for i, j in zip(text, string_new_key_new):
        if i.upper() in rus_symbol:
            new_index_symbol = 0
            index_key_dict, index_text_dict = (
                dict_rus_symbol_upper[j.upper()],
                dict_rus_symbol_upper[i.upper()],
            )
            if parameter == "encrypt":
                new_index_symbol = index_text_dict + index_key_dict

            if parameter == "decode":
                new_index_symbol = index_text_dict - index_key_dict

            if new_index_symbol > 32 or new_index_symbol < 0:
                new_index_symbol = abs(abs(new_index_symbol) - 32)
            if i.isupper():
                string_new_text += list(dict_rus_symbol_upper.keys())[new_index_symbol]
            else:
                string_new_text += list(dict_rus_symbol_upper.keys())[
                    new_index_symbol
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
                new_index_symbol = index_text_dict - index_key_dict

            if new_index_symbol > 25 or new_index_symbol < 0:
                new_index_symbol = abs(abs(new_index_symbol) - 25)
            if i.isupper():
                string_new_text += list(dict_eng_symbol_upper.keys())[new_index_symbol]
            else:
                string_new_text += list(dict_eng_symbol_upper.keys())[
                    new_index_symbol
                ].lower()

        if i.upper() not in eng_symbol and i.upper() not in rus_symbol:
            string_new_text += i
    return string_new_text


def main() -> None:
    """Main function"""
    f = open("text.txt", encoding="utf8", mode="r").readlines()
    key, source_text = f[0].replace('\n', ''), f[1]

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
                        encrypt_decode_string(source_text, key, "encrypt"), key
                    )
                    print("Your string is encrypted\n")
                else:
                    print(
                        "There are letters of different alphabet in the key or text\n"
                    )
            case "2":
                if os.path.isfile("Encrypt string.txt"):
                    f = open("Encrypt string.txt", encoding="utf8", mode="r").readlines()
                    key_decode, source_text_enc = f[0].replace('\n', ''), f[1]

                    write_file_decode(
                        encrypt_decode_string(source_text_enc, key_decode, "decode"),
                        key_decode,
                    )
                    print("Your line has been decrypted\n")
                else:
                    print("I'm sorry, you haven't encrypted the string yet.")
            case "3":
                break


if __name__ == "__main__":
    main()
