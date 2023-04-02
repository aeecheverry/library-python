# Backend developer - Prueba técnica

Desarrollar una API web que permita administrar una pequeña biblioteca.

## Desiciones de diseño

Opte por usar Flask como framework de desarrollo, para implementar una arquitectura 3-tier, con una capa de negocio, una capa de acceso a datos y una capa de rutas. Esto permite una mayor escalabilidad y mantenibilidad del código. 

### Estructura del proyecto

- app
    - business: Logica de negocio, validaciones, etc
        - helpers: Funciones auxiliares, como consulta de APIs externas
    - dao: Acceso a datos
    - docs: Documentación OpenAPI 3.0
    - factories: Fabricas para crear objetos de la aplicación
    - routes: Rutas de la aplicación
    - test: Test de la aplicación
- data: Volumentes de datos para la base de datos
- main.py: Archivo principal de la aplicación

### Base de datos

MongoDB: Se escogió esta base de datos por su facilidad de uso y escalabilidad. Además de que es una base de datos NoSQL, lo que permite una mayor flexibilidad en el diseño de la base de datos.

### Docker y docker-compose

Escogí usar docker y docker-compose para facilitar el despliegue de la aplicación. Además de que permite una mayor portabilidad de la aplicación.

### Setup

Para iniciar la aplicación, se puede ejecutar cualquiera de los siguientes archivos:
1. `run_on_docker.sh` en la raíz del proyecto. Este archivo se encarga de construir las imágenes de docker y ejecutar los contenedores.
2. `run_on_local.sh` en la raíz del proyecto. Este archivo se encarga de instalar las dependencias de python y ejecutar la aplicación de manera local.

### API

Se implementó la documentación de la API usando OpenAPI 3.0. Esto permite una mayor facilidad de uso de la API, ya que permite probarla directamente desde la documentación. `http://localhost:3000/docs`

La API consta de 3 rutas:

- GET /books: Obtiene los libros de la base de datos por medio de filtros
    - Query params:
        - id: Filtra por id
        - title: Filtra por titulo
        - subtitle: Filtra por subtitulo
        - author: Filtra por autor: autor1, autor2, autor3, ... etc
        - category: Filtra por categoria: categoria1, categoria2, categoria3, ... etc
        - publishedDate: Filtra por fecha de publicación: 2021-01-01
        - publisher: Filtra por editorial
        - description: Filtra por descripción
    - Ejemplo: `http://localhost:3000/books?id=identificador&author=autor1,autor2&category=categoria1,categoria2`

- POST /books: Crea un nuevo libro en la base de datos
    - Body:
        - id: Identificador del libro
        - source: Fuentes de donde se obtuvo la información del libro: `google` | `db_interna` | `otro`
    - Ejemplo: `http://localhost:3000/books`
    ```json
    {
        "id": "identificador",
        "source": "google"
    }
    ```
- DELETE /books/{id}: Elimina un libro de la base de datos
    - Ejemplo: `http://localhost:3000/books/identificador`

### Tecnologías

- pyhton 3.10 (3.9+)
- Flask
- MongoDB
- Docker
- Docker-compose
- Swagger
- Pytest
- Github

