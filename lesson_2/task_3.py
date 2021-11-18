"""
Усовершенствовать родительский класс таким образом, чтобы получить доступ к
защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


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
    main()
