from funkcje import *

liczba_kas = 10
kasa1 = Kasa(1)
print(kasa1.wyswietl_cechy())
kasy = utworz_losowe_kasy(liczba_kas)
wyswietl_kasy(kasy)
kasy = dodaj_nowe_losowe_kasy(kasy, 5)
wyswietl_kasy(kasy)
kasy = utworz_po_jednej_kasie_z_kategorii()
wyswietl_kasy(kasy)
kasy = dodaj_kase(kasy, 1)
wyswietl_kasy(kasy)
