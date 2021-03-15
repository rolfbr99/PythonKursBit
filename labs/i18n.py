di={"de":"Guten Morgen",
    "fr":"Bon jour",
    "it":"Buongiorno",
    "en":"Good morning"
}

keys=list(di.keys())
msg="Wählen sie eine Sprache "+str(keys)+": "
key=input(msg)
key=key if key in di.keys() else "en"
print(di[key])