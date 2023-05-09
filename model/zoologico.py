import controller.habitatController as HabitatController
class zoologico:
    def __init__(self):
        self.habitats = []
    def agregarHabitat(self, tipoHabitat):
        bandera = 0
        for habitat in self.habitats:
            if habitat.habitat == tipoHabitat.habitat:
                bandera = 1
                print("Esta habitat ya se ha creado, intente de nuevo.")

        if (bandera == 0):
            self.habitats.append(tipoHabitat)
            print("Se agrego el habitat exitosamente")

    def ingresarAnimal(self, nuevoAnimal):
        bandera = 0
        for habitat in self.habitats:
            if habitat.habitat == nuevoAnimal.habitat and habitat.dieta == nuevoAnimal.dieta:
                bandera = 1
                habitat.agregarAnimales(nuevoAnimal)

        if(bandera == 0):
            print("La informacion del animal no corresponde con ninguna habitat disponible")


    def mostrarHabitats(self):
        print("Listado de habitats:\n")
        for habitat in self.habitats:
            habitat.imprimirHabitat()
