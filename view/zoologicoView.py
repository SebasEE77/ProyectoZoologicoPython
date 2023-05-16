import model.habitat as habitatModel
import controller.zoologicoController as ZoologicoController
import model.zoologico as zoologicoModel
import model.animales as animalesModel

## Esta clase se crea específicamente para mostrar el menu y se llamar los respectivos metodos desde el controlador.
class zoologicoView:

    def __init__(self):
        self.zoologico = zoologicoModel.zoologico()
        self.controlador = ZoologicoController.zoologicoController(self.zoologico, self)

    def mostrarMenu(self):
        print("Bienvenido al Zoologico de Cali")
        while True:
            print("\n\t**** Bienvenido al Zoologico de Cali ****\n")
            print("1. Agregar habitat al zoologico")
            print("2. Agregar un animal al zoologico")
            print("3. Ver lista de Habitats")
            print("4. Ver lista de animales del zoologico")
            print("5. Ver informacion sobre un animal")
            print("6. Menu de comidas")
            print("7. Interactuar con un animal")
            print("8. Salir")
            opcion = int(input("Por favor ingrese una opción: "))

            if opcion == 1:
                self.controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 2:
                self.controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 3:
                self.controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 4:
                self.controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 5:
                self.controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 6:
                self.controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 7:
                self.controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 8:
                print("Muchas gracias por visitarnos")
                break


##Creamos una función que pide por consola el nombre y varias características del hábitat a crear y luego verificamos que sea el correcto. Esta función se implementa
##en el view debido a que manejamos información para crear los hábitats. Al final se retorna el hábitat creado para guardar la información en la lista
    def menuCrearHabitat(self):
        print("Hola usuario, estas son las opciones para agregar habitats\n")
        print("\t->Habitats para agregar<-")
        print("-> desertico\n""-> selvatico\n" "-> polar\n" "-> acuatico\n")
        habitat = input("Escriba el habitat que desea agregar: ")
        bandera = 0
        while(bandera == 0):
            if (habitat != "desertico" and habitat != "selvatico" and habitat != "polar" and habitat != "acuatico"):
                print("Asegurate de colocar bien el tipo de habitat")
                habitat = input("Escriba el habitat que desea agregar: ")
            else:
                bandera = 1
        numAnimales = int(input("Escriba la cantidad de animales que pueda tener el habitat (Max 4 animales por habitat): "))
        while(bandera == 1):
            if(numAnimales < 1 or numAnimales > 4):
                print("Escribe nuevamente la cantidad maxima de animales")
                numAnimales = int(input("Escriba la cantidad de animales que pueda tener el habitat (Max 4 animales por habitat): "))
            else:
                bandera = 0
        print("\t->Rangos de temperatura<-")
        print("-> desertico: 30° - 40°\n""-> selvatico: 10° - 20°\n" "-> polar: -20° - -5°\n" "-> acuatico: 2° - 8°\n")
        temperatura = int(input("Escribe la temperatura del habitat de acuerdo con el rango de la pantalla: "))
        while(bandera == 0):
            if (habitat == "desertico" and (temperatura < 30 or temperatura > 40)):
                print("Escribe nuevamente la temperatura")
                temperatura = int(input("Escribe la temperatura del habitat: "))
            elif (habitat == "selvatico" and (temperatura < 10 or temperatura > 20)):
                print("Escribe nuevamente la temperatura")
                temperatura = int(input("Escribe la temperatura del habitat: "))
            elif (habitat == "polar" and (temperatura < -20 or temperatura > -5)):
                print("Escribe nuevamente la temperatura")
                temperatura = int(input("Escribe la temperatura del habitat: "))
            elif (habitat == "acuatico" and (temperatura < 2 or temperatura > 8)):
                print("Escribe nuevamente la temperatura")
                temperatura = int(input("Escribe la temperatura del habitat: "))
            else:
                bandera = 1
        print("\t->Dietas disponibles<-")
        print("-> carnivoro\n""-> herbivoro\n" "-> omnivoro\n")
        dietaAnimal = input("Escribe la dieta del habitat: ")
        while (bandera == 1):
            if (dietaAnimal != "carnivoro" and dietaAnimal != "herbivoro" and dietaAnimal != "omnivoro"):
                print("Asegurate de colocar bien la dieta")
                dietaAnimal = input("Escribe la dieta del habitat: ")
            else:
                bandera = 0
        if habitat == "desertico":
            print("\nTeniendo en cuenta que el habitat es desertico, se le atribuyen caracteristicas, "
                  "siendo un clima arido y un lugar donde hay tormentas de arena.\n")
            nuevaHabitat = habitatModel.desertico(habitat, numAnimales, temperatura, dietaAnimal, 0, "si", "si")
        elif habitat == "acuatico":
            print("\nTeniendo en cuenta que el habitat es acuatico, se le atribuyen caracteristicas, "
                  "siendo que se debe respirar bajo el agua y ser capaz de nadar.\n")
            nuevaHabitat = habitatModel.acuatico(habitat, numAnimales, temperatura, dietaAnimal, 0, "si", "si")
        elif habitat == "polar":
            print("\nTeniendo en cuenta que el habitat es polar, se le atribuyen caracteristicas, "
                  "siendo un clima con hielo y nieve y un lugar con escasa vegetacion.\n")
            nuevaHabitat = habitatModel.polar(habitat, numAnimales, temperatura, dietaAnimal, 0, "si", "si")
        else:
            print("\nTeniendo en cuenta que el habitat es selvatico, se le atribuyen caracteristicas, "
                  "siendo un clima calido y humedo y un lugar con mucha diversidad biologica.\n")
            nuevaHabitat = habitatModel.selvatico(habitat, numAnimales, temperatura, dietaAnimal, 0, "si", "si")

        return nuevaHabitat

##Creamos una función que pide por consola las distintas características del animal que se va agregar en el hábitat. Esta función se implementa
##en el view debido a que manejamos información para crear los animales. Al final se retorna el hábitat creado para guardar la información en una lista vacía

    def menuCrearAnimales(self):
        bandera = 0

        print("Hola usuario, escribe las caracteristicas del animal que quieres crear\n")
        id = int(input("Escribe el id del animal: "))
        nombre = input("Escribe el nombre del animal: ")
        print("\t->Habitats para agregar<-")
        print("-> desertico\n""-> selvatico\n" "-> polar\n" "-> acuatico\n")
        habitat = input("Escriba el habitat al que pertenece el animal: ")
        while (bandera == 0):
            if (habitat != "desertico" and habitat != "selvatico" and habitat != "polar" and habitat != "acuatico"):
                print("Asegurate de colocar bien el tipo de habitat")
                habitat = input("Escriba el habitat que desea agregar: ")
            else:
                bandera = 1
        print("-> La edad debe ser entre los 0 - 15 años")
        edad = int(input("Escribe la edad del animal: "))
        while (bandera == 1):
            if (edad < 0 or edad > 15):
                print("Escribe otra vez la edad")
                edad = int(input("Escribe la edad del animal: "))
            else:
                bandera = 0
        print("\t->Dietas disponibles<-")
        print("-> carnivoro\n""-> herbivoro\n" "-> omnivoro\n")
        dieta = input("Escriba el tipo de alimentacion: ")
        while (bandera == 0):
            if (dieta != "carnivoro" and dieta != "herbivoro" and dieta != "omnivoro"):
                print("Asegurate de colocar bien la alimentacion")
                dieta = input("Escriba el tipo de alimentacion: ")
            else:
                bandera = 1
        print("\t->Rangos de temperatura<-")
        print("-> desertico: 30° - 40°\n""-> selvatico: 10° - 20°\n" "-> polar: -20° - -5°\n" "-> acuatico: 2° - 8°\n")
        temperatura = int(input("Escribe la temperatura que puede soportar el animal: "))
        print("-> Las horas de dormir deben ser entre 5 - 20 horas")
        horasDormir = int(input("Escribe las horas de dormir del animal: "))
        while (bandera == 0):
            if (horasDormir < 5 or horasDormir > 20):
                print("Escribe bien las horas de dormir")
                horasDormir = int(input("Escribe las horas de dormir del animal: "))
            else:
                bandera = 1
        print("\nA continuacion se realizara dos preguntas cerradas para saber si el animal "
              "esta en condiciones del habitat seleccionado, \nsi escribe 'si' en ambas es porque esta en condiciones, sino no lo esta.")
        if habitat == "desertico":
            print("El animal podria vivir en un clima arido?")
            print("\n->si")
            print("->no")
            aridez = input("Escribe la respuesta: ")
            print("El animal soportaria tormentas de arena?")
            print("\n->si")
            print("->no")
            tormentaArena = input("Escribe la respuesta: ")
            nuevoAnimal = animalesModel.animales(id,nombre,habitat,edad,dieta,horasDormir,temperatura,1,0,aridez,tormentaArena)
        elif habitat == "acuatico":
            print("El animal puede respirar bajo el agua?")
            print("\n->si")
            print("->no")
            respiraAgua = input("Escribe la respuesta: ")
            print("El animal sabe nadar?")
            print("\n->si")
            print("->no")
            nadar = input("Escribe la respuesta: ")
            nuevoAnimal = animalesModel.animales(id, nombre, habitat, edad, dieta, horasDormir, temperatura, 1, 0,
                                                 respiraAgua, nadar)
        elif habitat == "polar":
            print("El animal hace parte de un clima de extrema baja temperatura y con mucha nieve?")
            print("\n->si")
            print("->no")
            clima = input("Escribe la respuesta: ")
            print("El animal soportaria un entorno con escasa vegetacion?")
            print("\n->si")
            print("->no")
            escasaVegetacion = input("Escribe la respuesta: ")
            nuevoAnimal = animalesModel.animales(id, nombre, habitat, edad, dieta, horasDormir, temperatura, 1, 0,
                                                 clima, escasaVegetacion)
        else:
            print("El animal hace parte de un clima calido y humedo?")
            print("\n->si")
            print("->no")
            climaSelvatico = input("Escribe la respuesta: ")
            print("El animal soportaria un entorno de vegetacion densa y con mucha diversidad biologica(arboles,plantas,insectos,animales)?")
            print("\n->si")
            print("->no")
            diversidad = input("Escribe la respuesta: ")
            nuevoAnimal = animalesModel.animales(id, nombre, habitat, edad, dieta, horasDormir, temperatura, 1, 0,
                                                 climaSelvatico, diversidad)
        return nuevoAnimal

## Estos dos métodos son auxiliares para poder verificar si realmente el animal exite pidiendo el id y el hábitat.
    def opcionAuxiliar1(self):
        id = int(input("Indique el id del animal: "))
        return id
    def opcionAuxiliar2(self):
        tipoHabitat = input("Indique el habitat del animal: ")
        return tipoHabitat


