#ALVARADO VALDIVIEZO MARIA GABRIELA
#CHIRIGUAYA ROMAN MARJORIE PAMELA
#MENDOZA LOAIZA DAYANA VALENTINA
#TACLE PAREDES DESSIRE IVONNE
from PROYECTO.dominio.persona import Persona

class Docente(Persona):

    contador_docente = 0

    def __init__(self ,cedula :str=None ,nombre :str=None ,apellido :str=None ,email :str=None ,telefono :str=None ,direccion :str=None
                 ,numero_libros :int=0 ,activo :bool=True ,carrera :str=None, titulo_3er_nivel :str=None ,titulo_4to_nivel :str=None):

        Docente.contador_docente +=1
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._id = Docente.contador_docente
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        super(Docente, self).__init__(cedula = cedula, nombre = nombre, apellido= apellido, email=email, telefono=telefono, direccion=direccion, numero_libros=numero_libros, activo=activo, carrera=carrera)

    def __str__ (self):
        return f' Docente : {self.__dict__.__str__()}'
    @property
    def id (self):
        return self._id

#3er nivel
    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel
    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, titulo_3er_nivel):
        self._titulo_3er_nivel = titulo_3er_nivel
#4to nivel
    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel
    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, titulo_4to_nivel):
        self._titulo_4to_nivel = titulo_4to_nivel

    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass

if __name__ == '__main__':
    Docente1 = Docente(cedula='0932260755', nombre='PAUL', apellido='BENAVIDES', email='pbenavides@gmail.com',
                       telefono='0982260755', direccion='VERNAZA NORTE', numero_libros=0, activo=True, carrera='DERECHO',
                       titulo_3er_nivel='LCDO', titulo_4to_nivel=',DOC')
    Docente2 = Docente(cedula='0911340556', nombre='JOAN', apellido='ALVARADO', email='jalvarado@gmail.com',
                       telefono='0960540817', direccion='VERNAZA NORTE', numero_libros=0, activo=True, carrera='PSICOLOGIA',
                       titulo_3er_nivel='LCDO', titulo_4to_nivel=',PHD')
    Docente3 = Docente(cedula='0913167548', nombre='LEONEL', apellido='GUERRERO', email='lguerrero@gmail.com',
                       telefono='0959747318', direccion='SAUCES 6', numero_libros=0, activo=True, carrera='GESTION DE LA INFORMACION GERENCIAL',
                       titulo_3er_nivel='LCDO', titulo_4to_nivel=',DOC')

    Docente4 = Docente(cedula='0924956311', nombre='JOEL', apellido='FERRERO', email='joelferrero@gmail.com',
                       telefono='0959747318', direccion='ALBORADA', numero_libros=0, activo=True, carrera='ADMINISTRACION DE EMPRESAS',
                       titulo_3er_nivel='LCDO', titulo_4to_nivel=',PHD')
    print(Docente1)
    print(Docente2)
    print(Docente3)
    print(Docente4)
