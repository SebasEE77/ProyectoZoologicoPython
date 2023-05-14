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
            if habitat.habitat == "desertico" and nuevoAnimal.habitat == "desertico":
                for desertico in self.habitats:
                    if desertico.habitat == nuevoAnimal.habitat and desertico.dieta == nuevoAnimal.dieta and \
                            desertico.aridez == nuevoAnimal.atributoHabitat1 and desertico.tormentaArena == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)
            elif habitat.habitat == "acuatico" and nuevoAnimal.habitat == "acuatico":
                for acuatico in self.habitats:
                    if acuatico.habitat == nuevoAnimal.habitat and acuatico.dieta == nuevoAnimal.dieta and \
                            acuatico.respiraAgua == nuevoAnimal.atributoHabitat1 and acuatico.nadar == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)
            elif habitat.habitat == "polar" and nuevoAnimal.habitat == "polar":
                for polar in self.habitats:
                    if polar.habitat == nuevoAnimal.habitat and polar.dieta == nuevoAnimal.dieta and \
                            polar.clima == nuevoAnimal.atributoHabitat1 and polar.escasaVegetacion == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)
            elif habitat.habitat == "selvatico" and nuevoAnimal.habitat == "selvatico":
                for selvatico in self.habitats:
                    if selvatico.habitat == nuevoAnimal.habitat and selvatico.dieta == nuevoAnimal.dieta and \
                            selvatico.climaSelvatico == nuevoAnimal.atributoHabitat1 and selvatico.diversidad == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)

        if(bandera == 0):
            print("La informacion del animal no corresponde con ninguna habitat disponible")


    def verificarTemperatura(self, nuevoAnimal):
        bandera = 0
        if (nuevoAnimal.habitat == "desertico" and (nuevoAnimal.temperatura < 30 or nuevoAnimal.temperatura > 40)):
            bandera = 1
            print("No se puede agregar el animal por la temperatura ingresadaa")
        elif (nuevoAnimal.habitat == "selvatico" and (nuevoAnimal.temperatura < 10 or nuevoAnimal.temperatura > 20)):
            bandera = 1
            print("No se puede agregar el animal por la temperatura ingresadab")
        elif (nuevoAnimal.habitat == "polar" and (nuevoAnimal.temperatura < -20 or nuevoAnimal.temperatura > -5)):
            bandera = 1
            print("No se puede agregar el animal por la temperatura ingresadac")
        elif (nuevoAnimal.habitat == "acuatico" and (nuevoAnimal.temperatura < 2 or nuevoAnimal.temperatura > 8)):
            bandera = 1
            print("No se puede agregar el animal por la temperatura ingresada")

        if bandera == 0:
            self.ingresarAnimal(nuevoAnimal)

    def mostrarHabitats(self):
        if self.habitats:
            print("\t->Listado de habitats del Zoologico<-")
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

