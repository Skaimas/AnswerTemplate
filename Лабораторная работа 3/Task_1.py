import numpy as np


def product_list(n_list, product_n):
    k = 0
    for i in range(len(n_list)):
        if n_list[i] == product_n:
            return i

        k += 1

        if k == len(n_list) + 1:
            return "None"


g_list = np.array(["Сосиска в тесте", "Бутерброд", "Смаженка", "Компот", "Сладкий чай", "Булочка с маком", "Самса"])
product_g1 = "Компот"
product_g2 = "Хотдог"

ask1 = product_list(g_list, product_g1)
ask2 = product_list(g_list, product_g2)

print(ask1, ask2, sep="\n")
