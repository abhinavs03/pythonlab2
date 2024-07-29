import module_ListFunction as lf

l1 = [i for i in range(10)]          
l2 = [i**2 for i in range(10)]       
l3 = [i for i in range(20) if i % 2 == 0]  
l4 = [i for i in range(1, 11) if i % 2 != 0]  
l5 = [i for i in range(-5, 6)]       

print(f"List1: {l1}")
print(f"Max of List1: {lf.find_max(l1)}")
print(f"Min of List1: {lf.find_min(l1)}")
print(f"Sum of List1: {lf.calculate_sum(l1)}")
print(f"Average of List1: {lf.calculate_average(l1)}")
print(f"Median of List1: {lf.calculate_median(l1)}")

print(f"\nList2: {l2}")
print(f"Max of List2: {lf.find_max(l2)}")
print(f"Min of List2: {lf.find_min(l2)}")
print(f"Sum of List2: {lf.calculate_sum(l2)}")
print(f"Average of List2: {lf.calculate_average(l2)}")
print(f"Median of List2: {lf.calculate_median(l2)}")

print(f"\nList3: {l3}")
print(f"Max of List3: {lf.find_max(l3)}")
print(f"Min of List3: {lf.find_min(l3)}")
print(f"Sum of List3: {lf.calculate_sum(l3)}")
print(f"Average of List3: {lf.calculate_average(l3)}")
print(f"Median of List3: {lf.calculate_median(l3)}")

print(f"\nList4: {l4}")
print(f"Max of List4: {lf.find_max(l4)}")
print(f"Min of List4: {lf.find_min(l4)}")
print(f"Sum of List4: {lf.calculate_sum(l4)}")
print(f"Average of List4: {lf.calculate_average(l4)}")
print(f"Median of List4: {lf.calculate_median(l4)}")

print(f"\nList5: {l5}")
print(f"Max of List5: {lf.find_max(l5)}")
print(f"Min of List5: {lf.find_min(l5)}")
print(f"Sum of List5: {lf.calculate_sum(l5)}")
print(f"Average of List5: {lf.calculate_average(l5)}")
print(f"Median of List5: {lf.calculate_median(l5)}")


'''
List1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Max of List1: 9
Min of List1: 0
Sum of List1: 45
Average of List1: 4.5
Median of List1: 4.5

List2: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Max of List2: 81
Min of List2: 0
Sum of List2: 285
Average of List2: 28.5
Median of List2: 20.5

List3: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
Max of List3: 18
Min of List3: 0
Sum of List3: 90
Average of List3: 9.0
Median of List3: 9.0

List4: [1, 3, 5, 7, 9]
Max of List4: 9
Min of List4: 1
Sum of List4: 25
Average of List4: 5.0
Median of List4: 5

List5: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Max of List5: 5
Min of List5: -5
Sum of List5: 0
Average of List5: 0.0
Median of List5: 0
'''
