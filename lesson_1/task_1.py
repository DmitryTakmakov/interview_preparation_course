"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""


def do_results(first: int, second: int) -> list:
    results = []
    j = 1
    while j <= second:
        row = []
        for i in range(1, first + 1):
            row.append(f'{i}*{j}={i * j}')
            i += 1
        results.append(row)
        j += 1
    return results


def main():
    first = int(input('Введите первый множитель: '))
    second = int(input('Введите второй множитель: '))
    results_list = do_results(first, second)
    for i in range(len(results_list)):
        row_string = ''
        for j in range(len(results_list[i])):
            row_string += results_list[i][j] + '\t'
        print(row_string)


if __name__ == '__main__':
    main()
