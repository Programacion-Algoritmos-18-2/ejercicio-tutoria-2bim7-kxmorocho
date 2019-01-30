import codecs
import sys

#Permite leer el archivo
class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/ejemplo.txt", "r") # Abrimos el archivo

    def obtener_info(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()

