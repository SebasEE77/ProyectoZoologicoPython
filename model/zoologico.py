class zoologico:
    def __init__(self):
        self.habitats = []
    def agregarHabitat(self, habitat):
        self.habitats.append(habitat)
        print("Se agrego el habitat exitosamente")



    def mostrarHabitats(self):
        print("Listado de habitats:")
        for habitat in self.habitats:
            habitat.imprimirHabitat()
