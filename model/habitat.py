class habitat:
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta):
        self.habitat = tipoHabitat
        self.numAnimales = numAnimales
        self.temperatura = temperatura
        self.dieta = dieta


    def imprimirHabitat(self):
        print("Habitat: ", self.habitat)
        print("Capacidad maxima: ", self.numAnimales)
        print("Temperatura: ", self.temperatura)
        print("Dieta: ", self.dieta)
