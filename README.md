# Proyecto de Ejemplos en Python

Este repositorio contiene una colección de ejemplos prácticos en Python que demuestran diferentes conceptos y funcionalidades de programación.

## 📋 Contenido

El proyecto incluye los siguientes ejemplos:

### 1. **Calculadora Básica** (`calculadora.py`)
Una calculadora interactiva que permite realizar operaciones básicas (suma, resta, multiplicación, división) mediante entrada del usuario por consola.

### 2. **Contador de Palabras** (`contador.py`)
Herramienta para contar palabras en archivos de texto y PDFs. Muestra el total de palabras y las 10 palabras más frecuentes.

**Características:**
- Soporte para archivos de texto (.txt)
- Soporte para archivos PDF (requiere PyPDF2)
- Análisis de frecuencia de palabras

### 3. **Análisis de Datos** (`analisis.py`)
Script para realizar análisis estadístico básico de datos CSV usando pandas y matplotlib.

**Funcionalidades:**
- Cálculo de media, mediana y desviación estándar
- Generación de gráficos de dispersión

### 4. **FizzBuzz** (`FizzBuzz.py`)
Implementación clásica del problema FizzBuzz que imprime números del 1 al 50, reemplazando múltiplos de 3 con "Fizz" y múltiplos de 5 con "Buzz".

## 🚀 Requisitos

- Python 3.x
- Dependencias opcionales (según el ejemplo que uses):
  - `pandas` - Para análisis de datos
  - `matplotlib` - Para visualización de gráficos
  - `PyPDF2` - Para lectura de archivos PDF

## 📦 Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd cursor
```

2. Crea un entorno virtual (recomendado):
```bash
python -m venv venv
```

3. Activa el entorno virtual:
   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     venv\Scripts\activate.bat
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias necesarias:
```bash
pip install pandas matplotlib PyPDF2
```

## 💻 Uso

### Calculadora
```bash
python ejemplos/calculadora.py
```

### Contador de Palabras
```bash
python ejemplos/contador.py
```
Se te pedirá la ruta del archivo a analizar.

### Análisis de Datos
```bash
python ejemplos/analisis.py
```
Asegúrate de tener un archivo `Libro1.csv` en el directorio `ejemplos/` con datos delimitados por punto y coma (`;`).

### FizzBuzz
```bash
python ejemplos/FizzBuzz.py
```

## 📁 Estructura del Proyecto

```
cursor/
├── ejemplos/
│   ├── analisis.py
│   ├── calculadora.py
│   ├── contador.py
│   ├── FizzBuzz.py
│   └── Libro1.csv
├── venv/          # Entorno virtual (ignorado por Git)
├── .gitignore
└── README.md
```

## 🔧 Notas

- El entorno virtual (`venv/`) está configurado para ser ignorado por Git.
- Los archivos de ejemplo son independientes y pueden ejecutarse por separado.
- Algunos ejemplos requieren entrada del usuario por consola.

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de agregar más ejemplos o mejorar los existentes.

