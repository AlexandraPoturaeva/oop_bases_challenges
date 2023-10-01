"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса Employee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self):
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float):
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, amount: float):
        self.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, amount: float):
        self.salary -= amount


class Developer(ItDepartmentEmployee, SuperAdminMixin):
    def __init__(self, name: str, surname: str, age: int, salary: float, program_lang: str):
        super().__init__(name, surname, age, salary)
        self.program_lang = program_lang

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, programming language - {self.program_lang}'


if __name__ == '__main__':
    python_developer = Developer(name='Guido', surname='van Rossum', age=67, salary=500000, program_lang='Python')

    print(python_developer.get_info())

    python_developer.increase_salary(amount=20)
    print(python_developer.get_info())

    python_developer.decrease_salary(amount=20)
    print(python_developer.get_info())
