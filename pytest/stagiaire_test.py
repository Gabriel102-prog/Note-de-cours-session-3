import pytest
from stagiaire import Stagiaire


@pytest.fixture
def stagiaire1():
    return Stagiaire("Alice", 22, "S001")


@pytest.fixture
def stagiaire2():
    return Stagiaire("Bob", 25, "S002")


def test_creation_stagiaire(stagiaire1):
    """Test de la création d'un stagiaire."""
    # Vérifie que l'objet est bien une instance de Stagiaire
    assert isinstance(stagiaire1, Stagiaire)
    # Vérifie que la méthode __str__ fonctionne correctement
    assert "Alice" in str(stagiaire1)
    assert "22" in str(stagiaire1)
    assert "S001" in str(stagiaire1)


def test_comparaison_inferieur(stagiaire1, stagiaire2):
    """Test de la comparaison d'âge (<)."""
    assert stagiaire1 < stagiaire2  # 22 < 25
    assert not (stagiaire2 < stagiaire1)  # 25 < 22 → False


def test_comparaison_type_invalide(stagiaire1):
    """Test si la comparaison avec un type non Stagiaire lève une erreur."""
    with pytest.raises(TypeError):
        _ = stagiaire1 < 42  # doit lever TypeError
    #Le _ est juste une variable “jetable” (on ne veut pas utiliser
    # la valeur du résultat, on veut juste provoquer l’erreur).