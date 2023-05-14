from random import randint
class animales:
    def __init__(self, id, nombre, habitat, edad, dieta, horasDormir,temperatura,estadoActivo,estadoJugar, atributoHabitat1, atributoHabitat2):
        self.id = id
        self.nombre = nombre
        self.habitat = habitat
        self.edad = edad
        self.dieta = dieta
        self. horasDormir = horasDormir
        self.temperatura = temperatura
        self.estadoActivo = estadoActivo
        self.estadoJugar = estadoJugar
        self.atributoHabitat1 = atributoHabitat1
        self.atributoHabitat2 = atributoHabitat2
        self.arregloCarnivoro = ["carne", "pescado", "pechuga", "gusanos", "ave", "huevos"]
        self.arregloHerbivoro = ["hierbas", "hojas", "savia", "raices", "semillas", "flores"]
        self.arregloOmnivoro = ["frutas", "carne", "vegetales", "plantas", "pescado", "verduras"]
        self.vectorDieta = []

    def mostrarDietaAnimal(self):
        i = 0
        if self.vectorDieta:
            print("La dieta del animal ", self.nombre, " es: ")
            while i < len(self.vectorDieta):
                print("Comida: ", self.vectorDieta[i])
                i += 1
        else:
            print("Por el momento no tiene dieta :(")



    def mostrarDietasDisponibles(self, dieta):
        print("\t->Para el animal esta disponible la siguiente dieta<-")
        i = 0
        if (dieta == "carnivoro" or dieta == "Carnivoro"):
            while i < len(self.arregloCarnivoro):
                print("- ", self.arregloCarnivoro[i])
                i += 1
        elif (dieta == "Herbivoro" or dieta == "herbivoro"):
            while i < len(self.arregloHerbivoro):
                print("- ", self.arregloHerbivoro[i])
                i += 1
        else:
            while i < len(self.arregloOmnivoro):
                print("- ", self.arregloOmnivoro[i])
                i += 1

    def verificarComida(self,comida):
        bandera = 0
        if comida not in self.vectorDieta:
            if comida in self.arregloCarnivoro or comida in self.arregloHerbivoro\
                    or comida in self.arregloOmnivoro:
                bandera = 1
                return bandera
        else:
            print("La comida que quieres agregar ya esta en la dieta del animal")

        return bandera

    def agregarComida(self, comida):
        self.vectorDieta.append(comida)
        print("Se agrego la comida!\n")

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
