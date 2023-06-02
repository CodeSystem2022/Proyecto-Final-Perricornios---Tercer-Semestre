# Proyecto-Final-Perricornios---Tercer-Semestre
Mismo proyecto de tienda de estética que teníamos en pSeInt

![perricorniospseint](https://github.com/CodeSystem2022/Proyecto-Final-Perricornios---Tercer-Semestre/assets/92758405/58da16cb-b222-4129-a2b8-ca3050f19592)

## Desde una terminal ubicada en el directorio del proyecto
- Importante : No estar ejecutando pgadmin ni postgresql al momento de lanzar el contenedor

### Para lanzar el contenedor
- docker-compose up

### Para cerrarlo
- docker-compose down

### Para recrearlo (Solo si tocamos configuracion de docker-composer.yml)
- docker-composer up -d

### Para Conectarse a PGADMIN
- ingresamos a http://localhost/
- usuario :perricornios@gmail.com
- password : admin

### Para crear conexion a base de datos desde PGADMIN
- HOST : postgres
- Usuario : perricornios
- Password : perricornios_pfinal
