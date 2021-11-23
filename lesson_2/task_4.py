"""
Реализовать возможность переустановки значения цены товара. Необходимо, чтобы
и родительский, и дочерний классы получили новое значение цены. Следует
проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class ItemDiscountReport(ItemDiscount):
    def __init__(self, parent_object: ItemDiscount):
        super().__init__(parent_object.name, parent_object.price)

    def get_parent_data(self) -> str:
        return f'Name: {self.name}; price: {self.price}'


def main():
    discount = ItemDiscount('Test_discount', 1000)
    discount_report = ItemDiscountReport(discount)
    print(discount_report.get_parent_data())
    discount.name = 'New_name'
    # создание нового отчета
    discount_report = ItemDiscountReport(discount)
    print(discount_report.get_parent_data())


if __name__ == '__main__':
    main()
