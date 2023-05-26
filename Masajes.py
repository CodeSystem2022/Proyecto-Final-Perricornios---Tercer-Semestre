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
        try:
            opciones = {
                    1: "Masaje relajante",
                    2: "Masaje descontracturante",
                    3: "Masaje terapéutico",
            }

            print("Elegí una opción: ")
            for key, value in opciones.items():
                print(f"{key}. {value}")

            eleccion = int(input("\nIngresá el número del masaje elegido: "))

            # condicional- estructra if, se verifica si la elección es válida
            # y seguarda el nombre del masaje en el atributo que declaramos como vacío
            if eleccion in opciones:
                self.masaje = opciones[eleccion]
                print(f"\nElegiste ~ {self.masaje} ~")
            else:
                print("\nOpción no válida. Volvé a intentarlo nuevamente.")

        except Exception as e:
                print(f"Se produjo un error: {str(e)}")

#se instancia un objeto
masaje = Masaje()
#se llama al método
masaje.masajes()
