lst = []


try:
    n = int(input("Enter the number of elements in sequence"))

    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    print(lst)

    for j in range(1, len(lst)):
        key = lst[j]
        i = j-1
        while i >= 0 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i - 1
        lst[i+1] = key

    print("O/p")
    print(lst)

except:
    print("Something went wrong")


