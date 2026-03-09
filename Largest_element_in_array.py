arr = [12, 45, 7, 89, 34]

largest = arr[0]

for i in range(1, 5):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element is:", largest)