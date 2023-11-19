dict_ = {
    "global_count": 0,
    "unique_count": 0
}

# Список ID пользователей посещавших сайт
global_list = [3234, 2645, 2146, 662, 3234, 124, 12465, 3234, 6562, 124, 1235, 2345, 2461, 15754, 662, 3465, 12465]

# Список уникальных ID
unique_list = list(set(global_list))

dict_["global_count"] = len(global_list)

dict_["unique_count"] = len(unique_list)

print(dict_)
