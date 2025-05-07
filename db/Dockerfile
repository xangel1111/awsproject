FROM mysql:8.0

# Copiar el archivo de configuración personalizado de MySQL
COPY my.cnf /etc/mysql/my.cnf

# Copiar el script de inicialización
COPY init.sql /docker-entrypoint-initdb.d/

# Exponer el puerto 3306
EXPOSE 3306

# Establecer la variable de entorno para la IP
ENV MYSQL_ALLOW_REMOTE_HOST=ec2-18-224-32-188.us-east-2.compute.amazonaws.com
