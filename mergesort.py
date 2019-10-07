def inp():
    A = []

    num = int(input("Enter the number of elements in sequence"))

    for y in range(0, num):
        A.append(int(input()))

    return A


# Merge Sort

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge(L)
        merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):  # Merge
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):  # Checking if any element was left
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def printlist(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    A = inp()
    print("The input array is \n")
    printlist(A)
    merge(A)
    print("The sorted array is \n")
    printlist(A)
