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
            r.nombre AS region,
            c.nombre AS comuna,
            i.nombre,
            i.descripcion
        FROM gestion_inmuebles_inmueble i
        INNER JOIN gestion_inmuebles_comuna c
            ON i.comuna_id = c.id
        INNER JOIN gestion_inmuebles_region r
            ON c.region_id = r.id
        ORDER BY r.nombre, c.nombre, i.nombre;
    """)

    resultados = cursor.fetchall()


ruta_salida = os.path.join(
    os.path.dirname(__file__),
    'reporte_regiones.txt'
)

with open(ruta_salida, 'w', encoding='utf-8') as archivo:

    region_actual = None

    for region, comuna, nombre, descripcion in resultados:

        if region != region_actual:
            archivo.write(f"\nREGIÓN: {region}\n")
            archivo.write("=" * 50 + "\n")
            region_actual = region

        archivo.write(f"Comuna: {comuna}\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Descripción: {descripcion}\n\n")

