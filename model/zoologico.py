class zoologico:
    def __init__(self):
        self.habitats = []
    def agregarHabitat(self, habitat):
        for i in self.habitats:
            tipoHabitat = self.habitats[i]
            if habitat not in tipoHabitat:
                self.habitats.append(habitat)
                print("Se agrego exitosamente el habitat")
            else:
                print("El habitat ya existe en el zoologico")



    def mostrarHabitats(self):
        print("Listado de habitats:")
        for habitat in self.habitats:
            habitat.imprimirHabitat()
