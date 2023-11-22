import numpy as np


def find_common_participants(str1, str2, sep_=","):
    st1 = srtok(str1)
    st2 = srtok(str2)
    s = np.array([])
    for i in st1:
        for j in st2:
            if i == j:
                s = np.append(s, i)
    print(sorted(s))


def srtok(str):
    s = np.array([])
    s1 = ""
    for i in str:
        if not i == '|':
            s1 += i
        else:
            s = np.append(s, s1)
            s1 = ""
    s = np.append(s, s1)
    return s


participants_first_group = "Сидоров|Петров|Иванов"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, ";")
