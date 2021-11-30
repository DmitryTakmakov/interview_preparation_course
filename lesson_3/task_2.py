"""
Написать программу, которая запрашивает у пользователя ввод числа. На введенное
число она отвечает сообщением, целое оно или дробное. Если дробное — необходимо
далее выполнить сравнение чисел до и после запятой. Если они совпадают,
программа должна возвращать значение True, иначе False.
"""
import math


def process_numbers():
    user_input = float(input('Please enter a number: '))
    decimal, integer = math.modf(user_input)
    if decimal == 0:
        return 'This is an integer!'
    else:
        _integer = int(integer)
        round_value = len(str(_integer))
        decimal = decimal.__round__(round_value)
        integered_decimal = int(str(decimal)[2:])
        if _integer == integered_decimal:
            return True
        else:
            return False


if __name__ == '__main__':
    print(process_numbers())
