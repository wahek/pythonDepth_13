import csv
import re
import statistics
from copy import deepcopy


class CustomException(Exception):
    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return self.message


class CustomExceptionName(CustomException):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value

    def __str__(self):
        return f'{self.message}, Вы ввели:{self.value}'


class CustomExceptionGreate(CustomException):
    def __init__(self, message, value_min, value_max):
        super().__init__(message)
        self.value_min = value_min
        self.value_max = value_max

    def __str__(self):
        return f'{self.message}, минимальна оценка: {self.value_min}, максимальная: {self.value_max}'


class ValidName:
    def __set_name__(self, owner, name):
        self.__param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.__param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.__param_name, value)

    @staticmethod
    def validate(value):
        if not value.istitle() and re.sub(r'[^\d.@%$&^*()+=]+', "jjj", value):
            raise CustomExceptionName('Ошибка имени', value)


class Student:
    """Задание. Создайте класс студента.
    - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
    - Названия предметов должны загружаться из файла CSV при создании экземпляра.
    Другие предметы в экземпляре недопустимы.
    - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    - Также экземпляр должен сообщать средний балл по тестам для каждого предмета
    и по оценкам всех предметов вместе взятых."""
    __last_name = ValidName()
    __first_name = ValidName()
    __patronymic = ValidName()

    def __init__(self, last_name, first_name, patronymic):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__patronymic = patronymic
        self._subjects_grades = dict
        self._subjects_tests = dict
        with open('subjects.csv', newline='') as data:
            res = csv.reader(data, quotechar='|')
            self._subjects_grades = {key[0]: [] for key in res}
            self._subjects_tests = deepcopy(self._subjects_grades)

    @staticmethod
    def valid_value(max_, min_):
        def deco(function):
            def wrapper(*args, **kwargs):
                func = function(*args, **kwargs)
                for arg in args:
                    try:
                        if max_ > arg > min_:
                            func()
                        else:
                            raise CustomExceptionGreate('Выход за пределы оценивания', min_+1, max_-1)
                    except TypeError:
                        pass

            return wrapper

        return deco

    @property
    def subjects_grades(self):
        return self._subjects_grades

    @valid_value(6, 1)
    def add_grade(self, subject, value: int):
        self._subjects_grades[subject].append(value)

    @valid_value(101, -1)
    def add_taste(self, subject, value: int):
        self._subjects_tests[subject].append(value)

    @property
    def subjects_tests(self):
        print(id(self.subjects_grades))
        print(id(self._subjects_tests))
        return self._subjects_tests

    def average_test(self, subject):
        return statistics.mean(self._subjects_tests[subject])

    def average_grades(self):
        res = []
        for i in self._subjects_grades.values():
            print(i)
            if i:
                res.append(statistics.mean(i))
        return statistics.mean(res)


if __name__ == '__main__':
    a = Student('Hf', 'Fdx', 'Wef')
    print(a.subjects_grades)
    print(a.subjects_tests)
    a.add_grade('math', 5)
    print(a.subjects_grades)
    a.add_taste('chemistry', 100)
    a.add_taste('chemistry', 51)
    a.add_grade('math', 3)
    a.add_grade('physics', 0)
    print(a.average_test('chemistry'))
    print(a.average_grades())
    print(a.subjects_grades)
    print(a.subjects_tests)
