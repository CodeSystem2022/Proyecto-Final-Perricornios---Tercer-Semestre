import psycopg2

class DatabaseConnection:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexión exitosa a la base de datos")
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar a la base de datos:", error)

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error al ejecutar la consulta:", error)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

db = DatabaseConnection('localhost', '5432', 'tienda', 'perricornios', 'perricornios_pfinal')
db.connect()

query = 'SELECT * FROM Perri_Centro_Spa.Clientes'

results = db.execute_query(query)

if results is not None:
    for row in results:
        print(row)

db.close()
