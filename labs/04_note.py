note = None
while note == None:
    value=input("Geben sie Ihre Note ein: ")
    try:
        note = int(value)
    except:
        print("keine ganze Zahl eingegeben")
        continue
    if note > 6 or note < 1:
        print("Note >6 oder <1")
        note = None

if note == 6:
    print("Note 6: sehr gut")
elif note == 5:
    print("Note 5: gut")
elif note == 4:
    print("Note 4: genügend")
else:
    print("Note ungenügend")
    