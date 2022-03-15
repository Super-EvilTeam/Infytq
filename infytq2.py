A=input()
d=[]
l=[]
h=''
r=[]
o=[]
for i in range(len(A)):
    if A[i]=="l" or A[i]=='L':
        l.append(A[i])
    if A[i] == "d" or A[i] == 'D':
        d.append(A[i])
    if A[i] == "r" or A[i] == 'R':
        r.append(A[i])
    if A[i] == "o" or A[i] == 'O':
        o.append(A[i])
    if i==int(len(A)-1):
        d.sort()
        l.sort()
        r.sort()
        o.sort()
print(d,l,r,o)