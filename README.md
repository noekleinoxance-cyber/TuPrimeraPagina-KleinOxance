# 🛠️ Mesa de Ayuda IT

Sistema web desarrollado en **Django** que simula una herramienta
interna de mesa de ayuda para registrar incidentes de soporte técnico,
documentar soluciones y realizar seguimiento de tickets.

------------------------------------------------------------------------

## 🚀 Funcionalidades

✔ Sistema de **autenticación de usuarios** - Registro - Inicio de
sesión - Cierre de sesión

✔ Creación de **tickets de soporte** asociados al usuario que los
reporta

✔ **Estados de ticket** - Abierto - En proceso - Resuelto

✔ **Niveles de prioridad** - Baja - Media - Alta - Crítica

✔ **Tipos de incidente** (categorías)

✔ **Comentarios en cada ticket**

✔ **Búsqueda de tickets por título**

✔ **CRUD completo de tickets** - Crear ticket - Listar tickets - Ver
detalle - Editar ticket - Eliminar ticket

✔ Interfaz basada en **herencia de plantillas con `base.html`**

------------------------------------------------------------------------

## 🧱 Modelos implementados

-   **Usuario** (Django Auth)
-   **Ticket** (Post)
-   **Categoría** (Tipo de incidente)
-   **Comentario**

------------------------------------------------------------------------

## ⚙️ Tecnologías utilizadas

-   Python 3
-   Django
-   SQLite3
-   HTML
-   CSS

------------------------------------------------------------------------

## 🖥️ Cómo ejecutar el proyecto

### 1️⃣ Clonar el repositorio

    git clone <url-del-repositorio>

### 2️⃣ Crear entorno virtual

    python -m venv .venv

### 3️⃣ Activar entorno virtual

Windows:

    .venv\Scripts\activate

Linux / Mac:

    source .venv/bin/activate

### 4️⃣ Instalar dependencias

    pip install django

### 5️⃣ Aplicar migraciones

    python manage.py makemigrations
    python manage.py migrate

### 6️⃣ Ejecutar el servidor

    python manage.py runserver

Luego abrir en el navegador:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🔎 Flujo recomendado para probar el sistema

1.  Registrarse como usuario
2.  Iniciar sesión
3.  Crear un **tipo de incidente (categoría)**
4.  Crear un **ticket de soporte**
5.  Visualizar el **listado de tickets**
6.  Editar o eliminar un ticket
7.  Probar **búsqueda de tickets**
8.  Agregar **comentarios** en el detalle del ticket

------------------------------------------------------------------------

## 📚 Proyecto académico

Proyecto desarrollado como trabajo práctico para aprender:

-   Django
-   Modelos y migraciones
-   Formularios
-   Autenticación de usuarios
-   CRUD completo
-   Plantillas y herencia de layouts

------------------------------------------------------------------------

## 👨‍💻 Autor

Noé Klein
