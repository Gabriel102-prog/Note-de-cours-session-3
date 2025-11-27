
import pytest
from student import Student

def test_nom():
    s = Student("Marius")
    assert s.name == "Marius"

@pytest.mark.parametrize("bad",["", " ", None, 123])
def test_invalide_name(bad):
    with pytest.raises(ValueError):
        Student(bad)

def test_ajout_note():
    s = Student("Sara")
    s.add_note(15)
    s.add_note(60)
    g = s.grades
    assert g == [15, 60]
    g.append(80)
    assert s.grades == [15, 60]
@pytest.mark.parametrize("note",[-1, 102, None])
def test_invalid_note(note):
    s = Student("Samuel")
    with pytest.raises(ValueError):
        s.add_note(note)