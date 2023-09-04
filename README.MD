# Applies a given function to the values of a nested dictionary

## Tested against Windows 10 / Python 3.10 / Anaconda

## pip install functionapplydict

```python
apply_function_dict(d: dict, fu=lambda keys, item, d: item):
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
```



```python
apply_function_dict_deep(d: dict, fu=lambda keys, item, d: item):
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


```