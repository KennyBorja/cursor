# -*- coding: utf-8 -*-
"""
Esqueleto básico de una aplicación Flask para gestor de tareas.
Incluye una ruta principal y punto de entrada para ejecutar el servidor.
"""

from flask import Flask, request, redirect, url_for, render_template
import json
import os

app = Flask(__name__)

# Archivo para guardar las tareas
ARCHIVO_TAREAS = 'tareas.json'

# Lista global en memoria y contador incremental de IDs
tareas = []
siguiente_id = 1


def guardar_datos():
    """Guarda las tareas y el siguiente_id en un archivo JSON."""
    with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as f:
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f, ensure_ascii=False, indent=2)


def cargar_datos():
    """Carga las tareas y el siguiente_id desde un archivo JSON."""
    global tareas, siguiente_id
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                tareas = datos.get('tareas', [])
                siguiente_id = datos.get('siguiente_id', 1)
        except (json.JSONDecodeError, IOError):
            # Si hay error al leer, empezar con datos vacíos
            tareas = []
            siguiente_id = 1


def agregar_tarea(texto):
    """Agrega una tarea con id incremental y campo 'hecho'."""
    global siguiente_id
    tarea = {"id": siguiente_id, "texto": texto, "hecho": False}
    tareas.append(tarea)
    siguiente_id += 1
    guardar_datos()
    return tarea


def completar_tarea(tarea_id):
    """Marca una tarea como completada por id. Devuelve True si la encontró."""
    for t in tareas:
        if t["id"] == tarea_id:
            t["hecho"] = True
            guardar_datos()
            return True
    return False


def eliminar_tarea(tarea_id):
    """Elimina una tarea por id. Devuelve True si la encontró."""
    global tareas
    tareas = [t for t in tareas if t["id"] != tarea_id]
    guardar_datos()
    return True


def editar_tarea(tarea_id, nuevo_texto):
    """Edita el texto de una tarea por id. Devuelve True si la encontró."""
    for t in tareas:
        if t["id"] == tarea_id:
            t["texto"] = nuevo_texto.strip()
            guardar_datos()
            return True
    return False


@app.route('/')

def index():

    # Ordenar tareas: incompletas primero, luego completadas

    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])

    return render_template('index.html', tareas=tareas_ordenadas)


@app.route("/agregar", methods=["POST"])
def agregar():
    """Procesa el formulario para agregar una nueva tarea."""
    texto = request.form.get("texto", "").strip()
    if texto:
        agregar_tarea(texto)
    return redirect('/')


@app.route("/completar/<int:tarea_id>", methods=["GET"])
def completar(tarea_id):
    """Marca una tarea como completada y redirige a la página principal."""
    completar_tarea(tarea_id)
    return redirect('/')


@app.route("/eliminar/<int:tarea_id>", methods=["GET"])
def eliminar(tarea_id):
    """Elimina una tarea y redirige a la página principal."""
    eliminar_tarea(tarea_id)
    return redirect('/')


@app.route("/editar/<int:tarea_id>", methods=["POST"])
def editar(tarea_id):
    """Edita el texto de una tarea y redirige a la página principal."""
    nuevo_texto = request.form.get("texto", "").strip()
    if nuevo_texto:
        editar_tarea(tarea_id, nuevo_texto)
    return redirect('/')


if __name__ == "__main__":
    # Cargar datos al iniciar la aplicación
    cargar_datos()
    app.run(debug=True)

