FROM mysql:8.0

# Copiar un archivo de configuración personalizado de MySQL (si es necesario)
# Esto es opcional, si necesitas hacer alguna modificación al archivo de configuración
# por ejemplo, permitir conexiones remotas

COPY my.cnf /etc/mysql/my.cnf

# Copiar un script de inicialización para configurar el acceso remoto
COPY init.sql /docker-entrypoint-initdb.d/

# Exponer el puerto 3306 para conexiones MySQL
EXPOSE 3306
