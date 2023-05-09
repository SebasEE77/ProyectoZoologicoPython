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
