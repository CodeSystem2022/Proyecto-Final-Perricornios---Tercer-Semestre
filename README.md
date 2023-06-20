# Proyecto-Final-Perricornios---Tercer-Semestre
Mismo proyecto de tienda de estética que teníamos en pSeInt

# Tablero de Actividades
Scrum Master *Bruno Leandro Cosimano Abadie*
| **Actividad** | **Asignado a** | **Anotaciones** |  |  | 
| ---- | ---- | --- | --- | --- | 
|  **00 - Implementación de Docker y Estructura de Proyecto** | *Bruno Leandro Cosimano Abadie* | **Actividad Completada** |
|  **01 - Creación de la Base de Datos y sus tablas** | *Gabriel Juan Alejandro Juhasz* | **Actividad Completada** |
|  **02 - Creación de la Clase Masaje** | *Noelia Romina Ruiz* | **Actividad Completada** | 
|  **03 - Creacion de la Clase Cliente** | *Noelia Romina Ruiz* | **Actividad Completada** | 
|  **03.1 - Clase Cliente - Funciones** | *Noelia Romina Ruiz* | **Actividad Completada** | 
|  **03.2 - Clase Cliente - Funciones** | *Bruno Leandro Cosimano Abadie* | **Actividad Completada** |
|  **03.3 - Clase Cliente - Funciones** | *Braian Guzmán Echarri* | **Actividad Completada, se requirio brindar codigo de referencia** |
|  **03.4 - Clase Cliente - Funciones** | *Carlos Fernando Villalón* | **Actividad Completada, se requirio brindar codigo de referencia** |
|  **04 - Clase Menu** | *Nadia Soledad Pereyra* | **Actividad Completada** |
|  **04.1 - Clase Menu** | *Facundo Benjamín Méndez* | **Actividad entregada fuera de tiempo** |
|  **04.2 - Creación de clase Admin** | *Noelia Romina Ruiz* | **Actividad Completada** | 
|  **04.3 - Creación de Clase Conexion** | *Juan Ignacio Encinas* | **Actividad entregada fuera de tiempo, se requirio brindar codigo de referencia** | 

#¿Como ejecutar el proyecto?
1- Abre el proyecto con tu editor de codigo
2- Inicia una terminal de comandos ubicada dentro de la carpeta principal del proyecto
3- Con Docker Desktop corriendo, ejecuta el siguiente comando en la terminal *docker-compose up -d*
4- Espera a que Docker inicie los contenedores y descarge las imagenes
5- Ejecuta el archivo main.py ubicado en la carpeta principal del proyecto

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
