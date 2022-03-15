a=input()
b=[]
c=[]
for i in range(len(a)):
    if a[i].isalnum():
        b.append(a[i])
    elif not a[i].isalnum():
        c.append(a[i])
        c.append(i)
d=b[::-1]
for i in range(len(c)):
    if str(c[i]) in a:
        d.insert(c[i+1],c[i])
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
print(listToString(d))