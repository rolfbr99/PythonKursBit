def max (a,b,c=None):
    lst=[]
    lst.append(a)
    lst.append(b)
    if c is not None:
        lst.append(c)
    lst.sort(reverse=True)
    return lst[0]

print(max(1,10,3))
print(max(3,2))
print(max(30,10,50))