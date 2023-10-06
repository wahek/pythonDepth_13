import unittest

from hw import Student


class TestUnittest(unittest.TestCase):
    def setUp(self):
        self.ob1 = Student('Hf', 'Fdx', 'Wef')
        self.ob2 = Student('Ddf', 'Xef', 'Rrf')
        self.ob3 = Student('Nm', 'Wex', 'Gef')

    def test_subjects_grades(self):
        self.assertEquals(self.ob1.subjects_grades,
                          {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                           'history': []})
        self.assertEquals(self.ob2.subjects_grades,
                          {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                           'history': []})
        self.assertEquals(self.ob3.subjects_grades,
                          {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                           'history': []})

    def test_subjects_tests(self):
        self.assertEquals(self.ob1.subjects_tests,
                          {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                           'history': []})
        self.assertEquals(self.ob2.subjects_tests,
                          {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [],
                           'history': []})
        self.assertEquals(self.ob3.subjects_tests,
                          {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [], 'history': []})

    def test_subjects_grades_add(self):
        self.ob1.add_grade('english', 3)
        self.assertEquals(self.ob1.subjects_grades,
                          {'subject': [], 'english': [3], 'math': [], 'physics': [], 'chemistry': [],
                           'history': []})
        self.ob1.add_grade('english', 4)
        self.assertEquals(self.ob1.subjects_grades,
                          {'subject': [], 'english': [3, 4], 'math': [], 'physics': [], 'chemistry': [],
                           'history': []})
        self.ob1.add_grade('chemistry', 5)
        self.assertEquals(self.ob1.subjects_grades,
                          {'subject': [], 'english': [3, 4], 'math': [], 'physics': [], 'chemistry': [5],
                           'history': []})
        self.ob2.add_grade('chemistry', 5)
        self.assertEquals(self.ob2.subjects_grades,
                          {'subject': [], 'english': [], 'math': [], 'physics': [], 'chemistry': [5],
                           'history': []})

    def test_average_grade(self):
        self.ob1.add_grade('english', 3)
        self.ob1.add_grade('english', 4)
        self.ob1.add_grade('chemistry', 5)
        self.assertEquals(self.ob1.average_grades(), 4)
        self.assertEquals(self.ob2.average_grades(), 0)
