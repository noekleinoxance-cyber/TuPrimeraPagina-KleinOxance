# TuPrimeraPagina+KleinOxance

Sistema web desarrollado en Django

El proyecto simula una herramienta interna para documentar **casos de soporte técnico**, 
registrar procedimientos y dejar constancia de soluciones aplicadas.

---

## Funcionalidades

- ✔ Herencia de plantillas mediante `base.html`
- ✔ Modelos implementados:
  - Autor
  - Categoría
  - Caso de soporte (Post)
  - Comentarios
- ✔ Formularios para:
  - Crear autor
  - Crear categoría
  - Crear caso
  - Agregar comentarios
- ✔ Búsqueda de casos por título
- ✔ CRUD completo de casos:
  - Crear
  - Listar
  - Ver detalle
  - Editar
  - Eliminar

---

## Tecnologías utilizadas

- Python 3
- Django 6
- SQLite3
- HTML + CSS básico

---

## Cómo ejecutar el proyecto

1. Crear entorno virtual:

    python -m venv .venv

2. Activar entorno virtual.

3. Instalar dependencias:

    pip install django

4. Aplicar migraciones:

    python manage.py makemigrations
    python manage.py migrate

5. Ejecutar servidor:

    python manage.py runserver

---

## Orden sugerido para probar funcionalidades

1. Crear un autor  
2. Crear una categoría  
3. Crear un caso de soporte  
4. Visualizar el listado de casos  
5. Editar o borrar un caso  
6. Probar búsqueda por título  
7. Agregar comentarios en el detalle del caso  
