class Persona:
    def __init__(self,paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion):
        self.nombre = paramNombre
        self.apellido = paramApellido
        self.email = paramEmail
        self.telefono = paramTelefono
        self.direccion = paramDireccion

class Profesor(Persona):
    def __init__(self,paramProfLegajo,paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion):
        self.idProf = paramProfLegajo
        super().__init__(paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion)

profesorDanielQuinteros = Profesor(45232,"Daniel","Quinteros","Daniel@um.edu.ar","261.343.2543","Godoy Cruz")
profesorDanielLillo = Profesor(56434,"Daniel","Lillo","Lillo@um.edu.ar","261.543.6532","Godoy Cruz")

class Alumno(Persona):
    def __init__ (self,paramLegajo,paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion):
        self.legajo = paramLegajo
        super().__init__(paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion)

alumnoLeandroFlores = Alumno("Leandro","Flores","lf.flores@alumno.um.edu.ar",59177,"261.302.5653","25 de mayo 86")
alumnoTomiRojas = Alumno("Tomas","Rojas","tomi@sexo.um.edu.ar",59234,"2616666666","Sexo Land")

class Materia:
    def __init__(self,paramIdMat,paramNombreMat,paramHorario,paramPeriodo):
        self.idMat = paramIdMat
        self.nombreMat = paramNombreMat
        self.horarioMat = paramHorario
        self.periodoMat = paramPeriodo

materiaComputacion = Materia(4567,"Computacion","Martes de 8:00 a 12:00","Anual")
materiaAnalisisII = Materia(4890,"Analisis de Sistemas II","Lunes de 10:30 a 13:30","Semestral")


if __name__ == "__main__":
    pass
