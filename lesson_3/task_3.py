"""
Создать два списка с различным количеством элементов. В первом должны быть
записаны ключи, во втором — значения. Необходимо написать функцию, создающую
из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
для него должно сохраняться значение None. Значения, которым не хватило ключей,
необходимо отбросить.
"""


def main():
    keys = ['id', 'username', 'email', 'password']
    values = [12345, 'test_user', 'test@example.com', 'pass', 123]
    if len(keys) > len(values):
        i = 0
        while i < abs(len(keys) - len(values)):
            values.append(None)
            i += 1
    combined_dict = dict(zip(keys, values))
    print(combined_dict)


if __name__ == '__main__':
    main()
