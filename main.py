# se puede hacer un import para llamar otro fichero/Documento
# y para usarlo mas tarde hay que escribir el nombre del fichero y punto la funcion que quieres llamar
import misFunciones

diccionario = { # ← el diccionario con palabras de muestra
    "PIEDRA": {
        "roca": "Piedra de gran tamaño",
        "chinita": "piedrecita en el zapato"
    },
    "INFORMATICA": {
        "minecra": "Es un juego de cubos",
        "brotato": "Es un juego en el que eres una patata con metralletas",
        "roca": "Esta palabra no tiene nada que ver con informatica pero necesitaba hacer una prueba"
    },
    "CULTO": {
        "kkk": "Es un grupo racista (como tú)",
        "Llados": "Un grupo que consiste en no ser un panza",
        "Spagetti": "Los jueves se come Spagetti"
    }
}

def main():
    misFunciones.banner_inicio()

    while True:
        misFunciones.clear()
        misFunciones.mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        match int(opcion):
            case 1: misFunciones.mostrar_BuscaMenu(diccionario)
            case 2: misFunciones.mostrar_AddModPal(diccionario)
            case 3: misFunciones.mostrar_DeletePal(diccionario)
            case 4: 
                print("has seleccionado salir")
                break
            case _: print("Valor no valido")
        input("Pulsa Enter para continuar... ")

if __name__ == "__main__":
    main()