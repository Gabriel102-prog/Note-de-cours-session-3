
from etudiant import Student
import pytest  # importing our library of test


# # 3 test cases are defined in this test suite
# def test_create_student_grades():
#     student = Student()
#     assert (student.grades) == []
#
#
# def test_create_student_average():
#     student = Student()
#     assert student.academic_average == 0
#
#
# def test_add_grades():
#     student = Student()
#     student.add_grade(12)
#    assert student.academic_average == 12

#ou
@pytest.fixture
def student():
    """Fixture qui crée un étudiant pour chaque test"""
    return Student()


def test_create_student_grades(student):
    assert student.grades == []


def test_create_student_average(student):
    assert student.academic_average == 0


def test_add_grades(student):
    student.add_grade(12)
    assert student.academic_average == 12