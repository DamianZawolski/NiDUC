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
        self.uszkodzona = False
        self.czas_naprawy = None
        self.przydzieleni_klienci = []

    def zwroc_laczny_czas_obslugi_klientow(self):
        czas = 0
        for klient in self.przydzieleni_klienci:
            czas += klient.czas_obslugi
        return czas

    def wyswietl_informacje(self):
        if self.obslugiwany_klient:
            print(f"Id: {self.id}   |   Kategoria: {self.kategoria}   |"
                  f"    Bezawaryjność: {self.bezawaryjnosc} | Uszkodzona: {self.uszkodzona} |"
                  f"   |    Czas naprawy: {self.czas_naprawy}   |   Obsługiwany klient: {self.obslugiwany_klient.id}")
            return (f"[Id: {self.id} | Kategoria: {self.kategoria} |"
                    f" Bezawaryjność: {self.bezawaryjnosc} | Uszkodzona: {self.uszkodzona} | "
                    f"Czas naprawy: {self.czas_naprawy} | Obsługiwany klient: {self.obslugiwany_klient.id}] ")
        else:
            print(f"Id: {self.id}   |   Kategoria: {self.kategoria}   |"
                  f"    Bezawaryjność: {self.bezawaryjnosc} | Uszkodzona: {self.uszkodzona} |"
                  f"   |    Czas naprawy: {self.czas_naprawy}   |   Obsługiwany klient: {self.obslugiwany_klient}")
            return (f"[Id: {self.id} | Kategoria: {self.kategoria} |"
                    f" Bezawaryjność: {self.bezawaryjnosc} | Uszkodzona: {self.uszkodzona} |"
                    f" Czas naprawy: {self.czas_naprawy} | Obsługiwany klient: {self.obslugiwany_klient}] ")


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


def stan_uszkodzen(kasy):
    uszkodzenia = []
    for kasa in kasy:
        uszkodzenia.append(kasa.uszkodzona)

    return uszkodzenia


def dodaj_opoznienia(kasy):
    uszkodzone = 0
    for kasa in kasy:
        if kasa.uszkodzona:
            uszkodzone += 1

    return uszkodzone


def zwroc_obslugiwanych_klientow(klienci):
    lista_klientow = []
    for klient in klienci:
        lista_klientow.append(klient.id)

    return lista_klientow


def pozostala_kolejka(kasy):
    for kasa in kasy:
        print("Kasa ", kasa.id, ": ", end='')
        for klient in kasa.przydzieleni_klienci:
            print(klient.id, " ", end='')
        print()
