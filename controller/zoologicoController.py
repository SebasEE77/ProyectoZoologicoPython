class zoologicoController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    def ejecutarOpcionHabitat(self, opcion):
        if opcion == 1:
            habitat = self.vista.menuCrearHabitat()
            self.modelo.agregarHabitat(habitat)
        elif opcion == 2:
            animales = self.vista.menuCrearAnimales()
            self.modelo.ingresarAnimal(animales)
        elif opcion == 3:
            self.modelo.mostrarHabitats()
        elif opcion == 4:
            self.modelo.mostrarAnimalesGeneral()
        elif opcion == 5:
            aux2 = self.vista.opcionAuxiliar2()
            aux1 = self.vista.opcionAuxiliar1()
            self.modelo.buscarAnimal(aux1,aux2,5)
        elif opcion == 6:
            aux2 = self.vista.opcionAuxiliar2()
            aux1 = self.vista.opcionAuxiliar1()
            self.modelo.buscarAnimal(aux1,aux2,6)
        elif opcion == 7:
            aux2 = self.vista.opcionAuxiliar2()
            aux1 = self.vista.opcionAuxiliar1()
            self.modelo.buscarAnimal(aux1,aux2,7)


