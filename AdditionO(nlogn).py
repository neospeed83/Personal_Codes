import mergesort
import BinarySearchIndex

A = mergesort.inp()
A = mergesort.merge(A)  # Sorting the set

find = int(input("Enter the number to be searched :"))
res = BinarySearchIndex.binary_search(A, find, 0)
print("element found at index : ")
print(res)

