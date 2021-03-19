from class_kreis import kreis
class zylinder(kreis):
    def __init__(self,radius,hoehe):
        super().__init__(radius)
        self.hoehe=hoehe
    
    def volumen(self):
        return self.flaeche() * self.hoehe

    def print(self):
        print("Zylinder mit Radius", self.radius, "und Höhe", self.hoehe)        
        print("{0:<20} {1:>9.2f}".format("- Volumen =",self.volumen()))
        #print("- Volumen     =", self.volumen())
        print(super().print())

