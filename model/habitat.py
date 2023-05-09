import model.animales as modelAnimal
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
        print("\n")

    def agregarAnimales(self, nuevoAnimal):
        bandera = 0
        for animales in self.animales:
            if animales.id == nuevoAnimal.id:
                bandera = 1
                print("No es posible agregar el animal por el id escrito")

        if (bandera == 0):
            self.animales.append(nuevoAnimal)
            print("Se agrego el animal correctamente")

    def mostrarAnimales(self):
        if self.animales:
            print("Listado de animales:\n")
            for animales in self.animales:
                animales.imprimirAnimales()
        else:
            print("No hay animales por el momento")

    def mostrarAnimalInfo(self):
        print("Listado de animales:\n")
        for animales in self.animales:
            animales.imprimirAnimalInfo()