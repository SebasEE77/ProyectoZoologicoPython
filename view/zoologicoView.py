import model.habitat as habitatModel
import controller.zoologicoController as ZoologicoController
import model.zoologico as zoologicoModel
import model.animales as animalesModel
import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
## Esta clase se crea específicamente para mostrar el menu y se llamar los respectivos metodos desde el controlador.
class zoologicoView:

    def __init__(self):
        self.zoologico = zoologicoModel.Zoologico()
        self.controlador = ZoologicoController.zoologicoController(self.zoologico, self)

    def mostrarMenu(self):
        pages = ["Inicio" ,"Agregar Habitat", "Agregar Animal a un Zoológico", "Agregar animal a un Hábitat", "Ver lista de Hábitats",
                 "Ver lista de Animales del Zoológico", "Ver lista animales general","Ver dieta de los animales",
                 "Interactuar con los animales","Consultar animales en internet"]
        selection = st.sidebar.radio("Selecciona una opción del menú", pages)

        if selection == "Inicio":
            st.title("Bienvenido al Zoologico de Cali")
            st.write("El proyecto trata de simular un zoológico el cual se compone de distintos hábitats escritos por el usuario, "
                "en este caso solo se podrían 4, el hábitat desértico, acuático, polar y selvático, donde cada hábitat tiene ciertas "
                "características en la que los animales tendrán que cumplir. La idea es que dentro de esos hábitats haya animales con ciertas cualidades, "
                "las cuales el usuario determinara para que finalmente se pueda interactuar con cada animal, ya sea agregando o editando la dieta del animal "
                "dependiendo de su tipo de alimentación, que sería carnívoro, herbívoro u omnívoro, y también interactuar de acuerdo con varias acciones que el animal podrá hacer, siendo comer, dormir o jugar")

        elif selection == "Agregar Habitat":
            st.title("Agregar Hábitat al Zoológico")
            botonAgregarHabitat = st.button("Agregar",1)
            if botonAgregarHabitat:
                st.session_state["opcion"] = 1

        elif selection == "Agregar Animal a un Zoológico":
            st.title("Agregar Animal al Zoológico")
            botonAgregarAnimal = st.button("Agregar", 2)
            if botonAgregarAnimal:
                st.session_state["opcion"] = 2

        elif selection == "Agregar animal a un Hábitat":
            st.title("Agregar Animales a una Hábitat")
            botonAgregarAnimalHabitat = st.button("Agregar a Hábitat",3)
            if botonAgregarAnimalHabitat:
                st.session_state["opcion"] = 3

        elif selection == "Ver lista de Hábitats":
            st.title("Lista de Hábitats")
            botonListaHabitats = st.button("Ver lista Hábitats", 4)
            if botonListaHabitats:
                st.session_state["opcion"] = 4

        elif selection == "Ver lista de Animales del Zoológico":
            st.title("Lista de Animales del Zoológico")
            botonListaAnimalesgeneral = st.button("Ver lista completa de animales",5)
            if botonListaAnimalesgeneral:
                st.session_state["opcion"] = 5

        elif selection == "Ver lista animales general":
            st.title("Lista de Animales en General")
            botonListaAnimalesgeneral = st.button("Ver lista completa de animales", 6)
            if botonListaAnimalesgeneral:
                st.session_state["opcion"] = 6

        elif selection == "Ver dieta de los animales":
            st.title("Dieta de los animales")
            botonDieta = st.button("Ingresar el animal", 7)
            if botonDieta:
                st.session_state["opcion"] = 7

        elif selection == "Interactuar con los animales":
            st.title("Interacción con los animales de las hábitats")
            botonAccionAnimal = st.button("Interactuar", 8)
            if botonAccionAnimal:
                st.session_state["opcion"] = 8

        elif selection == "Consultar animales en internet":
            st.title("Varias imagenes de Animales")
            botonApi = st.button("Mirar Imagenes", 9)
            if botonApi:
                st.session_state["opcion"] = 9

        if "opcion" in st.session_state:
            self.controlador.ejecutarOpcion(st.session_state["opcion"])

    ##Creamos una función que pide por consola el nombre y varias características del hábitat a crear y luego verificamos que sea el correcto. Esta función se implementa
##en el view debido a que manejamos información para crear los hábitats. Al final se retorna el hábitat creado para guardar la información en la lista
    def menuCrearHabitat(self):
        st.divider()
        with st.container():
            st.subheader("Hola usuario, estas son las opciones para agregar habitats:")
            st.subheader("\t->Habitats para agregar<-")
            st.write("-> desertico")
            st.write("-> selvatico")
            st.write("-> polar")
            st.write("-> acuatico")
            habitat = st.selectbox(
                "Escoge el habitat que desea agregar:",
                ("","desertico", "selvatico", "polar", "acuatico"))
            numAnimales = st.number_input("Escriba la cantidad de animales que pueda tener el habitat (Max 4 animales por habitat):", min_value=1, max_value=4)
            st.subheader("\t->Rangos de temperatura<-")
            st.write("-> desertico: 30° -> 40°")
            st.write("-> selvatico: 10° -> 20°")
            st.write("-> polar: -20° -> -5")
            st.write("-> acuatico: 2° -> 8° ")
            if habitat == "desertico":
                temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:", min_value=30, max_value=40)
            elif habitat == "selvatico":
                temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:", min_value=10, max_value=20)
            elif habitat == "polar":
                temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:", min_value=-20, max_value=-5)
            else:
                temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:", min_value=2, max_value=8)
            st.subheader("\t->Dietas disponibles<-")
            st.write("-> carnivoro")
            st.write("-> herbivoro")
            st.write("-> omnivoro")
            dietaAnimal = st.selectbox(
                "Escoge la dieta del hábitat:",
                ("","carnivoro", "herbivoro", "omnivoro"))

            botonAccionHabitat = st.button("Crear Habitat")
            if botonAccionHabitat:
                if habitat == "desertico":
                    st.write("\nTeniendo en cuenta que el habitat es desertico, se le atribuyen caracteristicas, "
                          "siendo un clima arido y un lugar donde hay tormentas de arena.\n")
                    nuevaHabitat = habitatModel.desertico(habitat, numAnimales, temperatura, dietaAnimal, 0, "arido", "soporta tormentas de arena")
                elif habitat == "polar":
                    st.write("\nTeniendo en cuenta que el habitat es polar, se le atribuyen caracteristicas, "
                          "siendo un clima con hielo y nieve y un lugar con escasa vegetacion.\n")
                    nuevaHabitat = habitatModel.polar(habitat, numAnimales, temperatura, dietaAnimal, 0, "frio y nieve", "escasa vegetación")
                elif habitat == "acuatico":
                    st.write("\nTeniendo en cuenta que el habitat es acuatico, se le atribuyen caracteristicas, "
                          "siendo que se debe respirar bajo el agua y ser capaz de nadar.\n")
                    nuevaHabitat = habitatModel.acuatico(habitat, numAnimales, temperatura, dietaAnimal, 0, "respirar bajo el agua","moderado y muy frio")
                else:
                    st.write("\nTeniendo en cuenta que el habitat es selvatico, se le atribuyen caracteristicas, "
                          "siendo un clima calido y humedo y un lugar con mucha diversidad biologica.\n")
                    nuevaHabitat = habitatModel.selvatico(habitat, numAnimales, temperatura, dietaAnimal, 0, "calido y humedo", "mucha diversidad biologica")
                return nuevaHabitat

##Creamos una función que pide por consola las distintas características del animal que se va agregar en el hábitat. Esta función se implementa
##en el view debido a que manejamos información para crear los animales. Al final se retorna el hábitat creado para guardar la información en una lista vacía

    def menuCrearAnimales(self):
        st.divider()
        st.subheader("Hola usuario, escribe las caracteristicas del animal que quieres crear\n")
        id = st.number_input("Escribe el id del animal:", min_value=1,max_value=1000000000)
        nombre = st.text_input("Escribe el nombre del animal:")
        st.subheader("\t->Habitats para escoger<-")
        st.write("-> desertico")
        st.write("-> selvatico")
        st.write("-> polar")
        st.write("-> acuatico")
        habitat = st.selectbox(
            "Escoge el habitat que desea agregar:",
            ("","desertico", "selvatico", "polar", "acuatico"))
        edad = st.number_input("Escribe la edad del animal:", min_value=1,max_value=15)
        st.subheader("\t->Dietas disponibles<-")
        st.write("-> carnivoro")
        st.write("-> herbivoro")
        st.write("-> omnivoro")
        dieta = st.selectbox(
            "Escoge la dieta del hábitat:",
            ("","carnivoro", "herbivoro", "omnivoro"))
        st.subheader("\t->Rangos de temperatura<-")
        st.write("-> desertico: 30° -> 40°")
        st.write("-> selvatico: 10° -> 20°")
        st.write("-> polar: -20° -> -5")
        st.write("-> acuatico: 2° -> 8° ")
        if habitat == "desertico":
            temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:",
                                          min_value=30, max_value=40)
        elif habitat == "selvatico":
            temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:",
                                          min_value=10, max_value=20)
        elif habitat == "polar":
            temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:",
                                          min_value=-20, max_value=-5)
        else:
            temperatura = st.number_input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla:",
                                          min_value=2, max_value=8)
        horasDormir = st.number_input("Escribe las horas de dormir del animal:", min_value=5, max_value=20)
        botonAccionAnimales = st.button("Crear Animal")
        if botonAccionAnimales:
            nuevoAnimal = animalesModel.Animales(id, nombre, habitat, edad, dieta, horasDormir, temperatura, 1, 0, None ,None,3)
            return nuevoAnimal

    def agregarAnimalHabitat(self, animalesGuardados, habitats):
        self.mostrarAnimalesZoologico(animalesGuardados)
        st.divider()
        self.mostrarHabitats(habitats)
        st.divider()
        opcionesAnimales = []
        opcionesHabitat = []
        for animales in animalesGuardados:
            opcionesAnimales.append(animales.id)
        for habitat in habitats:
            opcionesHabitat.append(habitat.habitat)
        id = st.selectbox("Escoge el animal que deseas agregar", opcionesAnimales)
        habitatSeleccionado = st.selectbox("Escoge el hábitat donde quieres agregar el animal", opcionesHabitat)
        animalEscogido = self.verificarAnimal(animalesGuardados,id)
        habitatEscogido = self.verificarHabitat(habitats, habitatSeleccionado)
        atributoHabitat = self.atributoHabitats(habitatSeleccionado)
        if atributoHabitat == 1:
            botonAccion = st.button("Agregar")
            if botonAccion:
                if animalEscogido.dieta == habitatEscogido.dieta and animalEscogido.tipoHabitat == habitatEscogido.habitat:
                    verificacion = habitatEscogido.agregarAnimales(animalEscogido)
                    if verificacion == True:
                        self.zoologico.eliminarAnimalGuardado(id)
                else:
                    st.error("La selección no concuerda")
        else:
            st.error("La selección por ahora no concuerda")

    def verificarAnimal(self,animalesGuardados, id):
        for animales in animalesGuardados:
            if id == animales.id:
                return animales
    def verificarHabitat(self,habitats, habitatSeleccionado):
        for habitat in habitats:
            if habitat.habitat == habitatSeleccionado:
                return habitat

    def atributoHabitats(self,habitat):
        st.write("\nA continuacion se realizara dos preguntas cerradas para saber si el animal "
              "esta en condiciones del habitat seleccionado, \nsi escribe 'si' en ambas es porque esta en condiciones, sino no lo esta.")
        bandera = 0
        if habitat == "desertico":
            aridez = st.selectbox(
                "¿El animal podrá vivir en un clima arido?",
                ("","si", "no"))
            tormentaArena = st.selectbox(
                "¿El animal soportaria tormentas de arena?",
                ("","si", "no"))
            if aridez == "si" and tormentaArena == "si":
                st.success("El animal puede agregarse")
                bandera = 1
                return bandera
        elif habitat == "acuatico":
            respiraAgua = st.selectbox(
                "¿El animal puede respirar bajo el agua?",
                ("","si", "no"))
            nadar = st.selectbox(
                "¿El animal sabe nadar?",
                ("","si", "no"))
            if respiraAgua == "si" and nadar == "si":
                st.success("El animal puede agregarse")
                bandera = 1
                return bandera
        elif habitat == "polar":
            clima = st.selectbox(
                "¿El animal hace parte de un clima de extrema baja temperatura y con mucha nieve?",
                ("","si", "no"))
            escasaVegetacion = st.selectbox(
                "¿El animal soportaria un entorno con escasa vegetacion?",
                ("","si", "no"))
            if clima == "si" and escasaVegetacion == "si":
                st.success("El animal puede agregarse")
                bandera = 1
                return bandera
        else:
            climaSelvatico = st.selectbox(
                "¿El animal hace parte de un clima calido y humedo?",
                ("","si", "no"))
            diversidad = st.selectbox(
                "¿El animal soportaria un entorno de vegetacion densa y con mucha diversidad biologica(arboles,plantas,insectos,animales)?",
                ("","si", "no"))
            if climaSelvatico == "si" and diversidad == "si":
                st.success("El animal puede agregarse")
                bandera = 1
                return bandera


    ## Este metodo recorre el vector de hábitat dentro de zoológico, mostrando así las hábitats existentes.
    def mostrarHabitats(self, habitats):
        st.divider()
        if len(habitats) > 0:
            with st.container():
                st.subheader("Listado de hábitats disponibles")
                if len(habitats) == 0:
                    st.error("No existe ningun hábitat")
                else:
                    datos = pd.DataFrame(
                        self.controlador.aplicarTabla(habitats),
                        columns=["Tipo de Hábitat", "Capacidad Máxima", "Temperatura del hábitat", "Dieta del hábitat","Clima","Atributo especial"]
                    )
                    st.table(datos)
        else:
            st.error("No hay hábitats en el zoológico")

    def mostrarAnimalesZoologico(self,animalesGuardados):
        st.divider()
        if len(animalesGuardados) > 0:
            with st.container():
                st.subheader("Listado de Animales en el Zoológico")
                if len(animalesGuardados) == 0:
                    st.error("No existe ningun Animal")
                else:
                    datos = pd.DataFrame(
                        self.controlador.aplicarTablaAnimales(animalesGuardados),
                        columns=["Id del animal", "Nombre", "Tipo de hábitat", "Edad", "Dieta",
                                 "Horas de sueño", "Temperatura"]
                    )
                    st.table(datos)
        else:
            st.error("No hay animales en el zoológico")


    def mostraMensajeError(self, mensaje):
        st.error(mensaje)

    def llamadoApi(self):
        listaImagenes = ["https://placebear.com/200/300.jpg","https://images.dog.ceo/breeds/basenji/n02110806_4117.jpg",
                   "https://images.dog.ceo/breeds/ovcharka-caucasian/IMG_20190801_112134.jpg"]
        for i in range(len(listaImagenes)):
            imagen = requests.get(listaImagenes[i])
            image = Image.open((BytesIO(imagen.content)))
            st.image(image, caption="Imagen de un animal")


