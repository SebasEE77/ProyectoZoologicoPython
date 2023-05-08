class animales:
    def __init__(self, id, nombre, tipoHabitat, edad, alimentacion, horasDormir):
        self.id = id
        self.nombre = nombre
        self.tipoHabitat = tipoHabitat
        self.edad = edad
        self.alimentacion = alimentacion
        self. horasDormir = horasDormir

    def imprimirAnimal(self):
        print("Nombre: ", self.nombre)
        print("Habitat: ", self.tipoHabitat)

    def imprimirAnimalesInfo(self):
        print("Id: ", self.id)
        print("Nombre: ", self.nombre)
        print("Habitat: ", self.tipoHabitat)
        print("Edad: ", self.edad)
        print("Alimentacion: ", self.alimentacion)
        print("Horas de dormir: ", self.horasDormir)
