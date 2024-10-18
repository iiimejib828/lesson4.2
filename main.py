class User:
    def __init__(self, user_id: int, name: str):
        # Приватные атрибуты
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа по умолчанию для обычных пользователей

    # Get и set методы для доступа к приватным данным
    def get_id(self):
        return self.__id

    def set_id(self, user_id: int):
        self.__id = user_id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level: str):
        self.__access_level = access_level

    def __repr__(self):
        return f"User(ID: {self.__id}, Имя: {self.__name}, Уровень доступа: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        # Устанавливаем уровень доступа администратора как приватный
        self.set_access_level ('admin')

    # Метод для добавления нового пользователя
    def add_user(self, user_list: list, user: User):
        user_list.append(user)
        print(f"User {user.get_name()} added to the system.")

    # Метод для удаления пользователя
    def remove_user(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"User with ID {user_id} removed from the system.")
                return
        print(f"User with ID {user_id} not found in the system.")

    def __repr__(self):
        return f"Admin(ID: {self.get_id()}, Имя: {self.get_name()}, Уровень доступа: {self.get_access_level()})"

# Создаем список пользователей
users = []

# Создаем администратора
admin = Admin(1, "Alice")

# Создаем обычных пользователей
user1 = User(2, "Bob")
user2 = User(3, "Charlie")

# Добавляем пользователей через администратора
admin.add_user(users, admin)
admin.add_user(users, user1)
admin.add_user(users, user2)

# Удаляем пользователя через администратора
admin.remove_user(users, 2)

# Выводим оставшихся пользователей
print("\nСписок пользователей:\n")
for t_user in users:
    print(f"Имя: {t_user.get_name()}, Id: {t_user.get_id()}, уровень доступа: {t_user.get_access_level()}")
