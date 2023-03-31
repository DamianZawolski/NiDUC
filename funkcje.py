import random

kategorie_klas = {
    0: 0.995,
    1: 0.990,
    2: 0.970,
    3: 0.950,
    4: 0.920
}

class Kasa:
    # klasa którą tworzymy obiekty kas
    liczba_id = 0
    def __init__(self, kategoria=0):
        self.id = Kasa.liczba_id
        self.kategoria = kategoria
        if kategoria in kategorie_klas:
            self.bezawaryjnosc = kategorie_klas[kategoria]
        else:
            self.bezawaryjnosc = 0  # bezawaryjność wynosi 0 jeśli klasa nie istnieje
        Kasa.liczba_id+=1
        self.w_trakcie_obslugi = False

    def wyswietl_cechy(self):
        print(f"Id: {self.id}   |   Kategoria: {self.kategoria}   |"
              f"    Bezawaryjność: {self.bezawaryjnosc} |   W trakcie obsługi: {self.w_trakcie_obslugi}")


def utworz_losowe_kasy(liczba_kas):
    # funkcja tworząca wybranoą ilość kas o losowych kategoriach
    lista_kas = []
    klucze = list(kategorie_klas.keys())
    for i in range(liczba_kas):
        lista_kas.append(Kasa(random.randint(0, len(klucze) - 1)))

    return lista_kas

def dodaj_nowe_losowe_kasy(kasy, liczba):
    klucze = list(kategorie_klas.keys())
    for i in range(liczba):
        kasy.append(Kasa(random.randint(0, len(klucze) - 1)))

    return kasy

def utworz_po_jednej_kasie_z_kategorii():
    lista_kas = []
    klucze = list(kategorie_klas.keys())
    for elem in klucze:
        lista_kas.append(Kasa(elem))
    return lista_kas

def dodaj_kase(kasy, kategoria):
    kasy.append(Kasa(kategoria))
    return kasy
def wyswietl_kasy(kasy):
    print("-----------------")
    for elem in kasy:
        elem.wyswietl_cechy()
    print("-----------------")
