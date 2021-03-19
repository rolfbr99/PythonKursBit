def max(*args):
    lst=list(locals()["args"])
    lst.sort(reverse=True)
    return lst[0]

print(max(1,10,3))
print(max(3,2))
print(max(30,10,50,80,10))