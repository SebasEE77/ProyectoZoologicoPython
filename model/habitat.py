class habitat:
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta,contadorAnimales):
        self.habitat = tipoHabitat
        self.numAnimales = numAnimales
        self.temperatura = temperatura
        self.dieta = dieta
        self.contadorAnimales = contadorAnimales
        self.animales = []

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
        self.contadorAnimales += 1
        for animales in self.animales:
            if animales.id == nuevoAnimal.id:
                bandera = 1
                print("No es posible agregar el animal por el id escrito")

        if self.contadorAnimales > self.numAnimales:
            bandera = 1
            print("No es posible agregar ya que no hay disponiblidad")

        if (bandera == 0):
            self.animales.append(nuevoAnimal)
            print("Se agrego el animal correctamente")

## Este método lo que hace es listar los animales dentro de la lista animales mostrando su id, nombre y tipo de hábitat,
## además, si no existe ningun animal se muestra el mensaje indicando que no existen.
    def mostrarAnimales(self):
        for animales in self.animales:
            if self.animales:
                print("-------------------------")
                print("id: ", animales.id)
                print("Nombre: ", animales.nombre)
                print("Habitat: ", animales.habitat)
                print("-------------------------")

            else:
                print("No hay animales por el momento")


## Este método se encarga de mostrar la información completa del animal de acuerdo al id pasado como parametro de la función. Aquí se busca
## dentro de la lista animales del habitat que encuentra buscarAnimal de la clase zoologico.
    def mostrarAnimalInfo(self,id):
        bandera = 0
        for animales in self.animales:
            if animales.id == id:
                print("\t ->Esta es la  ficha de informacion del animal<-")
                print("Id: ", animales.id)
                print("Nombre: ", animales.nombre)
                print("Habitat: ", animales.habitat)
                print("Edad: ", animales.edad)
                print("Alimentacion: ", animales.dieta)
                print("Horas de dormir: ", animales.horasDormir)
                print("Temperatura del animal: ", animales.temperatura)
                bandera = 1

        if bandera == 0:
            print("El animal no pertenece al zoologico")

## Este metodo lo que se encarga es de buscar al animal dentro de la lista animales de acuerdo a su id para de tal modo gestionar la dieta del animal,
## ya sea agregar una comida, cambiarla por otra o eliminarla de su dieta.
    def dietaVectoresAnimales(self,id):
        bandera = 0
        banderaVerificacion = 0
        for animales in self.animales:
            if animales.id == id:
                print("Bienvenido al menu de dieta para los animales del Zoo\n")
                print("->[1]. Ver la dieta del animal\n")
                print("->[2]. Agregar comida a la dieta del animal\n")
                print("->[3]. Modificar/Eliminar comida de la dieta del animal\n")
                opcion = int(input("Elige una opcion: "))
                while(banderaVerificacion == 0):
                    if(opcion < 1 or opcion > 3):
                        opcion = int(input("Elige una opcion: "))
                    else:
                        banderaVerificacion = 1
                if opcion == 1:
                    animales.mostrarDietaAnimal()
                    bandera = 1
                elif opcion == 2:
                    bandera = 1
                    dieta = animales.dieta
                    animales.mostrarDietasDisponibles(dieta)
                    print("-----------------------------------------")
                    comida = input("Elige una comida de la lista para el animal: ")
                    while animales.verificarComida(comida) == 0:
                        comida = input("Elige otra comida de la lista para el animal: ")
                    animales.agregarComida(comida)
                else:
                    bandera = 1
                    print("->[1]. Modificar\n")
                    print("->[2]. Eliminar\n")
                    accion = int(input("->Escoge una opcion<-\n"))
                    while banderaVerificacion == 1:
                        if accion < 1 or accion > 2:
                            accion = int(input("->Escoge una opcion<-\n"))
                        else:
                            banderaVerificacion = 0

                    if accion == 1:
                        animales.mostrarDietaAnimal()
                        comida = input("Ingrese la comida que quisiera modificar: ")
                        animales.modificarDieta("modificar", comida)
                    else:
                        animales.mostrarDietaAnimal()
                        comida = input("Ingrese la comida que quisieras eliminar: ")
                        animales.modificarDieta("eliminar", comida)

        if(bandera == 0):
            print("El animal indicado no existe\n")

## Este metodo se encargara de buscar al animal dentro del hábitat de acuerdo al id mandado como parametro. Luego pedira al usuario que escoga
## una opción para interactuar con el animal, ya sea jugar, dormir o comer.
    def interactuarAnimal(self, id):
        bandera = 0
        banderaVerificacion = 0
        for animales in self.animales:
            if animales.id == id:
                print("Gracias por querer interactuar con nuestros animales!")
                print("->[1]. Jugar\n" "->[2]. Comer\n" "->[3]. Dormir\n")
                opcion = int(input("Elige la accion que quieras hacer: "))
                while (banderaVerificacion == 0):
                    if (opcion < 1 or opcion > 3):
                        opcion = int(input("Elige una opcion: "))
                    else:
                        banderaVerificacion = 1
                if opcion == 1:
                    if animales.estadoActivo == 0:
                        print("El animal esta dormiendo en este momento")
                    elif animales.estadoJugar == 1:
                        print("El animal ya ha jugado. Desea jugar con él?")
                        print("->[1]. Si\n" "->[2]. No\n")
                        accion = int(input("Escoja su opcion: "))
                        while banderaVerificacion == 1:
                            if (accion < 1 or accion > 2):
                                accion = int(input("Escoja su opcion: "))
                            else:
                                banderaVerificacion = 0
                        if accion == 1:
                            animales.jugar()
                        else:
                            animales.estadoJugar = 0
                    else:
                        animales.jugar()
                        animales.estadoJugar = 1

                elif opcion == 2:
                    if animales.estadoActivo == 0:
                        print("El animal esta dormiendo en este momento")
                    else:
                        animales.comer()

                else:
                    if animales.estadoActivo == 0:
                        print("Se desperto el animal")
                        animales.estadoActivo = 1
                    else:
                        animales.dormir()
                bandera = 1

        if bandera == 0:
            print("El animal no existe")


## Apartir de aquí están las clases hijas de la clase hábitat las cuales tienen 2 atributos únicos que los diferencian
## de las demás hábitats del zoológico. Cada una tiene un imprimirHabitat y un imprimirAnimales que lo que hacen es añadir
## información extra a esos métodos.
class desertico(habitat):
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

    def mostrarAnimalInfo(self,id):
        super().mostrarAnimalInfo(id)
        for animales in self.animales:
            print("Clima Arido: ", animales.atributoHabitat1)
            print("Hay tormentas de arena: ", animales.atributoHabitat2)

class acuatico(habitat):
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

    def mostrarAnimalInfo(self,id):
        super().mostrarAnimalInfo(id)
        for animales in self.animales:
            print("Puede respirar bajo el agua: ", animales.atributoHabitat1)
            print("Puede nadar: ", animales.atributoHabitat2)

class polar(habitat):
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

    def mostrarAnimalInfo(self,id):
        super().mostrarAnimalInfo(id)
        for animales in self.animales:
            print("Soporta extremas temperaturas: ", animales.atributoHabitat1)
            print("Soporta un ecosistema con escasa vegetacion: ", animales.atributoHabitat2)

class selvatico(habitat):
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

    def mostrarAnimalInfo(self,id):
        super().mostrarAnimalInfo(id)
        for animales in self.animales:
            print("Soporta el clima calido y humedo: ", animales.atributoHabitat1)
            print("Soporta la densa vegetacion y la diversidad biologica: ", animales.atributoHabitat2)