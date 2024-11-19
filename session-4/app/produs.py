import json


class Produs(object):
    # class level variable (set)
    category_options = {"Haine", "Accesorii", "Incaltaminte"}

    def __init__(self, categorie=None, nume=None, pret=None, stoc=None):
        self._categorie = categorie
        self._nume = nume
        self._pret = pret
        self._stoc = stoc

    def display(self):
        print(f'Product: {self._nume}, Price: {self._pret}lei, Stoc: {self._stoc}.')

    def set_categorie(self, categorie):
        self._categorie = categorie

    def set_nume(self, nume):
        self._nume = nume

    def set_pret(self, pret):
        self._pret = pret

    def set_stoc(self, stoc):
        self._stoc = stoc

    def validare_categorie(self):
        return self._categorie in Produs.category_options

    def validare_nume(self):
        return self._nume.isalpha()

    def validare_pret(self):
        return isinstance(self._pret, float) and self._pret >= 0.0

    def validare_stoc(self):
        return isinstance(self._stoc, int) and self._stoc >= 0

    def to_dict(self):
        return {
            "categorie": self._categorie,
            "produse": self._nume,
            "pret": self._pret,
            "stoc": self._stoc
        }
