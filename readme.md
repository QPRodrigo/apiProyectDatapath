# Proyecto de Api Conectado con una BD

Este proyecto es una API RESTful creada con FastAPI para gestionar películas, aprovechando SQLAlchemy para la base de datos y Uvicorn como servidor. Permite operaciones CRUD eficientes en un entorno optimizado, ideal para proyectos que necesitan una gestión sencilla y efectiva de películas.

## Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo. Ve a la sección de **Instalación** para conocer cómo instalarlo.

## Prerrequisitos

Antes de comenzar, asegúrate de tener los siguientes prerrequisitos instalados:

- Docker
- Docker Compose
Consulta [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/) para las guías de instalación.

## Estructura del proyecto:

```nginx
| - app
    | - connection
        | - postgressConnector.py
    |- controllers
    	| - controller_movies.py
    | - models
	    | - model_movies.py
    | - routers
    	| - router_movies.py	    
    | - main.py
| - .gitignore
| - docker-compose.yml
| - Dockerfile
| - readme.md
| - requirements.txt
```
### Contenidos de las carpetas
`app` contiene todos los archivos necesarios de nuestra aplicación.

`app.connection` contiene las conexiones a bases de datos usadas por la aplicación.

`app.controllers` contiene los controladores que gestionan la lógica de los métodos GET, POST, PUT y DELETE.

`app.models` contiene los modelos que definen el esquema de datos para la entrada y salida.

`app.routers` contiene las rutas que gestionan cada solicitud dentro de nuestra aplicación, abarcando los métodos GET, POST, PUT y DELETE.

`.gitignore` especifica los archivos y directorios que Git debe ignorar y no incluir en el control de versiones.

`docker-compose.yml` define servicios, redes y volúmenes para aplicaciones multi-contenedor con Docker Compose.

`Dockerfile` Imagen Docker creada por mi persona  que prepara el entorno para ejecutar aplicaciones FastAPI.

`requirements.txt` enumera las dependencias de Python necesarias para el proyecto.

### Instalación

Una serie paso a paso de ejemplos que te indican cómo hacer funcionar un entorno de desarrollo.

## Cómo empezar

1. **Clonar el repositorio**

   Abre una terminal y clona el repositorio usando:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```
   Ingresar a la carpeta
   ```bash
   cd apiProyectDatapath
   ```
2. **Construir y ejecutar con Docker Compose**
   
    Desde el directorio del proyecto, ejecuta:
   ```bash
   docker-compose up --build
   ```
    Este comando construye la imagen Docker basada en el Dockerfile proporcionado y luego inicia la aplicación utilizando docker-compose.yml
   
4. **Construir y ejecutar con Docker Compose**
   
   Una vez que los contenedores estén en ejecución, puedes acceder a tu aplicación FastAPI navegando a [http://localhost:8000](http://localhost:8000) en tu navegador.

### Desarrollo y Contribuciones
Para contribuir al proyecto, por favor crea un fork del repositorio, realiza tus cambios y envía un pull request. Asegúrate de adherirte a las convenciones de código y documentación existentes.
