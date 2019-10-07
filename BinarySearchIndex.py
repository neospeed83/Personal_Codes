from builtins import ValueError
import mergesort


def binary_search(arr, key, index):
    mid = len(arr) // 2

    if arr[mid] == key:
        return mid + index
    if len(arr) == 1:
        return -1
    elif arr[mid] > key:
        return binary_search(arr[:mid], key, index)
    elif arr[mid] < key:
        return binary_search(arr[mid:], key, mid + index)


if __name__ == "__main__":
    A = mergesort.inp()
    A = mergesort.merge(A)
    print(A)

    while True:
        try:
            find = int(input("Enter the number to be searched : "))
            result = binary_search(A, find, 0)
            if result != -1:
                print("Element found at index ")
                print(result)
            else:
                print("The entered number does not exist in array")
        except ValueError:
            print("Thank you")
            break
