A = []
num = int(input("Enter the total number of elements :"))

for i in range(0, num):
    A.append(int(input()))

print(A)


for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] < key:                #just reversed the sign
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

print(A)
