import math as math
class kreis:
    def __init__(self,radius):
        self.radius=radius

    def umfang(self):
        return self.radius * 2 *math.pi

    def flaeche(self):
        return math.pow(self.radius,2) * math.pi

    def print(self):
        print("Kreis mit Radius =",self.radius)
        print("{0:<20} {1:>9.2f}".format("- Umfang =",self.umfang()))
        print("{0:<20} {1:>9.2f}".format("- Flaeche =",self.flaeche()))

    def newradius(self,radius):
        self.radius=radius




