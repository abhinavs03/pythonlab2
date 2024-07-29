import module_SetOperations as so

s = {1, 2, 3}
so.add_element(s, 4)
print(f"Set after adding 4: {s}")
so.add_element(s, 4)
print(f"Set after trying to add 4 again: {s}")

so.remove_element(s, 3)
print(f"Set after removing 3: {s}")
so.remove_element(s, 3)
print(f"Set after trying to remove 3 again: {s}")

s1 = {1, 2, 3}
s2 = {3, 4, 5}
union, intersection = so.union_and_intersection(s1, s2)
print(f"Union of {s1} and {s2}: {union}")
print(f"Intersection of {s1} and {s2}: {intersection}")

diff = so.difference(s1, s2)
print(f"Difference of {s1} - {s2}: {diff}")

subset_result = so.is_subset({1, 2}, {1, 2, 3})
print(f"Is {1, 2} a subset of {1, 2, 3}?: {subset_result}")

length = so.set_length({1, 2, 3, 4})
print(f"Length of the set {1, 2, 3, 4} is: {length}")

sym_diff = so.symmetric_difference({1, 2, 3}, {3, 4, 5})
print(f"Symmetric difference of {1, 2, 3} and {3, 4, 5}: {sym_diff}")

power_set_result = so.power_set({1, 2})
print(f"Power set of {1, 2}: {power_set_result}")

unique_subsets_result = so.unique_subsets({1, 2})
print(f"Unique subsets of {1, 2}: {unique_subsets_result}")


'''
Set after adding 4: {1, 2, 3, 4}
Set after trying to add 4 again: {1, 2, 3, 4}
Set after removing 3: {1, 2, 4}
Set after trying to remove 3 again: {1, 2, 4}
Union of {1, 2, 3} and {3, 4, 5}: {1, 2, 3, 4, 5}
Intersection of {1, 2, 3} and {3, 4, 5}: {3}
Difference of {1, 2, 3} - {3, 4, 5}: {1, 2}
Is (1, 2) a subset of (1, 2, 3)?: True
Length of the set (1, 2, 3, 4) is: 4
Symmetric difference of (1, 2, 3) and (3, 4, 5): {1, 2, 4, 5}
Power set of (1, 2): [(), (1,), (2,), (1, 2)]
Unique subsets of (1, 2): [(1,), (1, 2), (), (2,)]
'''
