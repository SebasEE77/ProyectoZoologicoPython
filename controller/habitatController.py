class habitatController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutarOpcionAnimales(self, opcion):
        if opcion == 2:
            animal = self.vista.menuCrearAnimales()
            self.modelo.agregarAnimales(animal)
        elif opcion == 3:
            self.modelo.mostrarHabitats()