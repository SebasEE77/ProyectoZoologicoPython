import streamlit as st
import pandas as pd
class Zoologico:
    def __init__(self):
        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []

        if "animalesGuardados" in st.session_state:
            self.animalesGuardados = st.session_state["animalesGuardados"]
        else:
            self.animalesGuardados = []
            st.session_state["animalesGuardados"] = []



## Este metodo de zoológico recibira la información del hábitat donde se agregará a la lista hábitats si se cumple
## la condición de que no exista otro hábitat igual.
    def agregarHabitat(self, nuevHabitat):
        bandera = 0
        for habitat in self.habitats:
            if habitat.habitat == nuevHabitat.habitat:
                st.error("No se puede agregar ya que el hábitat existe")
                bandera = 1
        if bandera == 0:
            st.success("El hábitat fue creado correctamente")
            self.habitats.append(nuevHabitat)
            st.session_state["habitats"] = self.habitats

    def agregarAnimal_Habitat(self, nuevoAnimal, tipoHabitat):
        for habitat in self.habitats:
            if nuevoAnimal.habitat != habitat.habitat:
                print("El animal que desea agregar no coincide con el habitat de registro")
            elif nuevoAnimal.dieta != habitat.dieta:
                print("El animal no coincide con la dieta del habitat")
            else:
                habitat.agregarAnimales(nuevoAnimal)

    def ingresarAnimalZoologico(self, nuevoAnimal):
        bandera = 0
        for animales in self.animalesGuardados:
            if animales.id == nuevoAnimal.id:
                st.error("No se puede agregar ya que el id es el mismo al de otro animal")
                bandera = 1
        if bandera == 0:
            st.success("El animal fue creado correctamente")
            self.animalesGuardados.append(nuevoAnimal)
            st.session_state["animalesGuardados"] = self.animalesGuardados




#
#     def agregarAnimalesHabitatZoo(self, nuevoAnimal):
#         for habitat in self.habitats:
#             habitat.agregarAnimales(nuevoAnimal)
#
#
#
#
# ## Este metodo dentro de zoológico recibira todos los datos del animal que se esta queriendo ingresar, primero verificando que su hábitat exista, luego ver a que hábitat se agrego y
# ## posteriormente agregando al animal llamando al metodo agregarAnimales del hábitat correspondiente si es que cumple las distintas condiciones.
# ## Aquí hay una bandera ya que ayuda a para el ciclo del for cuando se debe y así no recorrerlo innecesariamente.
#     def ingresarAnimal(self, nuevoAnimal):
#         bandera = 0
#         for habitat in self.habitats:
#             if habitat.habitat == nuevoAnimal.habitat and nuevoAnimal.habitat == "desertico":
#                 for desertico in self.habitats:
#                     if desertico.habitat == nuevoAnimal.habitat and desertico.dieta == nuevoAnimal.dieta and \
#                             desertico.aridez == nuevoAnimal.atributoHabitat1 and desertico.tormentaArena == nuevoAnimal.atributoHabitat2:
#                         bandera = 1
#                         habitat.agregarAnimales(nuevoAnimal)
#             elif habitat.habitat == nuevoAnimal.habitat  and nuevoAnimal.habitat == "acuatico":
#                 for acuatico in self.habitats:
#                     if acuatico.habitat == nuevoAnimal.habitat and acuatico.dieta == nuevoAnimal.dieta and \
#                             acuatico.respiraAgua == nuevoAnimal.atributoHabitat1 and acuatico.nadar == nuevoAnimal.atributoHabitat2:
#                         bandera = 1
#                         habitat.agregarAnimales(nuevoAnimal)
#             elif habitat.habitat == nuevoAnimal.habitat  and nuevoAnimal.habitat == "polar":
#                 for polar in self.habitats:
#                     if polar.habitat == nuevoAnimal.habitat and polar.dieta == nuevoAnimal.dieta and \
#                             polar.clima == nuevoAnimal.atributoHabitat1 and polar.escasaVegetacion == nuevoAnimal.atributoHabitat2:
#                         bandera = 1
#                         habitat.agregarAnimales(nuevoAnimal)
#             elif habitat.habitat == nuevoAnimal.habitat  and nuevoAnimal.habitat == "selvatico":
#                 for selvatico in self.habitats:
#                     if selvatico.habitat == nuevoAnimal.habitat and selvatico.dieta == nuevoAnimal.dieta and \
#                             selvatico.climaSelvatico == nuevoAnimal.atributoHabitat1 and selvatico.diversidad == nuevoAnimal.atributoHabitat2:
#                         bandera = 1
#                         habitat.agregarAnimales(nuevoAnimal)
#
#         if(bandera == 0):
#             print("La informacion del animal no corresponde con ninguna habitat disponible")
#
#
# ##  Este método verifica si hay algo en la lista de hábitats y luego la recorre para así en cada una llamar al metodo de mostrarAnimales,
# ## mostrando de tal modo los animales dentro de cada habitat existente
#     def mostrarAnimalesGeneral(self):
#         if self.habitats:
#             print("\tListado de animales Zoo de Cali")
#             for habitat in self.habitats:
#                 habitat.mostrarAnimales()
#         else:
#             print("No hay habitats disponibles en el zoologico, entonces, no existe ningun animal")
#
# ## Este metodo recibe el id del animal, el hábitat y la opción a realizar con el animal. Dentro de esta se recorre
# ## la lista de habitat buscando el hábitat específico del animal, luego de acuerdo a la opción escogida se llama el método correspondiente del
# ## hábitat, ya sea mostrarAnimalInfo, dietaVectoresAnimales o interactuarAnimal.
#     def buscarAnimal(self, id, tipoHabitat, opcion):
#         bandera = 0
#         for habitat in self.habitats:
#             if(habitat.habitat == tipoHabitat):
#                 if(opcion == 5):
#                     habitat.mostrarAnimalInfo(id)
#                 elif (opcion == 6):
#                     habitat.dietaVectoresAnimales(id)
#                 else:
#                     habitat.interactuarAnimal(id)
#                 bandera = 1
#
#         if(bandera == 0):
#             print("No existe tal habitat, por lo tanto tampoco el animal")

