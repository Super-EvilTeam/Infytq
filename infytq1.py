A = input()
B = []
C = []


def func2():
    if int(len(B)) == int(max(C)):
        print(B[int(max(C)) - 1])

    if int(len(B)) > int(max(C)):
        print(B[int(max(C)) - 1])

    while int(len(B)) < int(max(C)):
        C.remove(max(C))
        if int(len(B)) == int(max(C)):
            print(B[int(max(C)) - 1])
        elif int(len(B)) > int(max(C)):
            print(B[int(max(C)) - 1])

def func():
    for i in range(len(A)):
        if A[i].isalpha():
            B.append(A[i])
        if A[i].isdigit():
            C.append(A[i])
        if A[i] == ',' or i==int(len(A)-1):
            func2()
            B.clear()
            C.clear()
            continue


func()
