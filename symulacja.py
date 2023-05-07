from klienci import *
from kasy import *
from time import sleep
from animacja import *


def sprawdz_uszkodzenia(kasy, minimalny_czas_awarii, maksymalny_czas_awarii):
    for kasa in kasy:
        if not kasa.uszkodzona:
            losowa = random.randint(0, 1000) / 1000
            if losowa > kasa.bezawaryjnosc:
                kasa.uszkodzona = True
                kasa.czas_naprawy = random.randint(minimalny_czas_awarii, maksymalny_czas_awarii)
        else:
            kasa.czas_naprawy -= 1
            if kasa.czas_naprawy == 0:
                kasa.uszkodzona = False


def przypisz_klientow_do_kas(kasy, klienci_nieobsluzeni, klienci_obslugiwani):
    if klienci_nieobsluzeni:
        for kasa in kasy:
            if kasa.obslugiwany_klient is None:
                if klienci_nieobsluzeni:
                    kasa.obslugiwany_klient = klienci_nieobsluzeni[0]
                    klienci_nieobsluzeni[0].obslugiwany_przez_kase = kasa
                    klienci_obslugiwani.append(klienci_nieobsluzeni[0])
                    klienci_nieobsluzeni.remove(klienci_nieobsluzeni[0])

    return kasy, klienci_nieobsluzeni, klienci_obslugiwani


def przypisz_klientow_do_kas_z_kolejki(kasy, klienci_nieobsluzeni, klienci_obslugiwani):
    if klienci_nieobsluzeni:
        for kasa in kasy:
            if kasa.obslugiwany_klient is None:
                print(f"Klienci nieobsłużeni {klienci_nieobsluzeni}")
                print(f"kasa przydzieleni klienci {kasa.przydzieleni_klienci}")
                if klienci_nieobsluzeni and len(kasa.przydzieleni_klienci) > 0:
                    kasa.obslugiwany_klient = kasa.przydzieleni_klienci[0]
                    kasa.przydzieleni_klienci[0].obslugiwany_przez_kase = kasa
                    klienci_obslugiwani.append(kasa.przydzieleni_klienci[0])
                    klienci_nieobsluzeni.remove(kasa.przydzieleni_klienci[0])
                    kasa.przydzieleni_klienci.pop(0)

    return kasy, klienci_nieobsluzeni, klienci_obslugiwani


def aktualizuj_czas_obslugi(klienci_obslugiwani):
    for klient in klienci_obslugiwani:
        if not klient.obslugiwany_przez_kase.uszkodzona:
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


def przydziel_do_kas(kasy, klienci_nieobsluzeni):
    for klient in klienci_nieobsluzeni:
        czas_obslugi = 999999999999999
        for kasa in kasy:
            if kasa.zwroc_laczny_czas_obslugi_klientow() < czas_obslugi:
                wybrana_kasa = kasa
                czas_obslugi = kasa.zwroc_laczny_czas_obslugi_klientow()
        wybrana_kasa.przydzieleni_klienci.append(klient)


def symulacja(kasy, klienci, opoznienie, minimalny_czas_awarii, maksymalny_czas_awarii, tryb_kolejkowy):
    kasy_kopia = []
    for kasa in kasy:
        kasy_kopia.append(kasa)
    klienci_kopia = []
    for klient in klienci:
        klienci_kopia.append(klient)
    klienci_nieobsluzeni = []
    klienci_obslugiwani = []
    klienci_obsluzeni = []
    czas_obslugi = 0
    plik = open("przebieg_symulacji.txt", "w")
    iteracja = 0
    dane_do_animacji = []
    opoznienia_iteracja = 0
    for klient in klienci:
        klienci_nieobsluzeni.append(klient)

    if tryb_kolejkowy:
        przydziel_do_kas(kasy, klienci_nieobsluzeni)
        while klienci_nieobsluzeni or klienci_obslugiwani:
            sleep(opoznienie)
            iteracja += 1
            czas_obslugi += 1
            kasy, klienci_nieobsluzeni, klienci_obslugiwani = przypisz_klientow_do_kas_z_kolejki(kasy,
                                                                                                 klienci_nieobsluzeni,
                                                                                                 klienci_obslugiwani)
            stan_kas = wyswietl_kasy(kasy)
            stan_klientow = wyswietl_klientow(klienci)
            aktualizuj_czas_obslugi(klienci_obslugiwani)

            sprawdz_czy_obsluzeni(kasy, klienci_obslugiwani, klienci_obsluzeni)
            sprawdz_uszkodzenia(kasy, minimalny_czas_awarii, maksymalny_czas_awarii)
            klienci_iteracja = zwroc_obslugiwanych_klientow(klienci_obslugiwani)
            animacja_iteracja = informacje_do_animacji(kasy_kopia, klienci_kopia)
            uszkodzenia_iteracja = stan_uszkodzen(kasy_kopia)
            opoznienia_iteracja += dodaj_opoznienia(kasy_kopia)
            dane_do_animacji.append([uszkodzenia_iteracja, animacja_iteracja, opoznienia_iteracja, klienci_iteracja])
            plik.write(f"Iteracja {str(iteracja)} Kasy: {str(stan_kas)}     Klienci {str(stan_klientow)}\n")
            print("Pozostała kolejka w kasach")
            pozostala_kolejka(kasy)
    else:

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
            sprawdz_uszkodzenia(kasy, minimalny_czas_awarii, maksymalny_czas_awarii)
            klienci_iteracja = zwroc_obslugiwanych_klientow(klienci_obslugiwani)
            animacja_iteracja = informacje_do_animacji(kasy_kopia, klienci_kopia)
            uszkodzenia_iteracja = stan_uszkodzen(kasy_kopia)
            opoznienia_iteracja += dodaj_opoznienia(kasy_kopia)
            dane_do_animacji.append([uszkodzenia_iteracja, animacja_iteracja, opoznienia_iteracja, klienci_iteracja])
            plik.write(f"Iteracja {str(iteracja)} Kasy: {str(stan_kas)}     Klienci {str(stan_klientow)}\n")
    print(f"Wszyscy klienci zostali obsłużeni w czasie {czas_obslugi}")
    plik.write(f"Wszyscy klienci zostali obsłużeni w czasie {czas_obslugi}")
    plik.close()
    wyswietl_klientow(klienci_obsluzeni)
    animuj(dane_do_animacji, kasy_kopia, czas_obslugi)
