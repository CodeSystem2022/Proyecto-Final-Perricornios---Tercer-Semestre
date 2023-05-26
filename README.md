# Proyecto-Final-Perricornios---Tercer-Semestre
Mismo proyecto de tienda de estética que teníamos en pSeInt


Para lanzar el contenedor
docker-compose up

Para cerrarlo
docker-compose down

Para recrearlo (Solo si tocamos configuracion de docker-composer.yml)
docker-composer up -d

Para Conectarce a PGADMIN
ingresamos a http://localhost/
usuario :perricornios@gmail.com
password : perricornios_pfinal





















Cada vez que se hace un cambio se debe reconstruir la imagen
docker build -t proyecto-final .

para lanzar la imagen
docker run -d -p 5432:5432 --name proyecto_final -e POSTGRES_PASSWORD=root -v $PWD/pgdata:/var/lib/postgresql/data postgres