"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income

    def decrease_balance(self, spending: float):
        if spending > self.balance:
            raise ValueError('Spending out of balance')

        self.balance -= spending


if __name__ == '__main__':
    bank_account = BankAccount(owner_full_name='Ivan Ivanov', balance=10000.0)
    print(f'Изначальный баланс: {bank_account.balance}')
    bank_account.decrease_balance(5000.0)
    print(f'Списание 5000.0: баланс {bank_account.balance}')
    bank_account.decrease_balance(100000.0)
    print(f'Списание 100000.0: баланс {bank_account.balance}')
