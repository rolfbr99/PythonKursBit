articles = {
    11: {'name': 'Bildschirm Belinea X3', 'price': 499.5},
    12: {'name': 'PC Tastatur Swiss German', 'price': 35.0},
    13: {'name': 'Logitec Maus', 'price': 17.25},
    14: {'name': 'USB Hub', 'price': 25.7},
    15: {'name': 'Lautsprecher X66-12', 'price': 87.9} 
}

for articlekey in articles:
    print("{0:50} {1:>9.2f}".format(articles[articlekey]["name"],articles[articlekey]["price"]))

article=None
for articlekey in articles:
    if article ==None:
        article=articles[articlekey]
        continue
    if articles[articlekey]["price"] < article["price"]:
        article = articles[articlekey]
print(article)


article=None
for articlekey in articles:
    if article ==None:
        article=articles[articlekey]
        continue
    article = articles[articlekey]  if articles[articlekey]["price"] < article["price"]  else article

print(article)

clone=articles
for articlekey in articles:
    x=articles[articlekey]
    x["price"]=x["price"]*0.8
    print("{0:<50} {1:>9.2f}".format(x["name"],x["price"]))
    
for articlekey in clone:
    x=clone[articlekey]
    print("{0:<50} {1:>9.2f}".format(x["name"],x["price"]))



