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
        Kasa.liczba_id += 1
        self.obslugiwany_klient = None

    def wyswietl_informacje(self):
        if self.obslugiwany_klient:
            print(f"Id: {self.id}   |   Kategoria: {self.kategoria}   |"
                  f"    Bezawaryjność: {self.bezawaryjnosc} |   Obsługiwany klient: {self.obslugiwany_klient.id}")
            return (f"[Id: {self.id} | Kategoria: {self.kategoria} |"
                    f" Bezawaryjność: {self.bezawaryjnosc} | Obsługiwany klient: {self.obslugiwany_klient.id}] ")
        else:
            print(f"Id: {self.id}   |   Kategoria: {self.kategoria}   |"
                  f"    Bezawaryjność: {self.bezawaryjnosc} |   Obsługiwany klient: {self.obslugiwany_klient}")
            return (f"[Id: {self.id} | Kategoria: {self.kategoria} |"
                    f" Bezawaryjność: {self.bezawaryjnosc} | Obsługiwany klient: {self.obslugiwany_klient}] ")


def utworz_losowe_kasy(liczba_kas):
    # funkcja tworząca wybraną ilość kas o losowych kategoriach
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
    print("Kasy")
    stan_kas = ""
    for elem in kasy:
        stan_kas += str(elem.wyswietl_informacje())
    print("-----------------")
    return stan_kas


def informacje_do_animacji(kasy, klienci):
    dane = []
    for kasa in kasy:
        if kasa.obslugiwany_klient is None:
            dane.append({"id_kasy": kasa.id, "czas_obslugi": 0})
        else:
            for klient in klienci:
                if klient.id == kasa.obslugiwany_klient.id:
                    dane.append({"id_kasy": kasa.id, "czas_obslugi": klient.czas_obslugi})
                    break
    print(dane)
    return dane
