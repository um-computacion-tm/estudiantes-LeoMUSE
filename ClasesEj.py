class Profesor:
    def __init__(self, param_nombre,param_apellido):
        self.nombre = param_nombre
        self.apellido = param_apellido
        self.asistencia = 0

    def asistencia_clase(self):
        self.asistencia += 1
        


profesor_pepe = Profesor("pepe","pito")
#profesor_walter = Profesor()
#profesor_daniel = Profesor()

print(id(profesor_pepe))
print(profesor_pepe.nombre)
print(profesor_pepe.apellido)

if __name__ == "__main__":
    pass
