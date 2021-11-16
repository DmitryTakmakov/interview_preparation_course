"""
Разработать генератор случайных чисел. В функцию передавать начальное и
конечное число генерации (нуль необходимо исключить). Заполнить этими данными
список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import struct
import time


def last_bit(time_value: float) -> int:
    return struct.pack('!f', time_value)[-1] & 1


def get_random_bits(random_bits_number: int) -> int:
    result = 0
    for _ in range(random_bits_number):
        time.sleep(0)
        result <<= 1
        result |= last_bit(time.process_time())
    return result


def random_interval(first: int, second: int) -> int:
    if first == 0 or second == 0:
        raise ValueError('Either of the numbers should not be null!')
    if first == second:
        raise ValueError('Numbers should not be equal!')
    return first + random_below(second - first + 1)


def random_below(number: int):
    if number <= 0:
        raise ValueError('Numbers should differ by more than 1!')
    bits_number = number.bit_length()
    result = get_random_bits(bits_number)
    while result >= number:
        result = get_random_bits(bits_number)
    return result


def main():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    array_length = int(
        input('Введите количество чисел, которое вы хотите сгенерировать: '))
    numbers_list = [random_interval(first_number, second_number) for _ in
                    range(array_length)]
    print(numbers_list)
    numbers_dict = {str('elem_' + str(numbers_list.index(value))): value for
                    value in numbers_list}
    print(numbers_dict)


if __name__ == '__main__':
    main()
