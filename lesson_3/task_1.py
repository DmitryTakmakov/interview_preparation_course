"""
Написать программу, которая будет содержать функцию для получения имени файла
из полного пути до него. При вызове функции в качестве аргумента должно
передаваться имя файла с расширением. В функции необходимо реализовать поиск
полного пути по имени файла, а затем «выделение» из этого пути имени файла
(без расширения).
"""
import os


def path_splitter(filepath: str) -> str:
    parts = os.path.split(filepath)
    filename = parts[1].split('.')[0]
    return filename


if __name__ == '__main__':
    full_path = input('Please enter the absolute path to a file: ')
    print(path_splitter(full_path))
