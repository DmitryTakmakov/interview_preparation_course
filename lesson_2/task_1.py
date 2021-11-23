"""
Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию
о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен
содержать функцию (get_parent_data), отвечающую за отображение информации о
товаре в одной строке. Проверить работу программы, создав экземпляр (объект)
родительского класса.
"""


class ItemDiscount:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


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
