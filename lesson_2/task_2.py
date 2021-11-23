"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет
сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, parent_object: ItemDiscount):
        super().__init__(parent_object.name, parent_object.price)

    def get_parent_data(self) -> str:
        return f'Name: {self.name}; price: {self.price}'


def main():
    discount = ItemDiscount('Test_discount', 1000)
    discount_report = ItemDiscountReport(discount)
    print(discount_report.get_parent_data())


if __name__ == '__main__':
    print("При выполнении сгенерируется ошибка")
    main()
