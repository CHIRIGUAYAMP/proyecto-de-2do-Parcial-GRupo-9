# ALVARADO VALDIVIEZO MARIA GABRIELA
# CHIRIGUAYA ROMAN MARJORIE PAMELA
# MENDOZA LOAIZA DAYANA VALENTINA
# TACLE PAREDES DESSIRE IVONNE
from statistics import median, mode
from datetime import datetime, date

from PySide6 import QtGui
# from PySide6.QtCore import QRegularExpression
# from PySide6.QtGui import QRegularExpressionValidator

from PySide6.QtWidgets import QMainWindow, QMessageBox

from PROYECTO.UI.vtn_principal import Ui_vtn_principal
from PROYECTO.datos.estudiante_dao import EstudianteDao
from PROYECTO.dominio.docente import Docente
from PROYECTO.dominio.estudiante import Estudiante





class PersonaPrincipal(QMainWindow):

    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        self.ui.btn_estatura.clicked.connect(self.estadistica_Estatura)
        self.ui.btn_peso.clicked.connect(self.estadistica_Peso)
        self.ui.btn_cal_edad.clicked.connect(self.calcular_edad)

        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())

        correo_exp: str= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        from PySide6.QtGui import QregularExpressionValidator
        validator = QregularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
        global respuesta
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if self.ui.txt_nombre.text() == '' or self.ui.txt_apellido.text() == ' ' \
                or len(self.ui.txt_cedula.text()) < 10 or self.ui.txt_email.text() == '':
            print('Completar datos')
            QMessageBox.warning(self, 'Advertenia', 'Falta de llenar los datos obligatorios')
        else:
            persona = None
            if tipo_persona == 'Docente':
                persona = Docente()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.estatura = self.ui.sp_estatura.text()
                persona.peso = self.ui.sp_Peso.text()
                persona.fechanacimiento = self.ui.de_fecha_nac.text()
                # persona.edad= self.ui.

            else:
                persona = Estudiante()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.estatura = self.ui.sp_estatura.text()
                persona.peso = self.ui.sp_Peso.text()
                persona.fechanacimiento = self.ui.de_fecha_nac.text()

                # Insertar en la base de datos al Estudiate
                respuesta = None
                respuesta = EstudianteDao.insert_estudiante(persona)



            if respuesta['exito']:
                self.ui.txt_nombre.setText('')
                self.ui.txt_apellido.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.txt_email.setText('')
                self.ui.txt_carrera.setText('')
                self.ui.sp_estatura.setValue(0)
                self.ui.sp_Peso.setValue(0)
                #self.ui.de_fecha_nac.setValue(0)

                self.ui.stb_estado.showMessage('Grabado con Exito', 2000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])

    def buscar_x_cedula(self):
        cedula = self.ui.txt_cedula.text()
        e = Estudiante(cedula=cedula)
        e = EstudianteDao.seleccionar_por_cedula(e)

        self.ui.txt_nombre.setText(e.nombre)
        self.ui.txt_apellido.setText(e.apellido)
        self.ui.txt_email.setText(e.email)
        self.ui.sp_Peso.setValue(e.peso)
        self.ui.sp_estatura.setValue(e.estatura)
        self.ui.txt_carrera.setText(e.carrera)
        self.ui.de_fecha_nac.setDate(e.fechanacimiento)
        self.ui.cb_tipo_persona.setCurrentText('Estudiante')

    # ojo
    def calcular_mediana(self, estaturas):
        return median(estaturas)

    def calcular_moda(self, estaturas):
        return mode(estaturas)

    def calcular_minimo(self, estaturas):
        return min(estaturas)

    def calcular_maximo(self, estaturas):
        return max(estaturas)



    # ojo
    def estadistica_Estatura(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_estaturas = 0
        estaturas = []

        for estudiante in estudiantes:
            suma_estaturas += estudiante.estatura
            estaturas.append(estudiante.estatura)

        promedio_estatura = suma_estaturas / cantidad_estudiantes
        mediana_estatura = self.calcular_mediana(estaturas)
        moda_estatura = self.calcular_moda(estaturas)
        minimo_estatura = self.calcular_minimo(estaturas)
        maximo_estatura = self.calcular_maximo(estaturas)

        print('-----------------------------------------------')
        print('------     ESTADISTICA DE ESTATURA   ----------')
        print('-----------------------------------------------')
        print(f'El promedio de estatura es: {promedio_estatura}')
        print(f'La mediana de estatura es: {mediana_estatura}')
        print(f'La moda de estatura es: {moda_estatura}')
        print(f'El valor mínimo de estatura es: {minimo_estatura}')
        print(f'El valor máximo de estatura es: {maximo_estatura}')

    def estadistica_Peso(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_peso = 0
        pesos = []

        for estudiante in estudiantes:
            suma_peso += estudiante.peso
            pesos.append(estudiante.peso)

        promedio_peso = suma_peso / cantidad_estudiantes
        print('-----------------------------------------------')
        print('------     ESTADISTICA DE PESO    -------------')
        print('-----------------------------------------------')
        print(f'El promedio de peso es: {promedio_peso}')

        # Cálculo de la moda
        moda_peso = max(set(pesos), key=pesos.count)
        print(f'La moda de peso es: {moda_peso}')

        # Cálculo de la mediana
        pesos_sorted = sorted(pesos)
        n = len(pesos_sorted)
        if n % 2 == 1:
            mediana_peso = pesos_sorted[n // 2]
        else:
            mediana_peso = (pesos_sorted[(n - 1) // 2] + pesos_sorted[n // 2]) / 2
        print(f'La mediana de peso es: {mediana_peso}')

        # Cálculo del mínimo y máximo
        min_peso = min(pesos)
        max_peso = max(pesos)
        print(f'El peso mínimo es: {min_peso}')
        print(f'El peso máximo es: {max_peso}')




#---------
    def calcular_edad(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        f_nacimiento = [estudiante.fechanacimiento for estudiante in estudiantes]
        fecha_actual = date.today()

        edades = []
        for fecha in f_nacimiento:
            edad = fecha_actual.year - fecha.year - ((fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day))
            edades.append(edad)

        # Calculando el promedio de edad
        promedio_edad = sum(edades) / len(edades)
        # Ordenando las edades y calculando la mediana
        edades_sorted = sorted(edades)
        n = len(edades_sorted)
        if n % 2 == 0:
            mediana_edad = (edades_sorted[n // 2 - 1] + edades_sorted[n // 2]) / 2
        else:  # Cantidad impar de edades
            mediana_edad = edades_sorted[n // 2]

        # Calculando la moda
        edad_counts = {edad: edades.count(edad) for edad in edades}
        max_count = max(edad_counts.values())
        moda_edad = [edad for edad, count in edad_counts.items() if count == max_count]

        # Calculando la edad máxima y mínima
        max_edad = max(edades)
        min_edad = min(edades)

        print('-----------------------------------------------')
        print('------     ESTADISTICA DE EDAD    -------------')
        print('-----------------------------------------------')
        print(f'El promedio de edades es: {promedio_edad:.2f} años')
        print(f'La mediana de edades es: {mediana_edad} años')
        print(f'La moda de edades es: {moda_edad}')
        print(f'La edad máxima es: {max_edad} años')
        print(f'La edad mínima es: {min_edad} años')


































