import mergesort

A = []

num = int(input("Enter the number of elements in sequence"))

for y in range(0, num):
    A.append(int(input()))

A = mergesort.merge(A)
print(A)


def binary_search(arr, x):
    mid = (0 + len(arr)) // 2

    if arr[mid] == x:
        return True
    elif mid == 0:
        return False
    elif arr[mid] > x:
        return binary_search(arr[:mid], x)
    elif arr[mid] < x:
        return binary_search(arr[mid:], x)


while True:
    try:
        find = int(input("Enter number to be searched : (or other key to exit)"))
        print(binary_search(A, find))

    except ValueError:
        print("Thank you!")
        break
