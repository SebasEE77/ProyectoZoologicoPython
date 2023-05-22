import streamlit as st
import model.habitat as habitatModel
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

    def ingresarAnimalZoologico(self, nuevoAnimal):
        bandera = 0
        for animales in self.animalesGuardados:
            if animales.id == nuevoAnimal.id:
                st.error("No se puede agregar ya que el id es el mismo al de otro animal")
                bandera = 1
        if bandera == 0:
            st.success("El animal fue agregado correctamente")
            self.animalesGuardados.append(nuevoAnimal)
            st.session_state["animalesGuardados"] = self.animalesGuardados
    def eliminarAnimalGuardado(self,id):
        for i, animales in enumerate(self.animalesGuardados):
            if animales.id == id:
                self.animalesGuardados.pop(i)
                st.session_state["animalesGuardados"] = self.animalesGuardados

# ##  Este método verifica si hay algo en la lista de hábitats y luego la recorre para así en cada una llamar al metodo de mostrarAnimales,
# ## mostrando de tal modo los animales dentro de cada habitat existente
    def mostrarAnimalesGeneral(self):
        st.divider()
        if self.habitats:
            for habitat in self.habitats:
                habitat.mostrarAnimales()
        else:
            st.error("No hay habitats disponibles en el zoologico, entonces, no existe ningun animal")

# ## Este metodo recibe el id del animal, el hábitat y la opción a realizar con el animal. Dentro de esta se recorre
# ## la lista de habitat buscando el hábitat específico del animal, luego de acuerdo a la opción escogida se llama el método correspondiente del
# ## hábitat, ya sea mostrarAnimalInfo, dietaVectoresAnimales o interactuarAnimal.
    def buscarAnimal(self,opcion):
        opcionesHabitat = []
        for habitat in self.habitats:
            opcionesHabitat.append(habitat.habitat)
        habitatSeleccionado = st.selectbox("Escoge el hábitat del animal", opcionesHabitat)
        habitatEscogido = self.verificarHabitat2(self.habitats, habitatSeleccionado)
        animalEscogido = habitatEscogido.buscarAnimalAnimales()
        if opcion == 5:
            habitatEscogido.dietaVectoresAnimales(animalEscogido)
        else:
            habitatEscogido.interactuarAnimal(animalEscogido)


    def verificarHabitat2(self,habitats, habitatSeleccionado):
        for habitat in habitats:
            if habitat.habitat == habitatSeleccionado:
                return habitat

