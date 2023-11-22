import numpy as np


def product(list_, object_):
    k = -1
    for i in range(len(list_)):
        if list_[i] == object_:
            return i
        k += 1
        if k == len(list_):
            return None


items_list = np.array(['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'])

for find_item in ['банан', 'груша', 'персик']:
    index_item = product(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
        
