from random import random
values = [random() for _ in range(20)]
searchValue = random()
# Sort the list of random values
values.sort()
print("Sorted values:", values)
print("Search value:", searchValue)
# Find the first value that is greater than or equal to the search value
for index, value in enumerate(values):
    if value >= searchValue:
        print("First matching index:", index)
        break
else:
    print("No value is greater than or equal to the search value")