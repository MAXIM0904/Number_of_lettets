import zipfile


def print_result(tuple_letter):
    print("Статистика по буквам:")
    for i_tuple in tuple_letter:
        print(f"Буква '{i_tuple[1]}' встречается {-i_tuple[0]} раз")


def open_file():
    voyna_i_mir_txt = open("voyna-i-mir.txt", "r", encoding='utf8')
    dict_letter = {}
    count_letter = 0
    for i_srt in voyna_i_mir_txt.read().split("\n"):
        for i_letter in i_srt:
            if i_letter.isalpha():
                dict_letter[i_letter] = dict_letter.get(i_letter, 0) + 1
                count_letter += 1
    dict_letter = [(-i_value, i_key) for i_key, i_value in dict_letter.items()]
    dict_letter.sort()
    print_result(dict_letter)


def extract_file():
    voyna_i_mir_zip = zipfile.ZipFile("voyna-i-mir.zip", "r")
    voyna_i_mir_zip.extract("voyna-i-mir.txt")
    voyna_i_mir_zip.close()
    open_file()


extract_file()

# зачёт!
