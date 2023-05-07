import random


class Klienci:
    # klasa którą tworzymy obiekty klientów
    liczba_id = 0

    def __init__(self, czas_obslugi=100):
        self.id = Klienci.liczba_id
        self.czas_obslugi = czas_obslugi
        self.obslugiwany_przez_kase = None
        Klienci.liczba_id += 1

    def wyswietl_informacje(self):
        if self.obslugiwany_przez_kase:
            print(f"Id: {self.id}   |   Czas obsługi: {self.czas_obslugi}   |   Obsługiwany przez kasę: "
                  f"{self.obslugiwany_przez_kase.id} ")
            return (f"[Id: {self.id} | Czas obsługi: {self.czas_obslugi} | Obsługiwany przez kasę: "
                    f"{self.obslugiwany_przez_kase.id} ")
        else:
            print(f"Id: {self.id}   |   Czas obsługi: {self.czas_obslugi}   |   Obsługiwany przez kasę: "
                  f"{self.obslugiwany_przez_kase} ")
            return (f"[Id: {self.id} | Czas obsługi: {self.czas_obslugi} | Obsługiwany przez kasę: "
                    f"{self.obslugiwany_przez_kase} ")

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
    stan_klientow = ""
    for elem in klienci:
        stan_klientow += str(elem.wyswietl_informacje())
    print("-----------------")
    return stan_klientow