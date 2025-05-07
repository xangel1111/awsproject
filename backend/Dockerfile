# Usar una imagen oficial de Python como base
FROM python:3.10-slim

# Instalar las dependencias del sistema necesarias para mysqlclient
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

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

ENV DB_HOST=ec2-18-224-32-188.us-east-2.compute.amazonaws.com

# Ejecutar makemigrations, migrate y luego iniciar el servidor
CMD python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py seed_data && \
    python manage.py create_user && \
    python manage.py runserver 0.0.0.0:8000
