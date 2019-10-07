A = [1, 4, 6, 7, 2, 9]
print(A)
x = int(input("Enter the number : "))


def add(numb):
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == numb:
                print("Two numbers found")
                print(A[i], A[j])
                return

    print("Not Found!")


add(x)
