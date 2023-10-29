import numpy as np


def count_letters(text):
    text2 = text.lower()
    bok_letters = np.array([])
    bok_count = np.array([[]])
    for lett in text2:
        if not lett.isalpha():
            continue
        bok_letters = np.append(bok_letters, lett)
    bok_letters = list(set(bok_letters))
    bok_letters = sorted(bok_letters)

    for i in bok_letters:
        CL = 0
        for lett in text2:
            if i == lett:
                CL += 1
        bok_count = np.append(bok_count, CL)

    return bok_letters, bok_count


def calculate_frequency(letters, count, CL):
    for i in range(len(count)):
        chastota = count[i] / CL
        print(f"{letters[i]}: {round(chastota, 2)}")


text = ("Наступила зима, ударили морозы, выпал пушистый снег. Река покрылась толстым слоем льда, "
        "ветви деревьев наклонились из-за тяжести снежного покрова. Повсюду раскинулось блестящее "
        "снежное покрывало. Его сияние напоминает блеск драгоценных камней. Воздух пахнет морозной "
        "свежестью и необыкновенно бодрит. Зимний пейзаж восхищает своим великолепием. "
        "рудно оторвать взгляд от такой красоты.")

CL = 0
for i in text:
    if not i.isalpha():
        continue
    CL += 1

letters, count = count_letters(text)
calculate_frequency(letters, count, CL)