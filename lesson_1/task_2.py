"""
Функция принимает имя каталога и распечатывает его содержимое в виде «путь и
имя файла», а также любые другие файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk нельзя.
Данная задача показывает ваше умение работать с вложенными структурами.
"""

import os


def path_finder(path: str):
    for entry in os.scandir(path):
        print(f'name: {entry.name}, path: {entry.path}')
        if entry.is_dir():
            path_finder(os.path.join(path, entry.name))


if __name__ == '__main__':
    path = input('Введите абсолютный путь к директории: ')
    path_finder(path)
