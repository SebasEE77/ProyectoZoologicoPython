class animales:
    def __init__(self, id, nombre, habitat, edad, dieta, horasDormir,temperatura):
        self.id = id
        self.nombre = nombre
        self.habitat = habitat
        self.edad = edad
        self.dieta = dieta
        self. horasDormir = horasDormir
        self.temperatura = temperatura

    def imprimirAnimales(self):
        print("Nombre: ", self.nombre)
        print("Habitat: ", self.habitat)

    def imprimirAnimalInfo(self):
        print("Id: ", self.id)
        print("Nombre: ", self.nombre)
        print("Habitat: ", self.habitat)
        print("Edad: ", self.edad)
        print("Alimentacion: ", self.dieta)
        print("Horas de dormir: ", self.horasDormir)
        print("Temperatura del animal: ", self.temperatura)

