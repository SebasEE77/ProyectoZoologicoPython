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
        if opcion == 2:
            try:
                animales = self.vista.menuCrearAnimales()
                if animales:
                    self.modelo.ingresarAnimalZoologico(animales)
            except ValueError:
                self.vista.mostraMensajeError("Se presentó un error creando el animal")
        if opcion == 3:
            self.vista.agregarAnimalHabitat(self.modelo.animalesGuardados,self.modelo.habitats)
        if opcion == 4:
            self.vista.mostrarHabitats(self.modelo.habitats)
        if opcion == 5:
            self.vista.mostrarAnimalesZoologico(self.modelo.animalesGuardados)
        if opcion == 6:
            self.modelo.mostrarAnimalesGeneral()
        if opcion == 7:
            self.modelo.mostrarAnimalesGeneral()
            self.modelo.buscarAnimal(5)
        if opcion == 8:
            self.modelo.mostrarAnimalesGeneral()
            self.modelo.buscarAnimal(6)

    def aplicarTabla(self, habitats):
        datos = []
        for desertico in habitats:
            if desertico.habitat == "desertico":
                datos.append([desertico.habitat, desertico.numAnimales, desertico.temperatura, desertico.dieta, desertico.aridez,desertico.tormentaArena])
        for acuatico in habitats:
            if acuatico.habitat == "acuatico":
                datos.append([acuatico.habitat, acuatico.numAnimales, acuatico.temperatura, acuatico.dieta, acuatico.nadar,acuatico.respiraAgua])
        for polar in habitats:
            if polar.habitat == "polar":
                datos.append([polar.habitat, polar.numAnimales, polar.temperatura, polar.dieta, polar.clima,polar.escasaVegetacion])
        for selvatico in habitats:
            if selvatico.habitat == "selvatico":
                datos.append([selvatico.habitat, selvatico.numAnimales, selvatico.temperatura, selvatico.dieta, selvatico.climaSelvatico,selvatico.diversidad])
        return datos

    def aplicarTablaAnimales(self,animalesGuardados):
        datos = []
        for animales in animalesGuardados:
            datos.append([animales.id, animales.nombre, animales.tipoHabitat, animales.edad,animales.dieta,animales.horasDormir,
                          animales.temperatura])
        return datos
