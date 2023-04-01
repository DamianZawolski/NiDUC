from klienci import *
from kasy import *


def przypisz_klientow_do_kas(kasy, klienci_nieobsluzeni, klienci_obslugiwani):
    if klienci_nieobsluzeni:
        for kasa in kasy:
            if kasa.obslugiwany_klient is None:
                if klienci_nieobsluzeni:
                    kasa.obslugiwany_klient = klienci_nieobsluzeni[0]
                    klienci_obslugiwani.append(klienci_nieobsluzeni[0])
                    klienci_nieobsluzeni.remove(klienci_nieobsluzeni[0])


    return kasy, klienci_nieobsluzeni, klienci_obslugiwani


def aktualizuj_czas_obslugi(klienci_obslugiwani):
    for klient in klienci_obslugiwani:
        klient.zmniejsz_czas_obslugi()

    return klienci_obslugiwani


def sprawdz_czy_obsluzeni(kasy, klienci_obslugiwani, klienci_obsluzeni):
    for klient in klienci_obslugiwani:
        if klient.czas_obslugi <= 0:
            klienci_obsluzeni.append(klient)
            klienci_obslugiwani.remove(klient)
            for kasa in kasy:
                if kasa.obslugiwany_klient == klient:
                    kasa.obslugiwany_klient = None


def symulacja(kasy, klienci):
    klienci_nieobsluzeni = []
    klienci_obslugiwani = []
    klienci_obsluzeni = []
    for klient in klienci:
        klienci_nieobsluzeni.append(klient)
    czas_obslugi = 0
    while klienci_nieobsluzeni or klienci_obslugiwani:
        czas_obslugi += 1
        kasy, klienci_nieobsluzeni, klienci_obslugiwani = przypisz_klientow_do_kas(kasy, klienci_nieobsluzeni,
                                                                                   klienci_obslugiwani)
        wyswietl_kasy(kasy)
        wyswietl_klientow(klienci)
        aktualizuj_czas_obslugi(klienci_obslugiwani)
        sprawdz_czy_obsluzeni(kasy, klienci_obslugiwani, klienci_obsluzeni)

    print(f"Wszyscy klienci zostali obsłużeni w czasie {czas_obslugi}")
    wyswietl_klientow(klienci_obsluzeni)
