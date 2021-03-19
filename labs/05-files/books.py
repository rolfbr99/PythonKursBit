import csv
csv.register_dialect('semicolon-delimited', delimiter=';')

path="S:/Daten/pythonworkspace/pythonlearn/labs/05-files/"
filein=path+"books.txt"
fileout=path+"books.csv"

with open(filein,"r") as fin:
    lines = fin.read().splitlines()

books = []
book  = []
for line in lines:
    if line.strip() == "":
        books.append(book)
        book = []
    else:
        book.append(line.strip())

books.append(book)

print(books)

titles = books[0]
rows = books[1:]

with open(fileout, "w", newline="") as fout:
    writer = csv.writer(fout, delimiter=";")
    writer.writerow(titles)
    writer.writerows(rows)
