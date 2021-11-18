"""
Написать программу «Банковский депозит». Она должна состоять из функции и ее
вызова с аргументами. Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 %
годовых). 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых,
2 года – 6.5 % годовых). 100000–1000000 руб (6 месяцев — 7 % годовых,
год — 8 % годовых, 2 года — 7.5 % годовых). Необходимо написать функцию, в
которую будут передаваться параметры: сумма вклада и срок вклада. Каждый из
трех банковских продуктов должен быть представлен в виде словаря с ключами
(begin_sum, end_sum, 6, 12, 24). Ключам соответствуют значения начала и конца
диапазона суммы вклада и значения процентной ставки для каждого срока. В
функции необходимо проверять принадлежность суммы вклада к одному из диапазонов
и выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада
на конец срока.
"""


def make_deposit(amount: int, period: int) -> float:
    if period not in (6, 12, 24):
        raise ValueError('Значение периода должно быть равным 6, 12 или 24!')
    first_product = {
        'begin_sum': 1000,
        'end_sum': 9999,
        6: 0.025,
        12: 0.06,
        24: 0.1
    }
    second_product = {
        'begin_sum': 10000,
        'end_sum': 99999,
        6: 0.03,
        12: 0.07,
        24: 0.13
    }
    third_product = {
        'begin_sum': 100000,
        'end_sum': 1000000,
        6: 0.035,
        12: 0.08,
        24: 0.15
    }
    if not first_product['begin_sum'] <= amount <= third_product['end_sum']:
        raise ValueError(
            f'Введена неверная сумма депозита! Сумма должна быть больше '
            f'{first_product["begin_sum"]} и меньше {third_product["end_sum"]}')
    products = [first_product, second_product, third_product]
    current_product = {}
    for i in range(len(products)):
        if products[i]['begin_sum'] <= amount <= products[i]['end_sum']:
            current_product = products[i]
    final_amount = amount + (amount * current_product[period])
    return final_amount.__round__(2)


def main():
    deposit = int(input(
        'Введите сумму, которую вы хотите внести (от 1000 до 1000000): '))
    period = int(input('Введите срок депозита в месяцах (6, 12 или 24): '))
    print(
        f'По истечению срока вклада вы получите {make_deposit(deposit, period)} рублей.')


if __name__ == '__main__':
    main()
