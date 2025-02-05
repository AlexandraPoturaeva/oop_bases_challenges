"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""
from datetime import datetime, timedelta


class Product:
    def __init__(self, title: str, quantity: int) -> None:
        self.title = title
        self.quantity = quantity

    def get_full_info(self) -> str:
        return f'Product {self.title}, {self.quantity} in stock.'

    def is_available(self) -> bool:
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title: str, quantity: int, expiration_date: datetime) -> None:
        super().__init__(title, quantity)
        self.expiration_date = expiration_date

    def get_full_info(self) -> str:
        return f'Product {self.title}, {self.quantity} in stock, expires {self.expiration_date}.'

    def is_available(self) -> bool:
        return super().is_available() and self.expiration_date >= datetime.today()


if __name__ == '__main__':
    expiration_date_past = datetime.today() - timedelta(days=2)
    expiration_date_future = datetime.today() + timedelta(days=2)

    sofa = Product(title='sofa', quantity=5)
    milk_expired = FoodProduct(title='milk', quantity=30, expiration_date=expiration_date_past)
    milk_fresh = FoodProduct(title='milk', quantity=25, expiration_date=expiration_date_future)

    print(sofa.get_full_info(), sofa.is_available())
    print(milk_expired.get_full_info(), milk_expired.is_available())
    print(milk_fresh.get_full_info(), milk_fresh.is_available())
