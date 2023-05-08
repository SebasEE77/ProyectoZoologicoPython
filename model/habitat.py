class habitat:
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta):
        self.habitat = tipoHabitat
        self.numAnimales = numAnimales
        self.temperatura = temperatura
        self.dieta = dieta
        self.animales = []


    def imprimirHabitat(self):
        print("Habitat: ", self.habitat)
        print("Capacidad maxima: ", self.numAnimales)
        print("Temperatura: ", self.temperatura)
        print("Dieta: ", self.dieta)

    def agregarAnimales(self, animal):
        self.animales.append(animal)
        print("Se agrego el animal correctamente")
