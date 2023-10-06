import pytest

from hw import Student, CustomExceptionGreate


@pytest.fixture()
def objects():
    return [Student('Hf', 'Fdx', 'Wef'),
            Student('Ddf', 'Xef', 'Rrf')]


# @pytest.fixture()
# def objects2():
#     return Student('Ddf', 'Xef', 'Rrf')


def test_add_grade(objects):
    objects[0].add_grade('history', 5)
    assert objects[0].subjects_grades == {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                                          'history': [5]}
    objects[0].add_grade('history', 2)
    assert objects[0].subjects_grades == {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                                          'history': [5, 2]}
    assert objects[1].subjects_grades == {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                                          'history': []}


def test_average_grades(objects):
    objects[0].add_grade('history', 5)
    objects[0].add_grade('history', 2)
    assert objects[0].average_grades() == 3.5
    assert objects[1].average_grades() == 0


def test_valid_value_exception(objects):
    with pytest.raises(CustomExceptionGreate,
                       match='Выход за пределы оценивания, минимальна оценка: 0, максимальная: 100'):
        objects[0].add_taste('english', -100)
