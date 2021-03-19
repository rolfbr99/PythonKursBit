values  = [7.5, 'Hello', 42, None, 'World', 1.25, 69, 12]
print(values)
inttype=[]
floattype=[]
strtype=[]
for value in values:
    if type(value) is float:
        floattype.append(value)
    elif type(value) is int:
        inttype.append(value)
    elif type(value) is str:
        strtype.append(value)

print(floattype)
print(inttype)
print(strtype)