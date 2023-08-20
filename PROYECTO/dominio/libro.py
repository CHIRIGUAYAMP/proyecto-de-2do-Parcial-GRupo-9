#ALVARADO VALDIVIEZO MARIA GABRIELA
#CHIRIGUAYA ROMAN MARJORIE PAMELA
#MENDOZA LOAIZA DAYANA VALENTINA
#TACLE PAREDES DESSIRE IVONNE
from material import Material
class Libro(Material):
    contador_libro = 0
    def __init__(self, codigo:str, autor:str, titulo:str, anio:int, editorial:str, disponible:bool, cantidad_disponible:int,tipo_pasta:str):
        Libro.contador_libro +=1
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible
        self._id = Libro.contador_libro
        self._tipo_pasta = tipo_pasta
        super(Libro, self).__init__(codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial, disponible=disponible, cantidad_disponible=cantidad_disponible)
    def __str__(self):
        return f' Pedido : {self.__dict__.__str__()}'
    @property
    def id(self):
        return self._id
    @property
    def tipo_pasta(self):
        return self._tipo_pasta
    @tipo_pasta.setter
    def tipo_pasta(self, tipo_pasta):
        self._tipo_pasta = tipo_pasta
    @classmethod
    def actualizar_disponibilidad(self)-> bool :
        pass

if __name__ == '__main__':
    Libro1 = Libro(codigo='001', autor='Brad Stone', titulo='The Everything Store', anio=2018,
                   editorial='English Edition', disponible=True, cantidad_disponible=25,tipo_pasta='Flexible')
    print(Libro1)
    Libro2 = Libro(codigo='002', autor='Ramon Salaverría Aliaga', titulo='Cibermedios', anio=2005,
                   editorial='Comunicacion Social Ediciones y Publicaciones', disponible=True, cantidad_disponible=8, tipo_pasta='Rustica')
    print(Libro2)

    Libro3 = Libro(codigo='003', autor='Steve McConnell', titulo='Code Complete 2', anio=2004,
                   editorial='Developer Best Practices', disponible=True, cantidad_disponible=25,tipo_pasta='Flexible')
    print(Libro3)
    Libro4 = Libro(codigo='004', autor='Hunt y Thomas', titulo='The pragmatic programmer', anio=2013,
                   editorial='English Edition', disponible=True, cantidad_disponible=63, tipo_pasta='Suave')
    print(Libro4)