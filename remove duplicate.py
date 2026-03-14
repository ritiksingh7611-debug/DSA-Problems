arr = [1, 2, 3, 2, 4, 1, 5]

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print("Array after removing duplicates:", unique)