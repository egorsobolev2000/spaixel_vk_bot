import json


def JSONFile(path, data='data', d_or_l='dump'):
    """ Функция непосредственного вызова и
        работы с JSON файлом """

    if d_or_l == 'dump':
        with open(path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=3)

    if d_or_l == 'load':
        with open(path, "r") as read_file:
            load_data = json.load(read_file)
        return load_data
