import main
import os

#TODO -- FUNCIONES --
# -- Limpia la terminal
def clear(): #
    clear = lambda: os.system('cls')
    clear()


#! - BUSCAR EN EL DICCIONARIO -
# -- Pide al usuario la palabra Relacionada y una palabra para mostrar su descripción
def buscarPalabra(dic):
    clear()
    print("Introduce la palabra a la que está relacionada:")
    print(dic.keys())
    usrInKey = str(input())
    usrInKey = usrInKey.upper() # ← Paso la palabra a mayuscula
    
    #verifica si la palabra del usuario existe
    if usrInKey in dic:
        print("Introduce la palabra:")
        print(dic[usrInKey].keys())
        usrIn = str(input())
        usrIn = usrIn.lower() # ← Paso la palabra a minuscula

        if usrIn in dic[usrInKey]:
            print(dic[usrInKey][usrIn])

        elif usrIn not in dic[usrInKey]:
            print("La palabra que buscas no está")

    elif usrInKey not in dic:
        print("Syntax ERROR")


# -- Imprime todas las palabras con su contenido
def imprimir_diccionario(dic):
    for clave in sorted(dic.keys()): # ← pasa palabra por balabra de la biblioteca
        print(clave)
        for subclave in sorted(dic[clave].keys()):
            print("\t", subclave, ":")
            print("\t\t", dic[clave][subclave])
            print()
        print()



#! - AÑADIR/MODIFICAR PALABRA -
def anadirPalabra(dic):
    print("Has seleccionado 'Añadir palabra'")

def modificarPalabra(dic):
    
    #?Crear estructura para esta funcion especifica

    usrInPal = str(input("Introduce una palabra: "))
    usrInPal = usrInPal.lower()
    
    buscaPal = False # ← Empiezo marcando que no hay coincidencias
    countPal=0
    for clave in sorted(dic.keys()):                # ← Busca dentro de las relaciones (clave)
        for subClave in sorted(dic[clave].keys()): 
            #print(subClave) # ← Busca
            if usrInPal in subClave:              # ← Si encuentra la palabra igual dentro de clave
                buscaPal = True
                countPal = countPal + 1
                # guardar en la estructura = countPal: subClave
                if countPal == 1:
                    print("Esta palabra ya está relacionada con: ")
                break
        if buscaPal == True:
            print(clave,", ", end="")
    print("")
    
    # switch para seleccionar la relacion a modificar
    


#! - ELIMINAR PALABRA -
def EliminaPalabra(dic):
    print("(Se supone que aqui eliminas una palabra)")


#! -- MENÚS --
def banner_inicio():
    clear()
    print("─────────────────────────────────────────────")
    print("  ──  ── El Libro de las Accepciónes ──  ──  ")
    print("  ──  ──       By Jordi Arabia       ──  ──  ")
    print("─────────────────────────────────────────────")
    input("Pulsa Enter para continuar... ") 

def mostrar_menu():
    clear()
    print("─────────────────────────────────────────────")
    print("  ──  ── El Libro de las Accepciónes ──  ──  ")
    print("─────────────────────────────────────────────")
    print(" 1-v Buscar en el diccionario")
    print(" 2-x Añadir/Modificar palabra")
    print(" 3-x Eliminar palabra")
    print(" 4- Salir")

def mostrar_BuscaMenu(dic):
    clear()
    print("─────────────────────────────────────────────")
    print("  ──  ──  Buscar en el diccionario  ──  ──   ")
    print("─────────────────────────────────────────────")
    print(" 1- Buscar palabra")
    print(" 2- Mostrar todo el diccionario")
    opcion = input("Selecciona una opción (1-2): ")
    match int(opcion):
        case 1: buscarPalabra(dic)
        case 2: imprimir_diccionario(dic)
        case _: print("Opcion no valida")

def mostrar_AddModPal(dic):
    clear()
    print("─────────────────────────────────────────────")
    print("  ──  ──  ──   Añadir Palabra   ──  ──  ──   ")
    print("─────────────────────────────────────────────")
    print(" 1- Modifica una palabra")
    print(" 2- Añadir Palabra")
    opcion = input("Selecciona una opción (1-2): ")
    match int(opcion):
        case 1: modificarPalabra(dic)
        case 2: anadirPalabra(dic)
        case _: print("Opcion no valida")

def mostrar_DeletePal(dic):
    clear()
    print("─────────────────────────────────────────────")
    print("  ──  ──  ──  Eliminar Palabra  ──  ──  ──   ")
    print("─────────────────────────────────────────────")
    EliminaPalabra(dic)
