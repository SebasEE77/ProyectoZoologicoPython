from random import randint
import streamlit as st
class Animales:
    def __init__(self, id, nombre, habitat, edad, dieta, horasDormir,temperatura,estadoActivo,estadoJugar, atributoHabitat1, atributoHabitat2):
        self.id = id
        self.nombre = nombre
        self.tipoHabitat = habitat
        self.edad = edad
        self.dieta = dieta
        self. horasDormir = horasDormir
        self.temperatura = temperatura
        self.estadoActivo = estadoActivo
        self.estadoJugar = estadoJugar
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
        st.success("Se agrego la comida!")
        self.vectorDieta.append(comida)
        st.session_state["vectorDieta"] = self.vectorDieta


## Este método se encarga de lo relacionado a cambiar la dieta del animal, por eso se recibe como parametro
## una comida y una acción que significa si se quiere cambiar o eliminar de la dieta.
    def modificarDieta(self, accion, comida):
        bandera = 0
        i = 0
        if(accion == "modificar" or accion == "Modificar"):
            self.mostrarDietasDisponibles(self.dieta)
            nuevaComida = input("Ingrese la comida a cambiar por: " )
            while i < len(self.vectorDieta):
                if(self.vectorDieta[i] == comida and self.verificarComida(nuevaComida) == 1):
                    self.vectorDieta[i] = nuevaComida
                    bandera = 1
                i += 1

        elif (accion == "eliminar" or accion == "Eliminar"):
            while i < len(self.vectorDieta):
                if self.vectorDieta[i] == comida:
                    self.vectorDieta.pop(i)
                    bandera = 1
                i += 1

        if bandera == 0:
            print("La comida ", comida, " no se encontraba en la dieta")
        else:
            print("Accion valida!")


## Este método es el que se encarga de que el usuario interactué con un animal en
## específico jugando a adivinar un número aleatorio.
    def jugar(self):
        intentos = 3
        num = -1
        aleatorio = randint(1,10)
        print("Hola! Ahora vas a jugar con ", self.nombre)
        print("El juego consiste en que adivines un numero entre el 1 y el 10\n")
        print("Listo?")
        while num != aleatorio and intentos > 0:
            num = int(input("Escribe tu respuesta: "))
            if num == aleatorio:
                print("Has ganado!!, ", self.nombre, " esta feliz")
            else:
                print("Te has equivocado!")
                intentos -= 1
        if intentos == 0:
            print("El animal esta triste, no ganaste")

## Este metodo se encarga de darle de comer al animal de acuerdo a la acción escogida por el usuario. Se muestra la dieta del animal
## y se escoge la que haya disponible.
    def comer(self):
        bandera = 0
        if self.vectorDieta:
            self.mostrarDietaAnimal()
            comida = input("Ahora elige una comida para el animal de acuerdo a la dieta: ")
            while bandera == 0:
                if comida not in self.vectorDieta:
                    print("La comida que quieres agregar no hace parte de la dieta ")
                    comida = input("Ahora elige una comida para el animal de acuerdo a la dieta: ")
                else:
                    bandera = 1
            print("------------------")
            print("yummmmm ", self.nombre, " ha comido ", comida, " ,te lo agradece mucho")
        else:
            print("Lo sentimos pero no tienes nada agregado en la dieta del animal")

## Este metodo se encarga de mandar al animal a dormir si se especifica el número de horas exacta escritas
## a la hora de crear el animal.
    def dormir(self):
        horas = -1
        while horas != self.horasDormir:
            horas = int(input("Indica las horas para que el animal duerma: "))
            if horas > self.horasDormir:
                print("Son muchas horas para dormir!\n")
            elif horas < self.horasDormir:
                print("Son pocas horas para dormir!\n")
            else:
                print("El animal ya duerme tranquilo\n")
                self.estadoActivo = 0
