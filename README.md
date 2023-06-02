# Proyecto-Final-Perricornios---Tercer-Semestre
Mismo proyecto de tienda de estética que teníamos en pSeInt

## Desde una terminal ubicada en el directorio del proyecto
- Importante : No estar ejecutando pgadmin ni postgresql al momento de lanzar el contenedor

### Para cerrarlo
- docker-compose down

### Para Lanzar el contenedor y añadirlo a DockerDesktop (Solo 1 vez y despues si tocamos configuracion de docker-composer.yml)
- docker-composer up -d
- Ejecutando este comando en una consola posicionada donde se encuentra el archivo docker.compose.yml , se añadira el volumen y los containers de postgres y pgadmin a DockerDesktop

### Para Conectarse a PGADMIN
- ingresamos a http://localhost/
- usuario :perricornios@gmail.com
- password : perricornios_pfinal
