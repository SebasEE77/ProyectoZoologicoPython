import streamlit as st
import pandas as pd
class zoologico:
    def __init__(self):
        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []
## Este metodo de zoológico recibira la información del hábitat donde se agregará a la lista hábitats si se cumple
## la condición de que no exista otro hábitat igual.
    def agregarHabitat(self, tipoHabitat):
        self.habitats.append(tipoHabitat)
        st.session_state["habitats"] = self.habitats

## Este metodo dentro de zoológico recibira todos los datos del animal que se esta queriendo ingresar, primero verificando que su hábitat exista, luego ver a que hábitat se agrego y
## posteriormente agregando al animal llamando al metodo agregarAnimales del hábitat correspondiente si es que cumple las distintas condiciones.
## Aquí hay una bandera ya que ayuda a para el ciclo del for cuando se debe y así no recorrerlo innecesariamente.
    def ingresarAnimal(self, nuevoAnimal):
        bandera = 0
        for habitat in self.habitats:
            if habitat.habitat == nuevoAnimal.habitat and nuevoAnimal.habitat == "desertico":
                for desertico in self.habitats:
                    if desertico.habitat == nuevoAnimal.habitat and desertico.dieta == nuevoAnimal.dieta and \
                            desertico.aridez == nuevoAnimal.atributoHabitat1 and desertico.tormentaArena == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)
            elif habitat.habitat == nuevoAnimal.habitat  and nuevoAnimal.habitat == "acuatico":
                for acuatico in self.habitats:
                    if acuatico.habitat == nuevoAnimal.habitat and acuatico.dieta == nuevoAnimal.dieta and \
                            acuatico.respiraAgua == nuevoAnimal.atributoHabitat1 and acuatico.nadar == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)
            elif habitat.habitat == nuevoAnimal.habitat  and nuevoAnimal.habitat == "polar":
                for polar in self.habitats:
                    if polar.habitat == nuevoAnimal.habitat and polar.dieta == nuevoAnimal.dieta and \
                            polar.clima == nuevoAnimal.atributoHabitat1 and polar.escasaVegetacion == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)
            elif habitat.habitat == nuevoAnimal.habitat  and nuevoAnimal.habitat == "selvatico":
                for selvatico in self.habitats:
                    if selvatico.habitat == nuevoAnimal.habitat and selvatico.dieta == nuevoAnimal.dieta and \
                            selvatico.climaSelvatico == nuevoAnimal.atributoHabitat1 and selvatico.diversidad == nuevoAnimal.atributoHabitat2:
                        bandera = 1
                        habitat.agregarAnimales(nuevoAnimal)

        if(bandera == 0):
            print("La informacion del animal no corresponde con ninguna habitat disponible")




##  Este método verifica si hay algo en la lista de hábitats y luego la recorre para así en cada una llamar al metodo de mostrarAnimales,
## mostrando de tal modo los animales dentro de cada habitat existente
    def mostrarAnimalesGeneral(self):
        if self.habitats:
            print("\tListado de animales Zoo de Cali")
            for habitat in self.habitats:
                habitat.mostrarAnimales()
        else:
            print("No hay habitats disponibles en el zoologico, entonces, no existe ningun animal")

## Este metodo recibe el id del animal, el hábitat y la opción a realizar con el animal. Dentro de esta se recorre
## la lista de habitat buscando el hábitat específico del animal, luego de acuerdo a la opción escogida se llama el método correspondiente del
## hábitat, ya sea mostrarAnimalInfo, dietaVectoresAnimales o interactuarAnimal.
    def buscarAnimal(self, id, tipoHabitat, opcion):
        bandera = 0
        for habitat in self.habitats:
            if(habitat.habitat == tipoHabitat):
                if(opcion == 5):
                    habitat.mostrarAnimalInfo(id)
                elif (opcion == 6):
                    habitat.dietaVectoresAnimales(id)
                else:
                    habitat.interactuarAnimal(id)
                bandera = 1

        if(bandera == 0):
            print("No existe tal habitat, por lo tanto tampoco el animal")

