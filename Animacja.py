import random
import matplotlib.pyplot as plt
from celluloid import Camera

from Osoba_ruchoma import *


def generuj_osoby(a, b):
    for i in range(a):
        temp = []
        for j in range(b):
            temp.append(Osoba(j * a + i))
        osoby.append(temp)


def dodaj_osoby_ruchome(a, b):
    for i in range(a):
        temp = []
        for j in range(b):
            temp.append(Osoba_ruchoma(osoby[i][j], [i, j]))
        osoby_ruchome.append(temp)


def wyswietl_osoby(a, b):
    for i in range(a):
        temp = []
        for j in range(b):
            temp.append(osoby[i][j].info())
        print(temp)


def wyswietl_stan(dane, a, b):
    wynik = []
    for i in range(a):
        temp = []
        for j in range(b):
            if dane[i][j].zdrowy:
                if dane[i][j].ozdrowialy:
                    temp.append(f"O[{dane[i][j].odpornosc}]")
                else:
                    temp.append("Z")
            else:
                temp.append(f"CHORY[{dane[i][j].licznik}]")
        print(temp)
        wynik.append(temp)
    return wynik


def symulacja(a, b, iter, szanse_na_zachorowanie, czas_wyzdrowienia, odpornosc):
    for iter in range(iter):
        chorzy = []
        for i in range(a):
            for j in range(b):
                if osoby[i][j].zdrowy == False:
                    chorzy.append([i, j])
                    osoby[i][j].licznik -= 1
                if osoby[i][j].licznik <= 0 and osoby[i][j].zdrowy == False:
                    osoby[i][j].zdrowy = True
                    osoby[i][j].ozdrowialy = True
                    osoby[i][j].odpornosc = odpornosc
                    osoby[i][j].licznik = 0
                if osoby[i][j].ozdrowialy:
                    osoby[i][j].odpornosc -= 1
                if osoby[i][j].odpornosc <= 0:
                    osoby[i][j].ozdrowialy = False
                    osoby[i][j].odpornosc = 0

        for chory in chorzy:
            if chory[0] != 0:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby[chory[0] - 1][chory[1]].zdrowy == True and osoby[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby[chory[0] - 1][chory[1]].zdrowy = False
                        osoby[chory[0] - 1][chory[1]].licznik = czas_wyzdrowienia

            if chory[0] < a - 1:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby[chory[0] + 1][chory[1]].zdrowy == True and osoby[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby[chory[0] + 1][chory[1]].zdrowy = False
                        osoby[chory[0] + 1][chory[1]].licznik = czas_wyzdrowienia

            if chory[1] != 0:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby[chory[0]][chory[1] - 1].zdrowy == True and osoby[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby[chory[0]][chory[1] - 1].zdrowy = False
                        osoby[chory[0]][chory[1] - 1].licznik = czas_wyzdrowienia

            if chory[1] < b - 1:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby[chory[0]][chory[1] + 1].zdrowy == True and osoby[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby[chory[0]][chory[1] + 1].zdrowy = False
                        osoby[chory[0]][chory[1] + 1].licznik = czas_wyzdrowienia

        print()
        print(f"Iteracja {iter + 1}")
        wynik = wyswietl_stan(osoby, a, b)
        wizualizacja(wynik)

def symulacja_ruchoma(a, b, iter, szanse_na_zachorowanie, czas_wyzdrowienia, odpornosc, ilosc_zamian):
    for iter1 in range(iter):
        osoby2 = []
        for i in range(ilosc_zamian):
            x = random.randint(0, a - 1)
            y = random.randint(0, b - 1)
            x2 = random.randint(0, a - 1)
            y2 = random.randint(0, b - 1)
            for i in range(a):
                for j in range(b):
                    if osoby_ruchome[i][j].pozycja == [x, y]:
                        osoby_ruchome[i][j].pozycja = [x2, y2]

                    elif osoby_ruchome[i][j].pozycja == [x2, y2]:
                        osoby_ruchome[i][j].pozycja = [x, y]
        for i in range(a):
            temp = []
            for j in range(b):
                for k in range(a):
                    for l in range(b):
                        if osoby_ruchome[k][l].pozycja == [i, j]:
                            temp.append(osoby_ruchome[k][l])
                            continue
            osoby2.append(temp)

        chorzy = []

        for i in range(a):
            for j in range(b):
                if osoby2[i][j].zdrowy == False:
                    chorzy.append([i, j])
                    osoby2[i][j].licznik -= 1
                if osoby2[i][j].licznik <= 0 and osoby2[i][j].zdrowy == False:
                    osoby2[i][j].zdrowy = True
                    osoby2[i][j].ozdrowialy = True
                    osoby2[i][j].odpornosc = odpornosc
                    osoby2[i][j].licznik = 0
                if osoby2[i][j].ozdrowialy:
                    osoby2[i][j].odpornosc -= 1
                if osoby2[i][j].odpornosc <= 0:
                    osoby2[i][j].ozdrowialy = False
                    osoby2[i][j].odpornosc = 0

        for chory in chorzy:
            if chory[0] != 0:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby2[chory[0] - 1][chory[1]].zdrowy == True and osoby2[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby2[chory[0] - 1][chory[1]].zdrowy = False
                        osoby2[chory[0] - 1][chory[1]].licznik = czas_wyzdrowienia

            if chory[0] < a - 1:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby2[chory[0] + 1][chory[1]].zdrowy == True and osoby2[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby2[chory[0] + 1][chory[1]].zdrowy = False
                        osoby2[chory[0] + 1][chory[1]].licznik = czas_wyzdrowienia

            if chory[1] != 0:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby2[chory[0]][chory[1] - 1].zdrowy == True and osoby2[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby2[chory[0]][chory[1] - 1].zdrowy = False
                        osoby2[chory[0]][chory[1] - 1].licznik = czas_wyzdrowienia

            if chory[1] < b - 1:
                if (random.randint(0, 10000) / 10000) < szanse_na_zachorowanie:
                    if osoby2[chory[0]][chory[1] + 1].zdrowy == True and osoby2[chory[0] - 1][
                        chory[1]].ozdrowialy == False:
                        osoby2[chory[0]][chory[1] + 1].zdrowy = False
                        osoby2[chory[0]][chory[1] + 1].licznik = czas_wyzdrowienia

        print()
        print(f"Iteracja {iter1 + 1}")
        wynik = wyswietl_stan(osoby2, a, b)
        wizualizacja(wynik)

def wizualizacja(wynik):
    for i in range(len(wynik)):
        for j in range(len(wynik[0])):
            do_wizualizacji[i + j * len(wynik)].append(wynik[i][j])

def kolory1(iteracja):
    kolory = []
    for i in range(len(do_wizualizacji)):
        if do_wizualizacji[i][iteracja][0] == 'Z':
            kolory.append("green")
        elif do_wizualizacji[i][iteracja][0] == 'O':
            kolory.append("yellow")
        else:
            kolory.append("red")
    return kolory

a = 10
b = 30
chorzy = 10
ilosc_iteracji = 50
szanse_na_zachorowanie = 0.2
czas_wyzdrowienia = 7
odpornosc = 14
ilosc_zamian = 50
osoby = []
generuj_osoby(a, b)
rand = []
osoby_ruchome = []
dodaj_osoby_ruchome(a, b)
do_wizualizacji = []
for i in range(a):
    temp = []
    for j in range(b):
        do_wizualizacji.append([])

print(len(do_wizualizacji))
for i in range(chorzy):
    rand.append(random.randint(1, 100))
print(f"Chorzy: {rand}")
for i in range(a):
    for j in range(b):
        if osoby[i][j].id in rand:
            osoby[i][j].zdrowy = False
            osoby[i][j].licznik = czas_wyzdrowienia
for i in range(a):
    for j in range(b):
        if osoby_ruchome[i][j].id.id in rand:
            osoby_ruchome[i][j].zdrowy = False
            osoby_ruchome[i][j].licznik = czas_wyzdrowienia

wyswietl_osoby(a, b)
wyswietl_stan(osoby, a, b)

#symulacja(a, b, ilosc_iteracji, szanse_na_zachorowanie, czas_wyzdrowienia, odpornosc)
symulacja_ruchoma(a, b, ilosc_iteracji, szanse_na_zachorowanie, czas_wyzdrowienia, odpornosc, ilosc_zamian)

ilosc_punktow = a * b

punkty = [[], []]
for i in range(b):
    for j in range(a):
        punkty[0].append(i)
        punkty[1].append(j)
plt.rcParams["figure.figsize"] = (20, 15)
kamera = Camera(plt.figure())
for k in range(ilosc_iteracji):
    kolory = kolory1(k)
    plt.scatter(*punkty, c=kolory, s=1000)
    plt.title(f"Symulacja")
    for l in range(b):
        for m in range(a):
            punkt = m + l * a
            plt.annotate(str(do_wizualizacji[punkt][k]), xy=(l, m), ha='center', va='bottom')
    kamera.snap()

anim = kamera.animate(blit=True, interval=500)
anim.save('symulacja.gif')
plt.show()
