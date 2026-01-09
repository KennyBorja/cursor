import os
from pathlib import Path

carpeta_objetivo=Path.home() / "Downloads"

categorias = {
    "Imagenes": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".svg"
    ],

    "Documentos": [
        ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls",
        ".pptx", ".ppt", ".odt", ".ods", ".csv"
    ],

    "Videos": [
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpeg"
    ],

    "Musica": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"
    ],

    "Comprimidos": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"
    ],

    "Programas": [
        ".exe", ".msi", ".deb", ".rpm", ".apk", ".dmg"
    ],

    "Codigo": [
        ".py", ".cpp", ".c", ".h", ".java", ".js", ".ts",
        ".html", ".css", ".json", ".xml", ".sh"
    ]
}

CATEGORIA_DEFECTO = "Otros"

extension_a_categoria = {}

for categoria, exts in categorias.items():
    for ext in exts:
        extension_a_categoria[ext.lower()] = categoria

for item in carpeta_objetivo.iterdir():
    if not item.is_file():
        continue
    extension = item.suffix.lower()
    categoria = extension_a_categoria.get(extension, CATEGORIA_DEFECTO)
    carpeta_destino = carpeta_objetivo / categoria
    carpeta_destino.mkdir(exist_ok=True)

    destino = carpeta_destino / item.name
    item.rename(destino)
print("✔ Organización completada")



