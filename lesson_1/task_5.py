"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию
должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Необходимо в главной функции реализовать вложенную функцию подсчета процентов
для пополняемой суммы. Примем, что клиент вносит средства в последний день
каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6
месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает
сумму дополнительно внесенных средств (с процентами), а главная функция — общую
сумму по вкладу на конец периода.
"""


def make_deposit(amount: int, period: int, extra_deposit: int) -> float:
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

    def calculate_extra(extra_amount: int, current_prod: dict,
                        extra_period: int) -> float:
        percents = 0.0
        if extra_period == 6:
            percents = current_prod[extra_period] / 6
        if extra_period == 12:
            percents = current_prod[extra_period] / 12
        if extra_period == 24:
            percents = current_prod[extra_period] / 24
        return (extra_amount + (extra_amount * percents)) * (extra_period - 2)

    final_amount = amount + (
            amount * current_product[period]) + calculate_extra(
        extra_deposit, current_product, period)
    return final_amount.__round__(2)


def main():
    deposit = int(input(
        'Введите сумму, которую вы хотите внести (от 1000 до 1000000): '))
    period = int(input('Введите срок депозита в месяцах (6, 12 или 24): '))
    monthly = int(input('Введите сумму фиксированного ежемесячного платежа: '))
    print(
        f'По истечению срока вклада вы получите {make_deposit(deposit, period, monthly)} рублей.')


if __name__ == '__main__':
    main()
