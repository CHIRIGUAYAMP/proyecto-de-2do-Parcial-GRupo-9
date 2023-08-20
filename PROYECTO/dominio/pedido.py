#ALVARADO VALDIVIEZO MARIA GABRIELA
#CHIRIGUAYA ROMAN MARJORIE PAMELA
#MENDOZA LOAIZA DAYANA VALENTINA
#TACLE PAREDES DESSIRE IVONNE

class Pedido():
    def __init__(self, id, solicitante, lista_material, fecha_prestamo, fecha_devolucion):
        self._id = id
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f'Pedido: {self.__dict__}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, nuevo_solicitante):
        self._solicitante = nuevo_solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, nueva_lista_material):
        self._lista_material = nueva_lista_material

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nueva_fecha_prestamo):
        self._fecha_prestamo = nueva_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nueva_fecha_devolucion):
        self._fecha_devolucion = nueva_fecha_devolucion


if __name__ == '__main__':
    Ped1 = Pedido(id='0924956311', solicitante='DESSIRE TACLE', lista_material='Revista Piedras Bit ',
                  fecha_prestamo='15/06/2023', fecha_devolucion='17/06/2023')
    print(Ped1)

    Ped2 = Pedido(id='0923156748', solicitante='GABRIELA ALVARADO', lista_material='Revista Mundo Informatico',
                  fecha_prestamo='13/06/2023', fecha_devolucion='14/07/2023')
    print(Ped2)

    Ped3 = Pedido(id='0934257865', solicitante='DAYANNA MENDOZA', lista_material='Cibermedios',
                  fecha_prestamo='01/06/2023', fecha_devolucion='19/06/2023')
    print(Ped3)

    Ped4 = Pedido(id='0929404572', solicitante='MARJORIE CHIRIGUAYA', lista_material='Revista Busqueda Tecnologica',
                  fecha_prestamo='02/06/2023', fecha_devolucion='15/06/2023')
    print(Ped4)

