import json
from json.decoder import JSONDecodeError


# чтение файла
def _read_(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Этот файл {file} не существует")
        return None
    except JSONDecodeError as e:
        print(f"Телефонная книга отсутствует или пуста: {e}")
        return None


# запись файла
def _write_(dictionary, file):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False)


# Создание записи
def _create_(dictionary: dict, data: dict):
    dictionary.update(data)
    return dictionary


# Обновление абонента
def _update_(dictionary: dict, data: dict):
    for phone in dictionary:
        if list(data.keys())[0] in phone:
            return {**dictionary, **data}



# Поиск абонента в справочнике по фамилиии или имени
def _search_(dictionary, search, value):
    result = {}
    # поиск по номеру телефона
    if search == '4':
        fl = True

        for phone in dictionary:
            if value in phone:
                result.update({phone: dictionary[phone]})
                fl = False
        if fl:
            print("Такого номера нет в справочнике\n")
    # поиск по фамилии
    elif search == '3':
        fl = True
        for phone, data in dictionary.items():
            if value.lower() in data['фамилия'].lower():
                result.update({phone: dictionary[phone]})
                fl = False
        if fl:
            print("Такой фамилии нет в справочнике")

    # Поиск по фамилии и имени
    elif search == '5':
        fl = True
        for phone, data in dictionary.items():
            try:
                if value[0].lower() in data['фамилия'].lower() and value[1].lower() in data['имя'].lower():
                    result.update({phone: dictionary[phone]})
                    fl = False
            except IndexError:
                print("Фамилия и имя введены неверно\n")
        if fl:
            print("Такой фамилии и имени нет в справочнике")
    return result
