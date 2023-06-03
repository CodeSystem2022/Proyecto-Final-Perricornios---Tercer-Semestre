"""
Se requiere crear una clase Masaje, la misma debe contar con los siguientes atributos y métodos:

Atributos:

Masaje String
Metodos :

masajes() : Se requiere contar con un método que ofrezca una selección de masajes y guarde la elección en la variable Masaje


"""
class Masaje:
    def __init__(self):
        self.masaje = "" #se inicializa como una cadena vacía en el constructor

    #funcion: muestra las opciones de masajes
    def masajes(self):
        print('\n----OPCIONES DE MENU----\n')
        
        opciones = {
                1: "Masaje convencional",
                2: "Masaje descontracturante",
                3: "Masaje terapéutico",
            }

        #para validar se usa un bucle while true
        #se va a ejecutar hasta que se ingrese una opción valida
        while True:

            try:
                print("Elegí una opción: ")
                for key, value in opciones.items():
                    print(f"{key}. {value}")

                eleccion = int(input("\nIngresá el número del masaje elegido: "))

                # condicional- estructra if, se verifica si la elección es válida
                # y seguarda el nombre del masaje en el atributo que declaramos como vacío
                if eleccion in opciones:
                    self.masaje = opciones[eleccion]
                    print(f"\nElegiste ~ {self.masaje} ~")
                    break

                else:
                    print(f"\nOpción no válida. ({eleccion}) Volvé a intentarlo nuevamente.\n")

            except Exception as e:
                    print(f"Se produjo un error: {str(e)} <NO PARECE SER UNA OPCIÓN VALIDA>")
                    print('Por favor, intentalo nuevamente..\n')

#se instancia un objeto
#masaje = Masaje()
#se llama al método
#masaje.masajes()
