"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def decrease_balance(self, amount: float) -> float:
        self.balance -= amount
        return self.balance


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    bank_account = BankAccount(owner_full_name='IVAN IVANOV', balance=10000)
    print(
        f'Движение по банковскому счёту: '
        f'\n1.{bank_account.balance} '
        f'\n2.{bank_account.increase_balance(100)}'
        f'\n3.{bank_account.decrease_balance(200)}')

    credit_account = CreditAccount(owner_full_name='IVAN IVANOV', balance=10000)
    print(f'\nДвижение по кредитному счёту: '
          f'\n1.{credit_account.balance} '
          f'\n2.{credit_account.increase_balance(500)}'
          f'\n3.{credit_account.decrease_balance(2000)}')

    print(
        'Право на получение кредита: ' +
        ('есть' if credit_account.is_eligible_for_credit() else 'нет')
    )
