# Mi imagen de Docker - Rodrigo Quinteros Peralta
# Usa una imagen oficial de Python como imagen padre
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /apiproyect

# Copia los archivos de requisitos primero para aprovechar la caché de capas de Docker
COPY ./requirements.txt /apiproyect/requirements.txt

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade -r /apiproyect/requirements.txt

# Copia el contenido del directorio local en el contenedor
COPY ./app /apiproyect/app

# Comando para ejecutar la aplicación usando uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
