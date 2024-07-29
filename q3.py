def merging_Dict(*args):
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result

def common_keys(*args):
    if not args:
        return set()
    common = set(args[0].keys())
    for dictionary in args[1:]:
        common.intersection_update(dictionary.keys())
    return common

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted

def common_key_value_pairs(*args):
    if not args:
        return {}
    common_pairs = args[0].items()
    for dictionary in args[1:]:
        common_pairs &= dictionary.items()
    return dict(common_pairs)

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 4, 'd': 5}
    dict3 = {'b': 2, 'c': 3, 'e': 6}

    merged_dict = merging_Dict(dict1, dict2, dict3)
    print(f"Merged Dictionary: {merged_dict}")

    common_keys_result = common_keys(dict1, dict2, dict3)
    print(f"Common Keys: {common_keys_result}")

    inverted_dict = invert_dict({'a': 1, 'b': 2, 'c': 1})
    print(f"Inverted Dictionary: {inverted_dict}")

    common_kv_pairs = common_key_value_pairs(dict1, dict2, dict3)
    print(f"Common Key-Value Pairs: {common_kv_pairs}")

'''
Merged Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}
Common Keys: {'c', 'b'}
Inverted Dictionary: {1: ['a', 'c'], 2: ['b']}
Common Key-Value Pairs: {'b': 2}
'''
