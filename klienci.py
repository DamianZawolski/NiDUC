import random


class Klienci:
    # klasa którą tworzymy obiekty klientów
    liczba_id = 0

    def __init__(self, czas_obslugi=100):
        self.id = Klienci.liczba_id
        self.czas_obslugi = czas_obslugi
        Klienci.liczba_id += 1
        self.w_trakcie_obslugi = False

    def wyswietl_informacje(self):
            print(f"Id: {self.id}   |   Czas obsługi: {self.czas_obslugi}   |"
              f"    W trakcie obsługi: {self.w_trakcie_obslugi}")

    def zmniejsz_czas_obslugi(self):
        self.czas_obslugi -= 1


def utworz_losowych_klientow(liczba_klientow, maksymalny_czas_obslugi):
    # funkcja tworząca wybraną ilość klientów o losowych czasie obsługi
    lista_klientow = []
    for i in range(liczba_klientow):
        lista_klientow.append(Klienci(random.randint(1, maksymalny_czas_obslugi)))

    return lista_klientow


def dodaj_nowych_losowych_klientow(lista_klientow, maksymalny_czas_obslugi, liczba_klientow):
    for i in range(liczba_klientow):
        lista_klientow.append(Klienci(random.randint(1, maksymalny_czas_obslugi)))

    return lista_klientow


def dodaj_klienta(lista_klientow, maksymalny_czas_obslugi):
    lista_klientow.append(Klienci(maksymalny_czas_obslugi))
    return lista_klientow


def wyswietl_klientow(klienci):
    print("-----------------")
    print("Klienci")
    for elem in klienci:
        elem.wyswietl_informacje()
    print("-----------------")
