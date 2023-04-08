import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import seaborn as sns
import numpy as np

mpl.rcParams['animation.ffmpeg_path'] = "ffmpeg.exe"

kasy = []
fig = plt.figure(figsize=(7, 5))


def animacja(i):
    fig.clear()
    axes = fig.add_subplot(1, 1, 1)
    axes.set_xlim(0, 10)
    plt.style.use("seaborn")
    axes.set_xlabel("Pozostaly czas pracy")
    axes.set_ylabel("Indeks kasy")
    dane = []
    tickdic = {}
    iteracja = 0
    for elem in kasy:
        dane.append(elem[i])
        tickdic[iteracja] = elem[i]
        iteracja += 1
    kolory = list(reversed(sns.color_palette("afmhot", 4).as_hex()))
    plt.barh(range(iteracja), dane, color=kolory)
    tcks = [i[0] for i in tickdic.items()]

    plt.title("Symulacja kasy sklepowej\nIteracja: {} ".format(i + 1), color="black")
    plt.yticks(np.arange(iteracja), tcks)


def animuj(dane_do_animacji, kasy_kopia, czas_obslugi):
    for _ in kasy_kopia:
        kasy.append([])
    for i in range(len(dane_do_animacji)):
        dane = dane_do_animacji[i][1]
        for elem in dane:
            kasy[elem['id_kasy']].append(elem['czas_obslugi'])

    animacja_wyjsciowa = FuncAnimation(fig, animacja, interval=1, save_count=czas_obslugi)
    plik = r"animacja_symulacji.mp4"
    gif = FFMpegWriter(fps=1)
    animacja_wyjsciowa.save(plik, writer=gif)
