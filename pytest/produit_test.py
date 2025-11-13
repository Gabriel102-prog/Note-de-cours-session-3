
import pytest
from produit import Produit

from unittest.mock import patch
from produit import ProductManagerApp

def test_creation_produit_valide():
    p = Produit("Banane", 10, 2.5)
    assert p.nom == "Banane"
    assert p.quantite == 10
    assert p.prix == 2.5

def test_nom_invalide():
    with pytest.raises(ValueError):
        Produit("", 5, 3)

def test_quantite_invalide():
    with pytest.raises(ValueError):
        Produit("Pomme", -1, 1.5)

def test_prix_invalide():
    with pytest.raises(ValueError):
        Produit("Orange", 2, -3)

def test_to_dict():
    p = Produit("Kiwi", 3, 1.2)
    d = p.to_dict()
    assert d == {"name": "Kiwi", "quantity": 3, "price": 1.2}

@pytest.fixture
def app():
    app = ProductManagerApp()
    yield app #similaire à return. Avec yield app : tu peux mettre
    # du code après le yield pour libérer des ressources,
    # fermer des fenêtres Tkinter,
    app.destroy()

def test_ajouter_produit_valide(app):
    app.entry_name.insert(0, "Lait")
    app.entry_quantity.insert(0, "5")
    app.entry_price.insert(0, "1.99")

    app.ajouter_produit()

    # Vérifie qu’un élément a été ajouté dans le Treeview
    items = app.tree.get_children()
    assert len(items) == 1
    values = app.tree.item(items[0], "values")
    assert values == ("Lait", "5", "1.99")

@patch("tkinter.messagebox.showerror")
#@patch("tkinter.messagebox.showerror") sert à simuler la boîte de
# dialogue d’erreur Tkinter lors d’un test, sans ouvrir de vraie fenêtre.
def test_ajouter_produit_invalide(mock_error, app):
    app.entry_name.insert(0, "")
    app.entry_quantity.insert(0, "abc")
    app.entry_price.insert(0, "-2")

    app.ajouter_produit()

    mock_error.assert_called()  # vérifie qu’un message d’erreur a été affiché
    assert len(app.tree.get_children()) == 0  # rien n’a été ajouté


def test_supprimer_avec_selection(app):
    # Ajoute un produit
    app.tree.insert("", "end", values=("Pain", 2, 3.0))
    item_id = app.tree.get_children()[0]

    app.tree.selection_set(item_id)
    app.supprimer_produit()

    assert len(app.tree.get_children()) == 0
