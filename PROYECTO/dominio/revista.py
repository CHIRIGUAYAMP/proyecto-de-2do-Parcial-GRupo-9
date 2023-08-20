#ALVARADO VALDIVIEZO MARIA GABRIELA
#CHIRIGUAYA ROMAN MARJORIE PAMELA
#MENDOZA LOAIZA DAYANA VALENTINA
#TACLE PAREDES DESSIRE IVONNE
from PROYECTO.dominio.material import Material
class Revista(Material):
    contador_revista = 0
    def __init__(self, codigo:str, autor:str, titulo:str, anio:int, editorial:str, disponible:bool, cantidad_disponible:int,tipo:str):
        Revista.contador_revista +=1
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible
        self._id = Revista.contador_revista
        self._tipo = tipo
        super(Revista, self).__init__(codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial, disponible=disponible, cantidad_disponible=cantidad_disponible)

    def __str__ (self):
        return f' Revista : {self.__dict__.__str__()}'
    @property
    def id(self):
        return self._id
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @classmethod
    def actualizar_disponibilidad(self)-> bool :
        pass
if __name__ == '__main__':
    REVISTA1 = Revista(codigo='101', autor='Gaby Alvarado', titulo='Revista Corazón Azul', anio=2010, editorial='FlipHTML5', disponible=True, cantidad_disponible=58,tipo='FISICO')
    print(REVISTA1)

    REVISTA2 = Revista(codigo='104', autor='Erick Perez', titulo='Revista Mundo Informatico', anio=2018,
                       editorial='Sanlucas', disponible=True, cantidad_disponible=10, tipo='VIRTUAL')
    print(REVISTA2)
    REVISTA3 = Revista(codigo='102', autor='Dessi Lopez', titulo='Revista Piedras Bit ', anio=2022,
                       editorial='LopezCortez', disponible=True, cantidad_disponible=7, tipo='FISICO')
    print(REVISTA3)
    REVISTA4 = Revista(codigo='103', autor='Pamela Roman', titulo='Revista Busqueda Tecnologica', anio=2023,
                       editorial='RomanAlvarado', disponible=True, cantidad_disponible=200, tipo='VIRTUAL')
    print(REVISTA4)
    REVISTA3.tipo = 'VIRTUAL'
    print(REVISTA3)