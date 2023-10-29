import numpy as np


def find_common_participants(list1, list2):
    mid_group = np.array([])
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                mid_group = np.append(mid_group, list1[i])

    mid_group = sorted(mid_group)

    for i in range(len(mid_group)):
        print(mid_group[i], end="")
        if i + 1 != len(mid_group):
            print(",", end="")


group1 = np.array(["Петров", "Устинов", "Яковлева", "Баранов", "Макеева"])
group2 = np.array(["Макеева", "Борисов", "Горохов", "Баранов", "Иванов", "Яковлева", "Козлов"])

find_common_participants(group1, group2)