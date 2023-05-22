import streamlit as st
import pandas as pd
class Habitat:
    def __init__(self, habitat, numAnimales, temperatura,dieta,contadorAnimales):
        self.habitat = habitat
        self.numAnimales = numAnimales
        self.temperatura = temperatura
        self.dieta = dieta
        self.contadorAnimales = contadorAnimales
        if "animales" in st.session_state:
            self.animales = st.session_state["animales"]
        else:
            self.animales = []
            st.session_state["animales"] = []

## Este metodo solamente muestra la información de los hábitats que existen en el zoológico
    def imprimirHabitat(self):
        print("Habitat: ",self.habitat)
        print("Capacidad maxima: ",self.numAnimales)
        print("Temperatura: ",self.temperatura)
        print("Dieta: ",self.dieta)

## Este metodo agrega los animales a la lista animales teniendo en cuenta las características recibidas
## en el método de ingresarAnimal de zoologico.
    def agregarAnimales(self, nuevoAnimal):
        bandera = 0
        for animales in self.animales:
            if animales.id == nuevoAnimal.id:
                st.error("No se puede agregar ya que el id es el mismo al de otro animal")
                bandera = 1
        if bandera == 0:
            st.success("El animal fue creado correctamente")
            self.animales.append(nuevoAnimal)
            st.session_state["animales"] = self.animales

        # if self.animales:
        #     self.contadorAnimales += 1
        # if len(self.animales) < self.numAnimales:
        #     st.success("El animal fue agregado")
        # else:
        #     st.error("No hay disponibilidad en el hábitat")

## Este método lo que hace es listar los animales dentro de la lista animales mostrando su id, nombre y tipo de hábitat,
## además, si no existe ningun animal se muestra el mensaje indicando que no existen.
    def mostrarAnimales(self):
        if len(self.animales) > 0:
            with st.container():
                st.subheader("Listado de Animales en los hábitats")
                if len(self.animales) == 0:
                    st.error("No existe ningun hábitat")
                else:
                    datos = pd.DataFrame(
                        self.aplicarTablaAnimalesGeneral(),
                        columns=["Id del animal", "Nombre", "Tipo de hábitat", "Edad", "Dieta",
                                 "Horas de sueño", "Temperatura"]
                    )
                    st.table(datos)
        else:
            st.error("No hay animales en los hábitats")

    def aplicarTablaAnimalesGeneral(self):
        datos = []
        for animales in self.animales:
            datos.append([animales.id, animales.nombre, animales.tipoHabitat, animales.edad, animales.dieta,
                          animales.horasDormir,animales.temperatura])
        return datos

    def buscarAnimalAnimales(self):
        st.divider()
        opcionesAnimales = []
        for animales in self.animales:
            opcionesAnimales.append(animales.id)
        id = st.selectbox("Escoge el id del animal", opcionesAnimales)
        animalEscogido = self.verificarAnimal2(self.animales, id)
        return animalEscogido

    def verificarAnimal2(self,animalesGuardados, id):
        for animales in animalesGuardados:
            if id == animales.id:
                return animales



## Este metodo lo que se encarga es de buscar al animal dentro de la lista animales de acuerdo a su id para de tal modo gestionar la dieta del animal,
## ya sea agregar una comida, cambiarla por otra o eliminarla de su dieta.
    def dietaVectoresAnimales(self,animalEscogido):
        for animales in self.animales:
            if animales.id == animalEscogido.id:
                st.divider()
                st.subheader("Bienvenido al menu de dieta para los animales del Zoo\n")
                tab1, tab2, tab3 = st.tabs(["Ver la dieta del animal", "Agregar comida a la dieta del animal",
                                            "Modificar comida de la dieta",])
                with tab1:
                    st.header("Dieta del animal")
                    animales.mostrarDietaAnimal()
                with tab2:
                    dieta = animales.dieta
                    animales.mostrarDietasDisponibles(dieta)
                    if dieta == "carnivoro":
                        comida = st.selectbox("Elige una comida de la lista para el animal: ",animales.arregloCarnivoro)
                    elif dieta == "herbivoro":
                        comida = st.selectbox("Elige una comida de la lista para el animal: ",
                                              animales.arregloHerbivoro, key=11)
                    else:
                        comida = st.selectbox("Elige una comida de la lista para el animal: ", animales.arregloOmnivoro,
                                              key=12)
                    botonAccion = st.button("Agregar Comida", key=13)
                    if botonAccion:
                        animales.agregarComida(comida)

                with tab3:
                    st.subheader("Modificar dieta")
                    verificarComida = animales.modificarDietaInfo()
                    comida = st.selectbox("Ingrese la comida que quisiera modificar: ", verificarComida)
                    animales.modificarDieta("modificar",comida)



## Este metodo se encargara de buscar al animal dentro del hábitat de acuerdo al id mandado como parametro. Luego pedira al usuario que escoga
## una opción para interactuar con el animal, ya sea jugar, dormir o comer.
    def interactuarAnimal(self, animalEscogido):
        for animales in self.animales:
            if animales.id == animalEscogido.id:
                st.divider()
                st.subheader("Gracias por querer interactuar con nuestros animales!")
                tab1, tab2, tab3 = st.tabs(["Jugar", "Comer","Dormir", ])
                with tab1:
                    if animales.estadoActivo == 0:
                        st.warning("El animal esta dormiendo en este momento")
                    elif animales.estadoJugar == 1:
                        st.warning("El animal ya ha jugado, podrá jugar otra vez cuando duerma")
                    else:
                        animales.jugar()

                with tab2:
                    if animales.estadoActivo == 0:
                        st.warning("El animal esta dormiendo en este momento")
                    else:
                        animales.comer()

                with tab3:
                    if animales.estadoActivo == 0:
                        animales.estadoActivo = 1
                        animales.estadoJugar = 0
                        despertar = st.button("Despertar al animal")
                        if despertar:
                            st.success("Se desperto el animal")
                    else:
                        animales.dormir()



## Apartir de aquí están las clases hijas de la clase hábitat las cuales tienen 2 atributos únicos que los diferencian
## de las demás hábitats del zoológico. Cada una tiene un imprimirHabitat y un imprimirAnimales que lo que hacen es añadir
## información extra a esos métodos.
class desertico(Habitat):
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta,contadorAnimales, aridez, tormentaArena):
        super().__init__(tipoHabitat, numAnimales, temperatura, dieta, contadorAnimales)
        self.aridez = aridez
        self.tormentaArena = tormentaArena

    def imprimirHabitat(self):
        print("-------------------------")
        super().imprimirHabitat()
        print("Clima Arido: ", self.aridez)
        print("Hay tormentas de arena: ", self.tormentaArena)
        print("-------------------------")

class acuatico(Habitat):
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta,contadorAnimales, respiraAgua, nadar):
        super().__init__(tipoHabitat, numAnimales, temperatura, dieta, contadorAnimales)
        self.respiraAgua = respiraAgua
        self.nadar = nadar

    def imprimirHabitat(self):
        print("-------------------------")
        super().imprimirHabitat()
        print("Se puede respirar bajo el agua: ", self.respiraAgua)
        print("Se puede nadar: ", self.nadar)
        print("-------------------------")

class polar(Habitat):
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta,contadorAnimales, clima, escasaVegetacion):
        super().__init__(tipoHabitat, numAnimales, temperatura, dieta, contadorAnimales)
        self.clima = clima
        self.escasaVegetacion = escasaVegetacion

    def imprimirHabitat(self):
        print("-------------------------")
        super().imprimirHabitat()
        print("Clima de baja temperatura: ", self.clima)
        print("Tiene escasa vegetacion: ", self.escasaVegetacion)
        print("-------------------------")

class selvatico(Habitat):
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta,contadorAnimales, climaSelvatico, diversidad):
        super().__init__(tipoHabitat, numAnimales, temperatura, dieta, contadorAnimales)
        self.climaSelvatico = climaSelvatico
        self.diversidad = diversidad

    def imprimirHabitat(self):
        print("-------------------------")
        super().imprimirHabitat()
        print("Clima calido y humedo: ", self.climaSelvatico)
        print("Tiene mucha diversidad biologica: ", self.diversidad)
        print("-------------------------")

