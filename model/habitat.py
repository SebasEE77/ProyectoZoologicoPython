class habitat:
    def __init__(self, tipoHabitat, numAnimales, temperatura,dieta):
        self.habitat = tipoHabitat
        self.numAnimales = numAnimales
        self.temperatura = temperatura
        self.dieta = dieta
        self.animales = []


    def imprimirHabitat(self):
        print("Habitat: ",self.habitat)
        print("Capacidad maxima: ",self.numAnimales)
        print("Temperatura: ",self.temperatura)
        print("Dieta: ",self.dieta)
        print("\n")

    def agregarAnimales(self, nuevoAnimal):
        bandera = 0
        for animales in self.animales:
            if animales.id == nuevoAnimal.id:
                bandera = 1
                print("No es posible agregar el animal por el id escrito")

        if (bandera == 0):
            self.animales.append(nuevoAnimal)
            print("Se agrego el animal correctamente")

    def mostrarAnimales(self):
        if self.animales:
            for animales in self.animales:
                print("-------------------------")
                print("id: ", animales.id)
                print("Nombre: ", animales.nombre)
                print("Habitat: ", animales.habitat)
                print("-------------------------")

        else:
            print("No hay animales por el momento")

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
                        accion = int(input("Escoja su opcion"))
                        while banderaVerificacion == 1:
                           if accion != 1 or accion != 2:
                               accion = int(input("Escoja su opcion"))
                        if accion == 1:
                            animales.jugar()
                        else:
                            animales.estadoJugar = 0
                    else:
                        animales.jugar()

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
