CREATE USER IF NOT EXISTS 'root'@'%';

-- Establecer los privilegios
GRANT ALL PRIVILEGES ON *.* TO 'root'@'${MYSQL_ALLOW_REMOTE_HOST}' IDENTIFIED BY '';

-- Crear la base de datos 'shop'
CREATE DATABASE IF NOT EXISTS shop;

-- Conceder privilegios sobre la base de datos 'shop'
GRANT ALL PRIVILEGES ON shop.* TO 'root'@'${MYSQL_ALLOW_REMOTE_HOST}';

-- Recargar los privilegios
FLUSH PRIVILEGES;
