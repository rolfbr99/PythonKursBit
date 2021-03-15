lst=[]
inp = None
while inp != "x":
    inp=input("Geben Sie bitte einen Integer ein oder 'x' um die Eingabe zu beenden: ")
    if inp == "x":
        continue
    try:
        value=int(inp)
    except:
        continue
    lst.append(value)

print(lst)