import misFunciones

diccionario = { # ← Aqui se guardan los indices (palabras clave)
    "PIEDRA": {
        "roca": "Texto de piedra.roca",
        "chinita": "piedrecita en el zapato"
    },
    "INFORMATICA": {
        "minecra": "Es un juego",
        "brotato": "Es otro juego"
    }
}
palabraIndx = {} # ← Aqui se guardan las palabras
palabraDesc = "" # ← Aqui se guarda la descripcion de una palabra


def main():
    while True:
        misFunciones.clear()
        misFunciones.mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        match int(opcion):
            case 1:
                print("Has seleccionado ''")
                misFunciones.mostrar_BuscaMenu()
                opcion = input("Selecciona una opción (1-2): ")
                misFunciones.buscarPalabra()
                #print(diccionario)
            case 2:
                print("Has seleccionado 'Añadir palabra'")
                #diccionario.update(palabraIndx.update(palabraDesc))
            case 3:
                print("Has seleccionado 'eliminar palabra'")
            case 4:
                print("has seleccionado salir")
                break
            case _:
                print("Valor no valido")
        input("Pulsa Enter para continuar... ")

if __name__ == "__main__":
    main()