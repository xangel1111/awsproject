# Usar una imagen oficial de Python como base
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt a la imagen del contenedor
COPY requirements.txt /app/

# Instalar las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto al contenedor
COPY . /app/

# Exponer el puerto en el que Django estará ejecutándose
EXPOSE 8000

# Ejecutar makemigrations, migrate y luego iniciar el servidor
CMD python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py seed_data && \
    python manage.py create_user && \
    python manage.py runserver 0.0.0.0:8000