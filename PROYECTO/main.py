#ALVARADO VALDIVIEZO MARIA GABRIELA
#CHIRIGUAYA ROMAN MARJORIE PAMELA
#MENDOZA LOAIZA DAYANA VALENTINA
#TACLE PAREDES DESSIRE IVONNE
from PROYECTO.dominio.estudiante import Estudiante
from PROYECTO.dominio.docente import Docente
from PROYECTO.dominio.libro import Libro
from PROYECTO.dominio.revista import Revista
from PROYECTO.dominio.pedido import Pedido

#ESTUDIANTES
Estudiante1 = Estudiante(cedula='0924956311', nombre='Dessire', apellido='Tacle', email='desitacle@gmail.com',
                         telefono='0994367826', direccion='Brisas del Norte', numero_libros=0, activo=True,
                         carrera='GIG',
                         nivel=3)
Estudiante2 = Estudiante(cedula='0923156748', nombre='Gabriela', apellido='Alvarado', email='Gabyalvarado@gmail.com',
                         telefono='0987656788', direccion='Mall del Sol', numero_libros=0, activo=True, carrera='GIG',
                         nivel=3)
Estudiante3 = Estudiante(cedula='0934257865', nombre='Dayana', apellido='Mendoza', email='Dayamendoza@gmail.com',
                         telefono='0987889700', direccion='Duran', numero_libros=0, activo=True, carrera='GIG',
                         nivel=3)
Estudiante4 = Estudiante(cedula='0929404572', nombre='Marjorie', apellido='Chiriguaya',
                         email='Marjo.chiriguaya@gmail.com',
                         telefono='0997597299', direccion='Santa Lucia', numero_libros=0, activo=True, carrera='GIG',
                         nivel=3)
print(Estudiante1)
print(Estudiante2)
print(Estudiante3)
print(Estudiante4)

#DOCENTEES
Docente1 = Docente(cedula='0932260755', nombre='PAUL', apellido='BENAVIDES', email='pbenavides@gmail.com',
                   telefono='0982260755', direccion='VERNAZA NORTE', numero_libros=0, activo=True, carrera='DERECHO',
                   titulo_3er_nivel='LCDO', titulo_4to_nivel=',DOC')
Docente2 = Docente(cedula='0911340556', nombre='JOAN', apellido='ALVARADO', email='jalvarado@gmail.com',
                   telefono='0960540817', direccion='VERNAZA NORTE', numero_libros=0, activo=True, carrera='PSICOLOGIA',
                   titulo_3er_nivel='LCDO', titulo_4to_nivel=',PHD')
Docente3 = Docente(cedula='0913167548', nombre='LEONEL', apellido='GUERRERO', email='lguerrero@gmail.com',
                   telefono='0959747318', direccion='SAUCES 6', numero_libros=0, activo=True,
                   carrera='GESTION DE LA INFORMACION GERENCIAL',
                   titulo_3er_nivel='LCDO', titulo_4to_nivel=',DOC')

Docente4 = Docente(cedula='0924956311', nombre='JOEL', apellido='FERRERO', email='joelferrero@gmail.com',
                   telefono='0959747318', direccion='ALBORADA', numero_libros=0, activo=True,
                   carrera='ADMINISTRACION DE EMPRESAS',
                   titulo_3er_nivel='LCDO', titulo_4to_nivel=',PHD')
print(Docente1)
print(Docente2)
print(Docente3)
print(Docente4)

#LIBROOS
Libro1 = Libro(codigo='001', autor='Brad Stone', titulo='The Everything Store', anio=2018,
               editorial='English Edition', disponible=True, cantidad_disponible=25, tipo_pasta='Flexible')
print(Libro1)
Libro2 = Libro(codigo='002', autor='Ramon Salaverría Aliaga', titulo='Cibermedios', anio=2005,
               editorial='Comunicacion Social Ediciones y Publicaciones', disponible=True, cantidad_disponible=8,
               tipo_pasta='Rustica')
print(Libro2)

Libro3 = Libro(codigo='003', autor='Steve McConnell', titulo='Code Complete 2', anio=2004,
               editorial='Developer Best Practices', disponible=True, cantidad_disponible=25, tipo_pasta='Flexible')
print(Libro3)
Libro4 = Libro(codigo='004', autor='Hunt y Thomas', titulo='The pragmatic programmer', anio=2013,
               editorial='English Edition', disponible=True, cantidad_disponible=63, tipo_pasta='Suave')
print(Libro4)

#REVISTA
REVISTA1 = Revista(codigo='101', autor='Gaby Alvarado', titulo='Revista Corazón Azul', anio=2010, editorial='FlipHTML5',
                   disponible=True, cantidad_disponible=58, tipo='FISICO')
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
#FINAL-PEDIDO
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