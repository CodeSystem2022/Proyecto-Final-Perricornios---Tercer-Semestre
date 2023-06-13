# Proyecto-Final-Perricornios---Tercer-Semestre
Mismo proyecto de tienda de estética que teníamos en pSeInt

## Para tener en cuenta
- Asegúrate de no estar ejecutando pgadmin ni postgresql al momento de lanzar el contenedor.
- Verifica que no haya ningún otro servicio ejecutándose en los puertos 5432 y 80.
- La persistencia de la base de datos se realiza utilizando volúmenes de Docker. Por lo tanto, si realizas algún cambio en la base de datos, debes asegurarte de subir todos los cambios ubicados en la carpeta "pgdata" del proyecto, ya que es allí donde se almacena nuestro volumen.
- Desde Docker Desktop puedes eliminar los volúmenes y contenedores cuantas veces quieras sin afectar al proyecto. Para volver a levantarlos, utiliza el comando "docker-compose up -d".

### Importante!!!
- Antes de commitear los cambios se debe detener el contenedor desde Docker Desktop


### Para lanzar el contenedor y añadirlo a Docker Desktop
- Ejecuta el siguiente comando en una consola ubicada en la ubicación del archivo "docker-compose.yml":
- docker-compose up -d
- Esto añadirá el volumen y los contenedores de Postgres y Pgadmin a Docker Desktop.

### Para cerrarlo
Ejecuta el siguiente comando:
- docker-compose down

### Para conectarse a Pgadmin
Accede a http://localhost/
- Usuario: perricornios@gmail.com
- Contraseña: admin

### Para conectarse desde Pgadmin a Postgresql
Desde Pgadmin, accede a http://localhost/
- Crea una nueva conexión.
- Host: postgres
- Usuario: perricornios
- Contraseña: perricornios_pfinal
