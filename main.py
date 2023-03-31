from kasy import *
from klienci import *

liczba_kas = 10
kasy = utworz_losowe_kasy(liczba_kas)
wyswietl_kasy(kasy)
kasy = dodaj_nowe_losowe_kasy(kasy, 5)
wyswietl_kasy(kasy)
kasy = utworz_po_jednej_kasie_z_kategorii()
wyswietl_kasy(kasy)
kasy = dodaj_kase(kasy, 1)
wyswietl_kasy(kasy)

liczba_klientow = 10
maksymalny_czas_obslugi = 20
klienci = utworz_losowych_klientow(liczba_klientow, maksymalny_czas_obslugi)
wyswietl_kasy(klienci)
klienci = dodaj_nowych_losowych_klientow(klienci, maksymalny_czas_obslugi, 10)
wyswietl_kasy(klienci)
klienci = dodaj_klienta(klienci, 50)
wyswietl_klientow(klienci)
