# Proyecto-Final-Perricornios---Tercer-Semestre
Mismo proyecto de tienda de estética que teníamos en pSeInt

## Para tener en cuenta
- No estar ejecutando pgadmin ni postgresql al momento de lanzar el contenedor
- No tener ningun servicio ejecutandoce en los puetos 5432 y 80
- La persistencia de la base de datos se realiza utilizando volumenes de docker, por lo tanto si realizan algun cambio en la base de datos tienen que asegurarce de commitear todos los cambios ubicados en la carpeta pgdata del proyecto,dado que en ella se encuentra almacenado nuestro volumen
- Desde dockerDesktop puedes eliminar los volumenes y contenedores cuantas veces quieras sin afectar al proyecto, y volver a levantarlos con "docker-composer up -d"

### Para Lanzar el contenedor y añadirlo a DockerDesktop (Solo 1 vez y despues si tocamos configuracion de docker-composer.yml)
- docker-composer up -d
- Ejecutando este comando en una consola posicionada donde se encuentra el archivo docker.compose.yml , se añadira el volumen y los containers de postgres y pgadmin a DockerDesktop

### Para cerrarlo
- docker-compose down

### Para Conectarse a PGADMIN
- ingresamos a http://localhost/
- usuario :perricornios@gmail.com
- password : admin

### Para conectarse desde PGADMIN a Postgresql
- desde pgadmin en http://localhost/
- creamos una nueva conexion
- host : postgres
- usuario : perricornios
- password : perricornios_pfinal
