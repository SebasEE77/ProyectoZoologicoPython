class zoologicoController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

## Este es el controlador del programa. Es con base a la clase zoológico ya que desde ahí se maneja la mayoría de las cosas.
    def ejecutarOpcion(self, opcion):
        if opcion == 1:
            habitat = self.vista.menuCrearHabitat()
            self.modelo.agregarHabitat(habitat)
        elif opcion == 2:
            animales = self.vista.menuCrearAnimales()
            self.modelo.ingresarAnimal(animales)
        elif opcion == 3:
            self.vista.mostrarHabitats(self.modelo.habitats)
        elif opcion == 4:
            self.modelo.mostrarAnimalesGeneral()
        elif opcion == 5:
            self.modelo.mostrarAnimalesGeneral()
            aux2 = self.vista.opcionAuxiliar2()
            aux1 = self.vista.opcionAuxiliar1()
            self.modelo.buscarAnimal(aux1,aux2,5)
        elif opcion == 6:
            self.modelo.mostrarAnimalesGeneral()
            aux2 = self.vista.opcionAuxiliar2()
            aux1 = self.vista.opcionAuxiliar1()
            self.modelo.buscarAnimal(aux1,aux2,6)
        elif opcion == 7:
            self.modelo.mostrarAnimalesGeneral()
            aux2 = self.vista.opcionAuxiliar2()
            aux1 = self.vista.opcionAuxiliar1()
            self.modelo.buscarAnimal(aux1,aux2,7)

    def aplicarTabla(self, habitats):
        datos = []
        for habitat in habitats:
            datos.append([habitat.habitat, habitat.numAnimales, habitat.temperatura, habitat.dieta])
        return datos