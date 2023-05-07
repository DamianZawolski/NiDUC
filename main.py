from symulacja import *

liczba_kas = 5
kasy = utworz_losowe_kasy(liczba_kas)
"""
wyswietl_kasy(kasy)
kasy = dodaj_nowe_losowe_kasy(kasy, 5)
wyswietl_kasy(kasy)
kasy = utworz_po_jednej_kasie_z_kategorii()
wyswietl_kasy(kasy)
kasy = dodaj_kase(kasy, 1)
wyswietl_kasy(kasy)
"""

liczba_klientow = 50
maksymalny_czas_obslugi = 5
opoznienie = 0
minimalny_czas_awarii = 5
maksymalny_czas_awarii = 10
klienci = utworz_losowych_klientow(liczba_klientow, maksymalny_czas_obslugi)
tryb_kolejkowy = False
wyswietl_kasy(klienci)
"""
klienci = dodaj_nowych_losowych_klientow(klienci, maksymalny_czas_obslugi, 10)
wyswietl_kasy(klienci)
klienci = dodaj_klienta(klienci, 50)
wyswietl_klientow(klienci)"""

symulacja(kasy, klienci, opoznienie, minimalny_czas_awarii, maksymalny_czas_awarii, tryb_kolejkowy)
