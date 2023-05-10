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
        if self.habitats:
            print("Listado de habitats del Zoologico:\n")
            for habitat in self.habitats:
                habitat.imprimirHabitat()
        else:
            print("No hay habitats disponibles en el zoologico")

    def mostrarAnimalesGeneral(self):
        if self.habitats:
            print("\tListado de animales Zoo de Cali")
            for habitat in self.habitats:
                habitat.mostrarAnimales()
        else:
            print("No hay habitats disponibles en el zoologico, entonces, no existe ningun animal")


    def buscarAnimal(self, id, tipoHabitat, opcion):
        bandera = 0
        for habitat in self.habitats:
            if(habitat.habitat == tipoHabitat):
                if(opcion == 5):
                    habitat.mostrarAnimalInfo(id)
                elif (opcion == 6):
                    habitat.dietaVectoresAnimales(id)
                else:
                    habitat.interactuarAnimal(id)
                bandera = 1

        if(bandera == 0):
            print("No existe tal habitat, por lo tanto tampoco el animal")

