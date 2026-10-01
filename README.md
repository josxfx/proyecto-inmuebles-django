# Proyecto de Gestión de Arriendos

Aplicación web desarrollada con **Django y PostgreSQL** para la gestión de inmuebles disponibles para arriendo. El sistema permite registrar usuarios como arrendadores o arrendatarios, administrar propiedades y gestionar solicitudes de arriendo.

## Descripción

Este proyecto fue desarrollado como parte del proceso de formación en desarrollo Full Stack Python.

La aplicación permite a los usuarios registrarse, iniciar sesión y gestionar su información de acuerdo con su tipo de usuario. Los arrendadores pueden administrar sus inmuebles, mientras que los arrendatarios pueden consultar propiedades disponibles, aplicar filtros y realizar solicitudes de arriendo.

## Tecnologías utilizadas

- **Python**
- **Django**
- **PostgreSQL**
- **Django ORM**
- **django-environ**
- **HTML5**
- **CSS3**
- **Bootstrap**
- **Git y GitHub**

## Funcionalidades

### Usuarios

- Registro de nuevos usuarios.
- Inicio y cierre de sesión.
- Perfil de usuario.
- Edición de información personal.
- Identificación del usuario como arrendador o arrendatario.

### Gestión de inmuebles

Los arrendadores pueden:

- Agregar nuevos inmuebles.
- Consultar sus inmuebles registrados.
- Editar información de sus propiedades.
- Eliminar inmuebles.

Los inmuebles almacenan información como:

- Nombre.
- Descripción.
- Tipo de inmueble.
- Región y comuna.
- Dirección.
- Metros cuadrados construidos y totales.
- Cantidad de dormitorios.
- Cantidad de baños.
- Estacionamiento.
- Precio mensual.

### Búsqueda y filtros

Los usuarios pueden consultar la oferta de inmuebles disponibles y filtrar los resultados según:

- Región.
- Comuna.

### Solicitudes de arriendo

Los arrendatarios pueden:

- Solicitar el arriendo de un inmueble.
- Consultar sus solicitudes.
- Revisar el estado de cada solicitud.

Las solicitudes pueden encontrarse en los siguientes estados:

- Pendiente.
- Aceptada.
- Rechazada.

## Base de datos

El proyecto utiliza **PostgreSQL** como sistema de gestión de base de datos.

Entre las principales entidades utilizadas se encuentran:

- Usuarios.
- Regiones.
- Comunas.
- Tipos de inmueble.
- Inmuebles.
- Solicitudes de arriendo.

Se utilizan relaciones entre los modelos mediante el **Django ORM**.

## Configuración del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/josxfx/proyecto-inmuebles-django.git
cd proyecto-inmuebles-django
```

### 2. Crear y activar un entorno virtual

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto utilizando `.env.example` como referencia.

El archivo debe contener las variables necesarias para Django y PostgreSQL:

```env
SECRET_KEY=tu-clave-secreta
DB_NAME=nombre-de-tu-base-de-datos
DB_USER=tu-usuario
DB_PASSWORD=tu-contrasena
DB_HOST=localhost
DB_PORT=5432
```

**No se deben publicar las credenciales reales ni el archivo `.env`.**

### 5. Configurar la base de datos

Crear una base de datos PostgreSQL y completar los datos de conexión en el archivo `.env`.

### 6. Ejecutar las migraciones

```bash
python manage.py migrate
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Luego acceder desde el navegador a:

```text
http://127.0.0.1:8000/
```

## Estructura principal del proyecto

```text
proyecto_inmuebles/
│
├── gestion_inmuebles/
│   ├── migrations/
│   ├── templates/
│   ├── fixtures/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── proyecto_inmuebles/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── reportes/
│   └── ...
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Aprendizajes y habilidades desarrolladas

Este proyecto permitió aplicar conocimientos relacionados con:

- Desarrollo web con Python y Django.
- Creación y relación de modelos.
- Uso del Django ORM.
- Operaciones CRUD.
- Autenticación y gestión de usuarios.
- Formularios y validación de datos.
- Manejo de bases de datos PostgreSQL.
- Consultas y relaciones entre datos.
- Uso de variables de entorno para proteger información sensible.
- Desarrollo de interfaces utilizando HTML, CSS y Bootstrap.
