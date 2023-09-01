import random as rd


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


val = []
for _ in range(0, 11):
    val.append(rd.randint(0, 1000))

print(f"Original array is {val}")
bubbleSort(val)
print(f"Sorted array is: {val}")
