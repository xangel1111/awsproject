CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- Crear la base de datos 'shop'
CREATE DATABASE IF NOT EXISTS shop;

-- Conceder privilegios al usuario 'root' sobre la base de datos 'shop'
GRANT ALL PRIVILEGES ON shop.* TO 'root'@'%';

-- Asegurarse de que los privilegios sean recargados
FLUSH PRIVILEGES;
