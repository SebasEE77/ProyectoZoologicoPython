import model.habitat as habitatModel
import controller.zoologicoController as ZoologicoController
import model.zoologico as zoologicoModel
import model.animales as animalesModel

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



    def menuCrearHabitat(self):
        print("Hola usuario, estas son las opciones para agregar habitats\n")
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
        print("-> carnivoro\n""-> herbivoro\n" "-> omnivoro\n")
        dietaAnimal = input("Escribe la dieta del habitat: ")
        while (bandera == 1):
            if (dietaAnimal != "carnivoro" and dietaAnimal != "herbivoro" and dietaAnimal != "omnivoro"):
                print("Asegurate de colocar bien la dieta")
                dietaAnimal = input("Escribe la dieta del habitat: ")
            else:
                bandera = 0
        nuevaHabitat = habitatModel.habitat(habitat, numAnimales, temperatura, dietaAnimal)
        return nuevaHabitat

    def menuCrearAnimales(self):
        bandera = 0
        print("Hola usuario, escribe las caracteristicas del animal que quieres crear\n")
        id = int(input("Escribe el id del animal: "))
        nombre = input("Escribe el nombre del animal: ")
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
        print("-> carnivoro\n""-> herbivoro\n" "-> omnivoro\n")
        dieta = input("Escriba el tipo de alimentacion: ")
        while (bandera == 0):
            if (dieta != "carnivoro" and dieta != "herbivoro" and dieta != "omnivoro"):
                print("Asegurate de colocar bien la alimentacion")
                dieta = input("Escriba el tipo de alimentacion: ")
            else:
                bandera = 1
        print("-> desertico: 30° - 40°\n""-> selvatico: 10° - 20°\n" "-> polar: -20° - -5°\n" "-> acuatico: 2° - 8°\n")
        temperatura = int(input("Escribe la temperatura que puede soportar el animal: "))
        while (bandera == 1):
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
                bandera = 0
        print("-> Las horas de dormir deben ser entre 5 - 20 horas")
        horasDormir = int(input("Escribe las horas de dormir del animal: "))
        while (bandera == 0):
            if (horasDormir < 5 or horasDormir > 20):
                print("Escribe bien las horas de dormir")
                horasDormir = int(input("Escribe las horas de dormir del animal: "))
            else:
                bandera = 1
        nuevoAnimal = animalesModel.animales(id,nombre,habitat,edad,dieta,horasDormir,temperatura,1,0)
        return nuevoAnimal

    def opcionAuxiliar1(self):
        id = int(input("Indique el id del animal: "))
        return id
    def opcionAuxiliar2(self):
        tipoHabitat = input("Indique el habitat del animal: ")
        return tipoHabitat



