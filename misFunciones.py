import main
import os

# -- FUNCIONES --
def clear(): #
    clear = lambda: os.system('cls')
    clear()


# - BUSCAR EN EL DICCIONARIO -
def buscarPalabra():
    clear()
    print("Introduce la palabra que quieres buscar:")
    usrIn = str(input())
    if (usrIn == main.diccionario) == True:
        print(main.diccionario[usrIn])

# - AÑADIR PALABRA -

# - ELIMINAR PALABRA -


# -- MENÚS --
def mostrar_menu():
    clear()
    print("  ──  ── El Libro de las Accepciónes ──  ──  ")
    print("─────────────────────────────────────────────")
    print(" 1- Buscar en el diccionario")
    print(" 2- Añadir palabra")
    print(" 3- Eliminar palabra")
    print(" 4- Salir")

def mostrar_BuscaMenu():
    clear()
    print("  ──  ──  Buscar en el diccionario  ──  ──   ")
    print("─────────────────────────────────────────────")
    print(" 1- Buscar por palabra")
    print(" 2- Mostrar todo el diccionario")


