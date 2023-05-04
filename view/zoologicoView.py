import model.habitat as habitatModel
import controller.zoologicoController as ZoologicoController
import model.zoologico as zoologicoModel

class zoologicoView:
    def mostrarMenu(self):
        print("Bienvenido al Zoologico de Cali")
        opcion = 0
        zoologico = zoologicoModel.zoologico()
        controlador = ZoologicoController.zoologicoController(zoologico,self)
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
                controlador.ejecutarOpcionHabitat(opcion)
            elif opcion == 3:
                controlador.ejecutarOpcionHabitat(opcion)


    def menuCrearHabitat(self):
        habitat = input("Escriba el habitat: ")
        nuevaHabitat = habitatModel.habitat(habitat)
        return nuevaHabitat

