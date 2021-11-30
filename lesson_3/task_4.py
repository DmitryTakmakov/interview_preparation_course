"""
Написать программу, в которой реализовать две функции. В первой должен
создаваться простой текстовый файл. Если файл с таким именем уже существует,
выводим соответствующее сообщение. Необходимо открыть файл и подготовить два
списка: с текстовой и числовой информацией. Для создания списков использовать
генераторы. Применить к спискам функцию zip(). Результат выполнения этой
функции должен должен быть обработан и записан в файл таким образом, чтобы
каждая строка файла содержала текстовое и числовое значение. Вызвать вторую
функцию. В нее должна передаваться ссылка на созданный файл. Во второй функции
необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""
import os
import random
import string


def first_function():
    filename = input('Please enter the file name: ')
    cur_dir = os.scandir()
    for entry in cur_dir:
        if entry.name == str(filename + '.txt'):
            print('File with this name already exists.')
            return
    text_vals = [
        ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase,
                               k=10))
        for _ in range(10)]
    num_vals = [random.randint(0, 1000) for _ in range(10)]
    unified_vals = zip(text_vals, num_vals)
    with open(f'{filename}.txt', 'w') as f:
        for item in unified_vals:
            first, second = item
            f.write(f'{first}:\t{second}\n')
        f.close()
    second_function(os.path.join(os.getcwd(), f'{filename}.txt'))


def second_function(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            print(line)


if __name__ == '__main__':
    first_function()
