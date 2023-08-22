import sys

from functions import _read_, _write_, _create_, _search_, _update_
#  ключи для словаря и для вывода
keys = ['имя', 'фамилия', 'отчество', 'организацию', 'рабочий телефон']


# вывод интерфейса
def print_commands():
    print('\nТелефонный справочник:\n',
          '1 - Вывести справочник',
          '2 - Создать новую запись',
          '3 - Найти по фамилии',
          '4 - Найти по номеру телефона',
          '5 - Найти по фамилии и имени',
          '6 - Изменить запись',
          '0 - Выйти из программы',
          sep='\n')


# вывод записей из словаря
def _result_(dictionary):
    for phone, data in dictionary.items():
        print(f'Личный номер: {phone}')
        print()
        for name, record in zip(keys, data):
            print(f'{name.capitalize()}: {data[record]}')

# ввод данных в словарь
def _read_values_():
    phone = input('\nВведите личный номер телефона: ')
    new_data = {phone: {}}
    for key, value in zip(keys, keys):
        new_data[phone][key] = input(f'Введите {value}: ')
    return new_data


def main(file):
    try:
        dataset = _read_(file)
        if dataset is None:
            print("Установите аргументом название файла")
            sys.exit()
        print_commands()
        while True:
            command = input('\nВведите необходимую команду ')
            if command == '1':
                _result_(dataset)
            elif command == '2':
                values = _read_values_()
                dataset = _create_(dataset, values)
                _write_(dataset, file)
            elif command == '3':
                value = input('\nВведите фамилию: ')
                result = _search_(dataset, command, value)
                _result_(result)
            elif command == '4':
                value = input('\nВведите личный телефон: ')
                result = _search_(dataset, command, value)
                _result_(result)
            elif command == '5':
                value = input('\nВведите фамилию и имя: ').split(' ')
                result = _search_(dataset, command, value)
                _result_(result)
            elif command == '6':
                result = _read_values_()
                dataset = _update_(dataset, result)
                _write_(dataset, file)
                print('Данные обновлены')
            elif command == '0':
                print('\nСпасибо что воспользовались!')
                _write_(dataset, file)
                break
            else:
                print('\nТакой комманды не существует')
    except KeyboardInterrupt:
        print("\nЗавершайте работу программы нажатием на 0")


if __name__ == '__main__':
    ph_book_name = 'database.json'
    main(ph_book_name)
