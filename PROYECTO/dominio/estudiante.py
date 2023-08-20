#ALVARADO VALDIVIEZO MARIA GABRIELA
#CHIRIGUAYA ROMAN MARJORIE PAMELA
#MENDOZA LOAIZA DAYANA VALENTINA
#TACLE PAREDES DESSIRE IVONNE
from PROYECTO.dominio.persona import Persona


class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula: str=None, nombre: str=None, apellido: str=None, email: str=None, telefono: str=None, direccion: str=None,
                 numero_libros: int=0, activo: bool=True, carrera: str=None, nivel: int=1, estatura=None, peso=None, fechanacimiento=None, edad=None):
        Estudiante.contador_estudiante += 1
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._id = Estudiante.contador_estudiante
        self._nivel = nivel
        super(Estudiante, self).__init__(cedula=cedula, nombre=nombre, apellido=apellido, email=email, telefono=telefono,
                                direccion=direccion, numero_libros=numero_libros,activo=activo, carrera=carrera, estatura= estatura,peso=peso, fechanacimiento=fechanacimiento, edad=edad)

    def __str__(self):
        return f' Estudiante : {self.__dict__.__str__()}'

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel
    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass

if __name__ == '__main__':
    Estudiante1 = Estudiante(cedula='0924956311', nombre='Dessire', apellido='Tacle', email='desitacle@gmail.com',
                    telefono='0994367826', direccion='Brisas del Norte', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    Estudiante2 = Estudiante(cedula='0923156748', nombre='Gabriela', apellido='Alvarado', email='Gabyalvarado@gmail.com',
                    telefono='0987656788', direccion='Mall del Sol', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    Estudiante3 = Estudiante(cedula='0934257865', nombre='Dayana', apellido='Mendoza', email='Dayamendoza@gmail.com',
                    telefono='0987889700', direccion='Duran', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    Estudiante4= Estudiante(cedula='0929404572', nombre='Marjorie', apellido='Chiriguaya', email='Marjo.chiriguaya@gmail.com',
                    telefono='0997597299', direccion='Santa Lucia', numero_libros=0, activo=True, carrera='GIG',nivel = 3)

    print(Estudiante1)
    print(Estudiante2)
    print(Estudiante3)
    print(Estudiante4)