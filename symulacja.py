from klienci import *
from kasy import *
from time import sleep
from animacja import *


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


def symulacja(kasy, klienci, opoznienie):
    kasy_kopia = []
    for kasa in kasy:
        kasy_kopia.append(kasa)
    klienci_kopia = []
    for klient in klienci:
        klienci_kopia.append(klient)

    klienci_nieobsluzeni = []
    klienci_obslugiwani = []
    klienci_obsluzeni = []
    for klient in klienci:
        klienci_nieobsluzeni.append(klient)
    czas_obslugi = 0
    plik = open("przebieg_symulacji.txt", "w")
    iteracja = 0
    dane_do_animacji = []
    while klienci_nieobsluzeni or klienci_obslugiwani:
        sleep(opoznienie)
        iteracja += 1
        czas_obslugi += 1
        kasy, klienci_nieobsluzeni, klienci_obslugiwani = przypisz_klientow_do_kas(kasy, klienci_nieobsluzeni,
                                                                                   klienci_obslugiwani)
        stan_kas = wyswietl_kasy(kasy)
        stan_klientow = wyswietl_klientow(klienci)
        aktualizuj_czas_obslugi(klienci_obslugiwani)
        sprawdz_czy_obsluzeni(kasy, klienci_obslugiwani, klienci_obsluzeni)
        animacja_iteracja = informacje_do_animacji(kasy_kopia, klienci_kopia)
        dane_do_animacji.append([iteracja, animacja_iteracja])
        plik.write(f"Iteracja {str(iteracja)} Kasy: {str(stan_kas)}     Klienci {str(stan_klientow)}\n")
    print(f"Wszyscy klienci zostali obsłużeni w czasie {czas_obslugi}")
    plik.write(f"Wszyscy klienci zostali obsłużeni w czasie {czas_obslugi}")
    plik.close()
    wyswietl_klientow(klienci_obsluzeni)
    animuj(dane_do_animacji, kasy_kopia, czas_obslugi)
