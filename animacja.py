import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from qbstyles import mpl_style
import numpy as np

mpl.rcParams['animation.ffmpeg_path'] = "ffmpeg.exe"

kasy = []
uszkodzenia = []
opoznienia = []
klienci_iteracja = []

mpl_style(True)
fig = plt.figure(figsize=(12, 10))


def animacja(i):
    dane = []
    uszkodzenia_iteracja = []
    tickdic = {}
    iteracja = 0
    for elem in kasy:
        dane.append(elem[i])
        tickdic[iteracja] = elem[i]
        iteracja += 1
    for elem in uszkodzenia[i]:
        uszkodzenia_iteracja.append(elem)

    uszkodzone_kasy = []
    for j in range(len(uszkodzenia_iteracja)):
        if uszkodzenia_iteracja[j] == 1:
            uszkodzone_kasy.append(j)
    kolory = []
    for elem in uszkodzenia_iteracja:
        if elem:
            kolory.append('#8b0000')
        else:
            kolory.append('#005000')

    fig.clear()
    axes = fig.add_subplot(1, 1, 1)
    axes.set_xlim(0, 10)
    axes.set_xlabel("Pozostały czas", color="white")
    axes.set_ylabel(f"Indeks kasy")
    plt.barh(range(iteracja), dane, color=kolory)
    tcks = [i[0] for i in tickdic.items()]
    plt.title("Symulacja kasy sklepowej\nIteracja: {} ".format(i + 1)+"\nUszkodzone kasy: {} ".format(uszkodzone_kasy)+"\nObsługiwani klienci: {} ".format(klienci_iteracja[i])+"\nŁączny czas opóźnień: {} ".format(opoznienia[i]), color="white")
    plt.yticks(np.arange(iteracja), tcks)


def animuj(dane_do_animacji, kasy_kopia, czas_obslugi):
    for _ in kasy_kopia:
        kasy.append([])
    for i in range(len(dane_do_animacji)):
        dane_kasy = dane_do_animacji[i][1]
        dane_uszkodzenia = dane_do_animacji[i][0]
        dane_opoznienia = dane_do_animacji[i][2]
        dane_klienci = dane_do_animacji[i][3]
        for elem in dane_kasy:
            kasy[elem['id_kasy']].append(elem['czas_obslugi'])
        uszkodzenia.append(dane_uszkodzenia)
        opoznienia.append(dane_opoznienia)
        klienci_iteracja.append(dane_klienci)
    animacja_wyjsciowa = FuncAnimation(fig, animacja, interval=0.7, save_count=czas_obslugi)
    plik = r"animacja_symulacji.gif"
    gif = PillowWriter(fps=1)
    animacja_wyjsciowa.save(plik, writer=gif)
