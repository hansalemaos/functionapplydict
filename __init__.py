from deepcopyall import deepcopy
from flatten_any_dict_iterable_or_whatsoever import fla_tu
from multikeyiterdict import MultiKeyIterDict
from isiter import isiter


def apply_function_dict(d: dict, fu=lambda keys, item, d: item):
    """
    Apply a given function to the values of a nested dictionary and return a modified dictionary.

    Parameters:
    - d (dict): The input dictionary to be modified.
    - fu (function): The function to be applied to each value in the dictionary.
        - keys (list): The list of keys leading to the current value.
        - item (any): The current value in the dictionary.
        - d (dict): The input dictionary.

    Returns:
    - dict: A new dictionary with the same structure as the input, but with modified values.

    Example:
        from functionapplydict import apply_function_dict

        child1 = {"name": "Emil", "year": 2004}
        child2 = {"name": "Tobias", "year": 2007}
        child3 = {"name": "Linus", "year": 2011}

        myfamily = {"child1": child1, "child2": child2, "child3": child3}


        def function1(keys, item, d):
            if isinstance(item, int):
                item = item * 8
            return item


        dnew = apply_function_dict(d=myfamily, fu=function1)
        dnew2 = apply_function_dict(d=myfamily, fu=lambda keys, item, d: str(item))

        ditest = {1: {2: [4, 56, 2, 4, 56]}, 2: {24: [4, 56, 2, 4, 56, 444]}}
        dnew3 = apply_function_dict(d=ditest, fu=lambda keys, item, d: sum(item))
        dnew4 = apply_function_dict(d=ditest, fu=lambda keys, item, d: str(item))

        print(dnew)
        print(dnew2)
        print(dnew3)
        print(dnew4)

        # {'child1': {'name': 'Emil', 'year': 16032}, 'child2': {'name': 'Tobias', 'year': 16056}, 'child3': {'name': 'Linus', 'year': 16088}}
        # {'child1': {'name': 'Emil', 'year': '2004'}, 'child2': {'name': 'Tobias', 'year': '2007'}, 'child3': {'name': 'Linus', 'year': '2011'}}
        # {1: {2: 122}, 2: {24: 566}} # sum can be applied to lists
        # {1: {2: '[4, 56, 2, 4, 56]'}, 2: {24: '[4, 56, 2, 4, 56, 444]'}} # the whole list is converted to a string
    """
    d = MultiKeyIterDict(deepcopy(d))
    allreadydone = []
    for item, keys in fla_tu(deepcopy(d)):
        try:
            allkeys = []
            for k in keys:
                try:
                    allkeys.append(k)

                    if allkeys in allreadydone:
                        continue
                    allreadydone.append(allkeys[:-1].copy())
                    t1 = isinstance(d[allkeys[:-1]], dict)
                    t2 = isinstance(d[allkeys], dict)
                    if t1 and not t2:
                        fuo = fu(allkeys, d[allkeys], d)
                        d[allkeys] = fuo
                        continue
                    t3 = isiter(d[allkeys[:-1]])
                    if not t1 and not t2 and t3:
                        d[allkeys[:-1]] = fu(allkeys[:-1], d[allkeys[:-1]], d)

                except Exception:
                    continue
        except Exception:
            continue

    return d.to_dict()


def apply_function_dict_deep(d: dict, fu=lambda keys, item, d: item):
    """
    Apply a given function to the values of a nested dictionary deeply and return a modified dictionary.

    Parameters:
    - d (dict): The input dictionary to be modified.
    - fu (function): The function to be applied to each value in the dictionary.
        - keys (list): The list of keys leading to the current value.
        - item (any): The current value in the dictionary.
        - d (dict): The input dictionary.

    Returns:
    - dict: A new dictionary with the same structure as the input, but with modified values.

    Example:
        from functionapplydict import apply_function_dict_deep
        child1 = {"name": "Emil", "year": 2004}
        child2 = {"name": "Tobias", "year": 2007}
        child3 = {"name": "Linus", "year": 2011}

        myfamily = {"child1": child1, "child2": child2, "child3": child3}


        def function1(keys, item, d):
            if isinstance(item, int):
                item = item * 8
            return item

        dnew = apply_function_dict_deep(d=myfamily, fu=function1)
        dnew2 = apply_function_dict_deep(d=myfamily, fu=lambda keys, item, d: str(item))

        ditest = {1: {2: [4, 56, 2, 4, 56]}, 2: {24: [4, 56, 2, 4, 56, 444]}}
        dnew3 = apply_function_dict_deep(d=ditest, fu=lambda keys, item, d: sum(item))
        dnew4 = apply_function_dict_deep(d=ditest, fu=lambda keys, item, d: str(item))

        print(dnew)
        print(dnew2)
        print(dnew3)
        print(dnew4)

        # {'child1': {'name': 'Emil', 'year': 16032}, 'child2': {'name': 'Tobias', 'year': 16056}, 'child3': {'name': 'Linus', 'year': 16088}}
        # {'child1': {'name': 'Emil', 'year': '2004'}, 'child2': {'name': 'Tobias', 'year': '2007'}, 'child3': {'name': 'Linus', 'year': '2011'}}
        # {1: {2: [4, 56, 2, 4, 56]}, 2: {24: [4, 56, 2, 4, 56, 444]}} # no change, because sum can't be applied to int
        # {1: {2: ['4', '56', '2', '4', '56']}, 2: {24: ['4', '56', '2', '4', '56', '444']}} # each int is converted to a string, but not the whole list


    """
    d = MultiKeyIterDict(deepcopy(d))
    for item, keys in fla_tu(deepcopy(d)):
        try:
            allkeys = list(keys)
            fuo = fu(keys, item, d)
            d[allkeys] = fuo
        except Exception:
            continue
    return d.to_dict()
