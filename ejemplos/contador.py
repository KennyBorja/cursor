import re
from collections import Counter

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

class ContadorDePalabras:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.texto = ""

    def leer_archivo(self):
        if self.ruta_archivo.lower().endswith('.pdf'):
            if PyPDF2 is None:
                raise ImportError("PyPDF2 no está instalado. Instálalo con 'pip install PyPDF2'.")
            self.texto = self._leer_pdf()
        else:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                self.texto = archivo.read()

    def _leer_pdf(self):
        texto_extraido = ""
        with open(self.ruta_archivo, "rb") as archivo_pdf:
            lector = PyPDF2.PdfReader(archivo_pdf)
            for pagina in lector.pages:
                texto_extraido += pagina.extract_text() or ""
        return texto_extraido

    def contar_palabras(self):
        palabras = re.findall(r'\b\w+\b', self.texto)
        total_palabras = len(palabras)
        palabras_frecuentes = Counter(palabras).most_common(10)
        return total_palabras, palabras_frecuentes

if __name__ == "__main__":
    ruta = input("Ingrese la ruta del archivo: ")
    contador = ContadorDePalabras(ruta)
    contador.leer_archivo()
    total, frecuentes = contador.contar_palabras()
    print(total)
    print(frecuentes)