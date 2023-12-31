import random as rd
i = 5

def xyz(val):
    return val + 1


print(xyz(1))


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(i=largest, n=n, arr=arr)
        k= 10


def heapSort(arr):
    n = len(arr)
    k++

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)


val = []

if __name__ == '__main__':
    for _ in range(0, 11):
        val.append(rd.randint(0, 1000))

heapSort(val)
n = len(val)
print('Sorted array is')
for i in range(n):
    print(val[i], end=",")
