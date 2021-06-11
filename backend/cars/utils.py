import collections
from fuzzywuzzy import process, fuzz


def get_key(d, value):
    """
    :param d: dict for searching
    :param value: the value by which we are looking for the key
    :return: the key that was searched for by value
    """
    for k, v in d.items():
        if v == value:
            return k


def serialize(objects):
    """
    :param objects: object should define to_dict method
    :return: list of to_dict on each object
    """
    res = []
    error = False
    if isinstance(objects, collections.Iterable):
        for object in objects:
            try:
                res.append(object.serialize())
            except Exception as e:
                error = e
                print(f"Serialize error: {e}")
                pass
    elif objects:
        res.append(objects.serialize())
    return res


def castom_paginate(objects, count_obj_on_page):
    cars_list = []
    pack = []
    count_page = 1
    len_ = len(objects)
    if isinstance(objects, collections.Iterable):
        if len_ % count_obj_on_page == 0:
            count_page = (len_ // count_obj_on_page)
        else:
            count_page = (len_ // count_obj_on_page) + 1
        if count_page > 1:  # 4
            num = 0
            num_2 = count_obj_on_page
            for _ in range(count_page):
                cars_list.append(serialize(objects[num:num_2]))
                num += count_obj_on_page
                num_2 += count_obj_on_page
                if num_2 > len_:
                    num_2 = len_ - (len_ - (num_2 - count_obj_on_page))
                    cars_list.append(serialize(objects[num_2:len_]))
                    pass
        else:
            cars_list.append(serialize(objects))
    elif objects:
        cars_list.append(objects.serialize())
    else:
        pass
    # for obj in objects:
    #     pack.append(obj)
    #     if len(pack) == count_page:
    #         cars_list.append(serialize(pack))
    #         pack = []

    print('!!!!!!!!!!!!!!!!!!!!castom_paginate_return!!!!!!!!!!!!!!!!!', cars_list)
    return cars_list


def smart_search_def(collection_objects, collection_data, data):
    list_res = process.extract(data, collection_data, limit=None)
    ids_ = []
    result = []
    for elem in list_res:
        if elem[1] > 57:
            ids_.append(elem[2])
    print('IDS___', ids_)
    for id in ids_:
        result += collection_objects.filter(id=id)
    print('RESULT__________________________________', result)
    return result
