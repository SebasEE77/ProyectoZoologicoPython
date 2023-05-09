class habitatController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutarOpcionAnimales(self, opcion):
        if opcion == 4:
            self.modelo.mostrarAnimales()
        elif opcion == 5:
            self.modelo.mostrarAnimalInfo()