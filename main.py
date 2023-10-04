import json


class CustomException(Exception):
    def __init__(self, *args):
        self.message = args if args else None

    def __str__(self):
        return self.message


class User:
    def __init__(self, user_id: int, level: int, user_name: str) -> None:
        self.level = level
        self.__user_id = user_id
        self.user_name = user_name

    @staticmethod
    def load(file_name: str):
        with open(f'{file_name}.json', 'r', encoding='utf-8') as file_json:
            data = json.load(file_json)
            users = []
            for one_user in data:
                users.append(User(*one_user.values()))
        return users

    def __eq__(self, other: 'User'):
        return self.__user_id == other.__user_id and self.user_name == other.user_name

    def __gt__(self, other: 'User'):
        return self.level > other.level


class Project:
    def __init__(self):
        self.users = User.load('test')
        self.entered_user = None

    def reload(self):
        self.users = User.load('test')

    def enter(self, u_id: int, u_name: str):
        test_user = User(u_id, 1, u_name)
        for user in self.users:
            if user == test_user:
                print('successful')
                self.entered_user = user
                return
        raise CustomException('Ошибка доступа')


def __repr__(self):
    return f'Имя: {self.user_name} Id: {self.__user_id} Уровень доступа: {self.level} '


if __name__ == '__main__':
    p1 = User(user_id=7, level=7, user_name="Test")
    print(p1.load(file_name='test'))
    a = Project()
    a.enter(2, 'vasya')
