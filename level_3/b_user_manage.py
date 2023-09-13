"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username_to_ban):
        if username_to_ban in self.usernames:
            self.usernames.remove(username_to_ban)
        else:
            print('Такого пользователя не существует')


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames.clear()


if __name__ == '__main__':
    print('UserManager:')
    user_manager = UserManager()
    user_manager.add_user('Ben')
    user_manager.add_user('Beth')
    print(user_manager.get_users())

    print('\nAdminManager:')
    admin_manager = AdminManager()
    admin_manager.add_user('Ben')
    admin_manager.add_user('Beth')
    admin_manager.ban_username('Ben')
    admin_manager.ban_username('Alex')
    print(admin_manager.get_users())

    print('\nSuperAdminManager:')
    super_admin_manager = SuperAdminManager()
    super_admin_manager.add_user('Ben')
    super_admin_manager.add_user('Beth')
    super_admin_manager.ban_username('Ben')
    super_admin_manager.ban_username('Alex')
    super_admin_manager.ban_all_users()
    print(super_admin_manager.get_users())