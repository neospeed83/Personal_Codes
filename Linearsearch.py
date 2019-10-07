A = [3, 4, 9, 5, 8]

v = int(input("Enter the number to be searched\n"))
flag = False

for i in range(0, len(A)):
    if A[i] == v:
        print("your number is at index \"" + str(i) + "\" in list A.")
        flag = True
        break
    elif i == len(A):
        flag = False

if not flag:
    print("Entered number does not belong to list A")