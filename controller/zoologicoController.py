import streamlit as st
class zoologicoController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

## Este es el controlador del programa. Es con base a la clase zoológico ya que desde ahí se maneja la mayoría de las cosas.
    def ejecutarOpcion(self, opcion):
        if opcion == 1:
            try:
                habitat = self.vista.menuCrearHabitat()
                if habitat:
                    self.modelo.agregarHabitat(habitat)
            except ValueError:
                self.vista.mostraMensajeError("Se presentó un error creando el hábitat")
        elif opcion == 2:
            try:
                animales = self.vista.menuCrearAnimales()
                if animales:
                    self.modelo.ingresarAnimalZoologico(animales)
            except ValueError:
                self.vista.mostraMensajeError("Se presentó un error creando el animal")
        elif opcion == 3:
            self.vista.agregarAnimalHabitat(self.modelo.animalesGuardados)
        if opcion == 4:
            self.vista.mostrarHabitats(self.modelo.habitats)
        if opcion == 5:
            self.vista.mostrarAnimalesZoologico(self.modelo.animalesGuardados)
        # elif opcion == 6:
        #     self.modelo.mostrarAnimalesGeneral()
        #     aux2 = self.vista.opcionAuxiliar2()
        #     aux1 = self.vista.opcionAuxiliar1()
        #     self.modelo.buscarAnimal(aux1, aux2, 5)
        # elif opcion == 7:
        #     self.modelo.mostrarAnimalesGeneral()
        #     aux2 = self.vista.opcionAuxiliar2()
        #     aux1 = self.vista.opcionAuxiliar1()
        #     self.modelo.buscarAnimal(aux1, aux2, 6)
        # elif opcion == 8:
        #     self.modelo.mostrarAnimalesGeneral()
        #     aux2 = self.vista.opcionAuxiliar2()
        #     aux1 = self.vista.opcionAuxiliar1()
        #     self.modelo.buscarAnimal(aux1, aux2, 7)

    def aplicarTabla(self, habitats):
        datos = []
        for habitat in habitats:
            datos.append([habitat.habitat, habitat.numAnimales, habitat.temperatura, habitat.dieta])
        return datos

    def aplicarTablaAnimales(self,animalesGuardados):
        datos = []
        for animales in animalesGuardados:
            datos.append([animales.id, animales.nombre, animales.tipoHabitat, animales.edad,animales.dieta,animales.horasDormir,
                          animales.temperatura])
        return datos
