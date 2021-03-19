fahrenheit = float(input("Geben sie die Temperatur in Fahrenheit an: "))
print(type(fahrenheit))
celsius = "{:.1f}".format(5 * (fahrenheit - 32) / 9)
print(fahrenheit,"Grad Fahrenheit entspechen",celsius,"Grad Celsius")