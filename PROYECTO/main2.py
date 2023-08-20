#ALVARADO VALDIVIEZO MARIA GABRIELA
#CHIRIGUAYA ROMAN MARJORIE PAMELA
#MENDOZA LOAIZA DAYANA VALENTINA
#TACLE PAREDES DESSIRE IVONNE
import sys

from PySide6.QtWidgets import QApplication

from PROYECTO.servicio.persona_principal import PersonaPrincipal

app = QApplication()
vtn_principal = PersonaPrincipal()
vtn_principal.show()
sys.exit(app.exec())