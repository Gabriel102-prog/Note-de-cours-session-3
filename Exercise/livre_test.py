import pytest
from livre import Livre

def test_creation_livre():
    l=Livre("disponible", "1234", "Harry Poteur", "Helmi")
    assert l.titre == "Harry Poteur"
    assert l.isbn == "1234"
    assert l.statut == "disponible"
    assert l.auteur == "Helmi"
    assert l.quantite_stock == 0

def test_creation_livre2():
    with pytest.raises(ValueError):
        Livre("", "5432", "Ricardo cuisine", "Marius")

def test_achat():
    l = Livre("précommande", "6767", "Programeur pour les nul", "Samuel")
    l.achat(12)
    assert l.quantite_stock == 12
    with pytest.raises(ValueError):
        l.achat(0)
    with pytest.raises(ValueError):
        l.achat(-67)

def test_vente():
    l = Livre("précommande", "6969", "Design interieur pour les nul", "Édouard")
    l.achat(10)
    l.vente(2)
    assert l.quantite_stock == 8
    with pytest.raises(ValueError):
        l.vente(25)
    with pytest.raises(ValueError):
        l.vente(0)
    with pytest.raises(ValueError):
        l.vente(-2)
def test_changer_statut():
    l = Livre("indisponible", "2222", "Manuelle de soccer", "Olivier")
    l.changer_statut("disponible")
    assert l.statut == "disponible"
    with pytest.raises(ValueError):
        l.changer_statut("Tout mouiller")

def test_info():
    l = Livre("indisponible", "8972", "Programmation pour les nul", "Florence")
    i = l.infos()
    assert isinstance(i, dict)
    assert list(l.infos().keys()) == ["titre", "auteur", "isbn", "statut", "stock"]
    assert l.infos() == {"titre": "Programmation pour les nul", "auteur": "Florence", "isbn": "8972","statut": "indisponible", "stock": 0}

def test_str():
    l = Livre("disponible", "8734", "Séducteur professionel", "Marius")
    assert l.__str__() == (f"Séducteur professionel par Marius "
                f"(ISBN: 8734, Statut: disponible) - "f"Stock: 0")
