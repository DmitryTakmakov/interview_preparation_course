"""
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором
списке часть строковых значений заменить на значения типа example345
(строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных
подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех
вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр, например: example345.
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
        ''.join(random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits,
            k=10)) for _ in range(10)]
    num_vals = [random.randint(0, 1000) for _ in range(10)]
    unified_vals = zip(text_vals, num_vals)
    with open(f'{filename}.txt', 'w') as f:
        for item in unified_vals:
            first, second = item
            f.write(f'{first}:\t{second}\n')
        f.close()
    second_function(os.path.join(os.getcwd(), f'{filename}.txt'))


# что-то я не понял, как реализовать обновление второй функции
def second_function(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            print(line)


if __name__ == '__main__':
    first_function()
