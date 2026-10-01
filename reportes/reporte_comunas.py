import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from django.db import connection


with connection.cursor() as cursor:
    cursor.execute("""
        SELECT
            c.nombre AS comuna,
            i.nombre,
            i.descripcion
        FROM gestion_inmuebles_inmueble i
        INNER JOIN gestion_inmuebles_comuna c
            ON i.comuna_id = c.id
        ORDER BY c.nombre, i.nombre;
    """)

    resultados = cursor.fetchall()


ruta_salida = os.path.join(
    os.path.dirname(__file__),
    'reporte_comunas.txt'
)

with open(ruta_salida, 'w', encoding='utf-8') as archivo:

    comuna_actual = None

    for comuna, nombre, descripcion in resultados:

        if comuna != comuna_actual:
            archivo.write(f"\nCOMUNA: {comuna}\n")
            archivo.write("-" * 50 + "\n")
            comuna_actual = comuna

        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Descripción: {descripcion}\n\n")

