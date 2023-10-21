eng_symbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_symbol = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
count = 1
dict_eng_symbol_upper, dict_eng_symbol_lower = dict(), dict()
dict_rus_symbol_upper, dict_rus_symbol_lower = dict(), dict()

for elem1, elem2 in zip(eng_symbol, eng_symbol.lower()):
    dict_eng_symbol_upper[elem1], dict_eng_symbol_lower[elem2] = count, count
    count += 1

count = 1
for elem1, elem2 in zip(rus_symbol, rus_symbol.lower()):
    dict_rus_symbol_upper[elem1], dict_rus_symbol_lower[elem2] = count, count
    count += 1
