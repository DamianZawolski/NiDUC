from funkcje import *

liczba_kas = 10
kasa1 = Kasa(1)
print(kasa1.wyswietl_cechy())
kasy = utworz_losowe_kasy(liczba_kas)
wyswietl_kasy(kasy)
kasy = dodaj_nowe_losowe_kasy(kasy, 5)
wyswietl_kasy(kasy)
