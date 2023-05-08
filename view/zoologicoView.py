import model.habitat as habitatModel
import controller.zoologicoController as ZoologicoController
import model.zoologico as zoologicoModel
import controller.habitatController as HabitatController
import model.animales as animalesModel

class zoologicoView:
    def mostrarMenu(self):
        print("Bienvenido al Zoologico de Cali")
        zoologico = zoologicoModel.zoologico()
        animales = animalesModel.animales()
        controladorhabitat = HabitatController.habitatController(animales,self)
        controladorZoologico = ZoologicoController.zoologicoController(zoologico,self)
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
                controladorZoologico.ejecutarOpcionHabitat(opcion)
            elif opcion == 2:
                controladorhabitat.ejecutarOpcionAnimales(opcion)
            elif opcion == 3:
                controladorZoologico.ejecutarOpcionHabitat(opcion)


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
        numAnimales = input("Escriba la cantidad de animales que pueda tener el habitat (Max 4 animales por habitat): ")
        print("-> desertico: 30° - 40°\n""-> selvatico: 10° - 20°\n" "-> polar: -5° - -20°\n" "-> acuatico: 2° - 8°\n")
        temperatura = input("Escribe la temperatura del habitat: ")
        print("-> carnivoro\n""-> herbivoro\n" "-> omnivoro\n")
        dietaAnimal = input("Escribe la dieta del habitat: ")

        nuevaHabitat = habitatModel.habitat(habitat, numAnimales, temperatura, dietaAnimal)
        return nuevaHabitat

    def menuCrearAnimales(self):
        print("Hola usuario, escribe las caracteristicas del animal que quieres crear\n")
        id = input("Escribe el id del animal: ")
        nombre = input("Escribe el nombre del animal: ")
        print("-> desertico\n""-> selvatico\n" "-> polar\n" "-> acuatico\n")
        tipoHabitat = input("Escriba el habitat al que pertenece el animal: ")
        print("-> La edad debe ser entre los 0 - 15 años")
        edad = input("Escribe la edad del animal: ")
        print("-> carnivoro\n""-> herbivoro\n" "-> omnivoro\n")
        alimentacion = input("Escriba el tipo de alimentacion: ")
        print("-> Las horas de dormir deben ser entre 5 - 20 horas")
        horasDormir = input("Escribe las horas de dormir del animal: ")

        nuevoAnimal = animalesModel.animales(id,nombre,tipoHabitat,edad,alimentacion,horasDormir)
        return nuevoAnimal

