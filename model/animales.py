from random import randint
import streamlit as st
class Animales:
    #Constructor de la clase animal
    def __init__(self, id, nombre, habitat, edad, dieta, horasDormir,temperatura,estadoActivo,estadoJugar, atributoHabitat1, atributoHabitat2,intentosJugar):
        self.id = id
        self.nombre = nombre
        self.tipoHabitat = habitat
        self.edad = edad
        self.dieta = dieta
        self. horasDormir = horasDormir
        self.temperatura = temperatura
        self.estadoActivo = estadoActivo
        self.estadoJugar = estadoJugar
        self.intentosJugar = intentosJugar
        self.atributoHabitat1 = atributoHabitat1
        self.atributoHabitat2 = atributoHabitat2
        self.arregloCarnivoro = ["leche", "pescado", "pechuga", "gusanos", "ave", "huevos"]
        self.arregloHerbivoro = ["hierbas", "hojas", "savia", "raices", "semillas", "flores"]
        self.arregloOmnivoro = ["frutas", "carne", "vegetales", "plantas", "higado", "verduras"]
        if "vectorDieta" in st.session_state:
            self.vectorDieta = st.session_state["vectorDieta"]
        else:
            self.vectorDieta = []
            st.session_state["vectorDieta"] = []

## Aquí muestra las comidas dentro de la lista dieta del animal.
    def mostrarDietaAnimal(self):
        i = 0
        if self.vectorDieta:
            st.subheader("La dieta del animal es:")
            while i < len(self.vectorDieta):
                st.write("Comida: ", self.vectorDieta[i])
                i += 1
        else:
            st.warning("Por el momento no tiene dieta :(")

    #Este metodo retorna el vector tipo dieta
    def modificarDietaInfo(self):
        return self.vectorDieta


## Este metodo se encarga de mostrar las posible comidas para el animal de acuerdo a su dieta, las cuales
## están dentro determinadas dentro de arreglos.
    def mostrarDietasDisponibles(self, dieta):
        st.divider()
        st.subheader("\t->Para el animal esta disponible la siguiente dieta<-")
        i = 0
        if dieta == "carnivoro" or dieta == "Carnivoro":
            while i < len(self.arregloCarnivoro):
                st.write("- ", self.arregloCarnivoro[i])
                i += 1
        elif dieta == "Herbivoro" or dieta == "herbivoro":
            while i < len(self.arregloHerbivoro):
                st.write("- ", self.arregloHerbivoro[i])
                i += 1
        else:
            while i < len(self.arregloOmnivoro):
                st.write("- ", self.arregloOmnivoro[i])
                i += 1

## Este metodo verificar que la comida que se pase como parametro este dentro de la opciones de dieta, y que esté
## en los arreglos de los 3 tipos de dieta.
    def verificarComida(self,comida):
        bandera = 0
        if comida not in self.vectorDieta:
            if comida in self.arregloCarnivoro or comida in self.arregloHerbivoro\
                    or comida in self.arregloOmnivoro:
                bandera = 1
                return bandera
        else:
            st.warning("La comida que quieres agregar ya esta en la dieta del animal")

        return bandera

## Este método se encarga solo de meter la comida dentro de la lista dieta del animal.
    def agregarComida(self, comida):
        if comida not in self.vectorDieta:
            st.success("Se agrego la comida!")
            self.vectorDieta.append(comida)
            st.session_state["vectorDieta"] = self.vectorDieta
        else:
            st.error("La comida que quieres agregar ya esta en la dieta del animal")


## Este método se encarga de lo relacionado a cambiar la dieta del animal, por eso se recibe como parametro
## una comida y una acción que significa si se quiere cambiar o eliminar de la dieta.
    def modificarDieta(self, accion,comida):
        i = 0
        if self.vectorDieta:
            if accion == "modificar":
                self.mostrarDietasDisponibles(self.dieta)
                nuevaComida = st.text_input("Ingrese la comida a cambiar por:")
                accion = st.button("Modificar")
                if accion:
                    while i < len(self.vectorDieta):
                        if(self.vectorDieta[i] == comida and self.verificarComida(nuevaComida) == 1):
                            self.vectorDieta[i] = nuevaComida
                            st.success("La modificación fue exitosa")
                        i += 1
        else:
            st.error("No hay dieta")


## Este método es el que se encarga de que el usuario interactué con un animal en
## específico jugando a adivinar un número aleatorio.
    def jugar(self):
        aleatorio = randint(1,10)
        st.subheader("Hola! Ahora vas a jugar con el animal que seleccionaste")
        st.write("El juego consiste en que adivines un numero entre el 1 y el 10\n")
        st.write("Listo?")
        num = st.selectbox("Escoge tu respuesta:", ("", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), key=20)
        intento = st.button("Intentar")
        if intento:
            self.intentosJugar -= 1
            if num == aleatorio:
                st.success("Has ganado!!, ahora el animal esta feliz")
                self.estadoJugar = 1
            elif num != aleatorio and self.intentosJugar > 0:
                st.warning("Te has equivocado!")
        if self.intentosJugar == 0 and num != aleatorio:
            st.error("Has perdido!, el animal esta triste :(")
            self.estadoJugar = 1
            self.intentosJugar = 3

    ## Este metodo se encarga de darle de comer al animal de acuerdo a la acción escogida por el usuario. Se muestra la dieta del animal
## y se escoge la que haya disponible.
    def comer(self):
        if self.vectorDieta:
            self.mostrarDietaAnimal()
            comida = st.text_input("Ahora elige una comida para el animal de acuerdo a la dieta:")
            comer = st.button("Darle de comer")
            if comer:
                if comida in self.vectorDieta:
                    st.success("yummmmm, el animal ha comido y te lo agradece mucho")
                else:
                    st.warning("La comida que quieres agregar no hace parte de la dieta")
        else:
            st.error("Lo sentimos pero no tienes nada agregado en la dieta del animal")

## Este metodo se encarga de mandar al animal a dormir si se especifica el número de horas exacta escritas
## a la hora de crear el animal.
    def dormir(self):
        horas = st.number_input("Indica las horas para que el animal duerma:", min_value=1,max_value=20)
        dormir = st.button("Poner a dormir al animal")
        if dormir:
            if horas > self.horasDormir:
                st.warning("Son muchas horas para dormir!")
            elif horas < self.horasDormir:
                st.warning("Son pocas horas para dormir!")
            else:
                self.estadoActivo = 0
                st.success("El animal ya duerme tranquilo")