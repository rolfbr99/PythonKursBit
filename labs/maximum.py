def max (a,b,c=None):
    if c is None:
        lst=[a,b]
    else:
        lst=[a,b,c]    
    lst.sort(reverse=True)
    return lst[0]

print(max(1,10,3))
print(max(3,2))
print(max(30,10,50))