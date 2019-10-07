A = []

num = int(input("Enter the total number of elements - "))

for i in range(0, num):
    element = int(input())
    A.append(element)

print(A)

for j in range(0, len(A)-1):
    minI = j  # assume first element is min
    for k in range(j, len(A)):  # find the min index
        if A[minI] > A[k]:
            minI = k
    temp = A[j]  # Swap minimum with cursor j
    A[j] = A[minI]
    A[minI] = temp

print(A)
