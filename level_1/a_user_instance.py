"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    user = User(name='Aleksandra', username='a_poturaeva', age=29, phone='123')
    print('Информация о пользователе: {name}, {username}, {age}, {phone}'.format(
        name=user.name,
        username=user.username,
        age=user.age,
        phone=user.phone
    ))
