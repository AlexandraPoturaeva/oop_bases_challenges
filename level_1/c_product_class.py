"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price_rub: float, weight_g: float) -> None:
        self.name = name
        self.description = description
        self.price_rub = price_rub
        self.weight_g = weight_g


if __name__ == '__main__':
    product = Product(
        name='Чай черный Greenfield English Edition',
        description='Черный листовой чай',
        price_rub=153.0,
        weight_g=200.0,
    )
    print('Информация о продукте: {name}, {description}, {price_rub} руб., {weight_g} г'.format(
        name=product.name,
        description=product.description,
        price_rub=product.price_rub,
        weight_g=product.weight_g,
    ))
