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
    for clave in dic.keys():
        print(clave)
    usrInKey = str(input())
    usrInKey = usrInKey.upper() # ← Paso la palabra a mayuscula
    
    #verifica si la palabra del usuario existe
    if usrInKey in dic:
        print("Introduce la palabra:")
        # print(dic[usrInKey].keys())
        for palClave in dic[usrInKey].keys():
            print(palClave,", ", end="")
        print("> ")
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
# VERSION 1
# def anadirPalabra(dic):
#     print("Has seleccionado 'Añadir palabra'")
    
#     Existe = False
    
#     usrInPal = str(input("Introduce una palabra: "))
#     usrInPal = usrInPal.lower()

#     print("\nPara que se utiliza? o que es?")
#     usrDefinePal = input("Añade una definicion: ")
    
#     for clave in dic.keys():
#         for pal in dic[clave].keys():
#             if pal == usrInPal:
#                 Existe = True
#                 break

#     if(usrInPal == Existe):
#         print("Ya existe esta palabra")
#     elif(usrInPal != Existe):
#         dic.update({usrInPal: usrDefinePal})
#         # imprimir_diccionario(dic)
#         # return dic
#   VERSION 2  
#  def anadirPalabra(dic):

#     # que quieres, añadir una palabra nueva, o añadir una acepcion de una que ya exista
#     print("Que quieres hacer?")
#     print(" 1- Añadir Palabra nueva")
#     print(" 2- Añadir accepcion a una palabra")
#     opcion = int(input())
#     Existe = False
#     match (opcion):
#         case 1:
#                 nuevaPal = input("Introduce la palabra nueva: ").upper()
#                 for clave in dic.keys():
#                     if clave == nuevaPal:
#                         print("Esta palabra ya existe, volviendo al menu")
#                         Existe = True
#                 if Existe == False:
#                     while True:
#                         usrInPal = str(input("Introduce una acepcion: ")).lower()
#                         print("\nPara que se utiliza? o que es?")
#                         usrDefinePal = input("Añade una definicion: ")
#                         usrInDefPal = {usrInPal:usrDefinePal}
#                         dic.update({nuevaPal: usrInDefPal})
#                         opcion = input("Quieres introducir una nueva palabra?\n 1- si \n 2- no")
#                         if opcion == 2 : break
def anadirPalabra(dic):
    while True:
        # que quieres, añadir una palabra nueva, o añadir una acepcion de una que ya exista
        print("Que quieres hacer?")
        print(" 1- Añadir Palabra nueva")
        print(" 2- Añadir acepcion a una palabra")
        opcion = int(input())

        if opcion == 1:
            nuevaPal = input("Introduce la palabra nueva: ").upper()
            if nuevaPal in dic:
                print("Esta palabra ya existe, volviendo al menu")
            else:
                # dic[nuevaPal] = {}
                while True:
                    usrInPal = input("Introduce una acepcion: ").lower()
                    print("\nPara que se utiliza? o que es?")
                    usrDefinePal = input("Añade una definicion: ")
                    usrInDefPal = {usrInPal:usrDefinePal}
                    dic.update({nuevaPal: usrInDefPal})
                    # dic[nuevaPal][usrInPal] = usrDefinePal
                    opcion = input("Quieres introducir otra acepcion?\n 1- si \n 2- no ")
                    if opcion == '2':
                        break
        elif opcion == 2:
            palabra_existente = input("Introduce la palabra existente: ").upper()
            if palabra_existente in dic:
                while True:
                    usrInPal = input("Introduce una acepcion: ").lower()
                    print("\nPara que se utiliza? o que es?")
                    usrDefinePal = input("Añade una definicion: ")
                    dic[palabra_existente].update({usrInPal: usrDefinePal})
                    # dic[palabra_existente][usrInPal] = usrDefinePal
                    opcion = input("Quieres introducir otra acepcion?\n 1- si \n 2- no ")
                    if opcion == '2':
                        break
            else:
                print("La palabra no existe en el diccionario.")
        else:
            print("Opción no válida.")
            continue

        # opcion = input("¿Quieres realizar otra operación?\n 1- sí \n 2- no ")
        # if opcion == '2':
        break

    #     case 2:

    # for clave in dic.keys():
    #     for pal in dic[clave].keys():
    #         if pal == usrInPal:
    #             Existe = True
    #             break

    # if(usrInPal == Existe):
    #     print("Ya existe esta palabra")
    # elif(usrInPal != Existe):
    #     dic.update({usrInPal: usrDefinePal})
    #     imprimir_diccionario(dic)
    #     return dic
   
def modificarPalabra(dic):
    # diccionario["PEPE"] = diccionario.pop("CULTO")
    # diccionario["PEPE"]["Macarrones"] = diccionario["PEPE"].pop("Spagetti")
    # diccionario["PEPE"]["Macarrones"] = "Los jueves se come rabo de toro"
    clear()
    print("Has seleccionado modificar!")

    print(" 1- Modificar nombre de una relacion")
    print(" 2- Modificar nombre de una palabra")
    print(" 3- Modificar descripcion")
    print("  - He cambiado de idea (volver)")
    opcion = int(input("> "))

    print("\nEstas son las relaciones existentes:")
    for rel in sorted(dic.keys()):
        print(rel)
    
    usrInRel = input("Cual quieres cambiar?\n> ").upper()

    match opcion:
        case 1:
            # Modificar nombre de una relacion
            usrNewRel = input("Introduce el nuevo nombre de relacion:").upper()
            dic[usrNewRel] = dic.pop(usrInRel)
        case 2:
            # Modificar nombre de una palabra
            print("Contiene estas palabras: ")
            for pal in sorted(dic[usrInRel].keys()):
                print(pal)
            usrPal = input("Cual de estas quieres cambiar?\n>").lower()

            usrNewPal = input("Introduce el nuevo nombre de palabra:").lower()
            dic[usrInRel][usrNewPal] = dic[usrInRel].pop(usrPal)
        case 3:
            # Modificar descripcion
            print("Contiene estas palabras: ")
            for pal in sorted(dic[usrInRel].keys()):
                print(pal)
            usrPal = input("Cual de estas quieres cambiar?\n>").lower()

            usrInDesc = input("Introduce una nueva descripcion").lower()
            dic[usrInRel][usrPal] = usrInDesc
        case _:
            # Salir
            print("Valor no valido")



#! - ELIMINAR PALABRA -
def EliminaPalabra(dic):
   # diccionario["PEPE"] = diccionario.pop("CULTO")
    # diccionario["PEPE"]["Macarrones"] = diccionario["PEPE"].pop("Spagetti")
    # diccionario["PEPE"]["Macarrones"] = "Los jueves se come rabo de toro"
    clear()
    print("Has seleccionado eliminar!")

    print(" 1- Eliminar una relacion")
    print(" 2- Eliminar una palabra")
    print("  - He cambiado de idea (volver)")
    opcion = int(input("> "))

    print("\nEstas son las relaciones existentes:")
    for rel in sorted(dic.keys()):
        print(rel)
    
    usrDelRel = input("Cual quieres eliminar?\n> ").upper()

    match opcion:
        case 1:
            # Modificar nombre de una relacion
            confirma = input("Estas seguro? s/n")
            if confirma == "s": dic.pop(usrDelRel)
        case 2:
            # Modificar nombre de una palabra
            print("Contiene estas palabras: ")
            for pal in sorted(dic[usrDelRel].keys()):
                print(pal)
            usrDelPal = input("Cual de estas quieres eliminar?\n>").lower()
            confirma = input("Estas seguro? s/n")
            if confirma == "s": dic[usrDelRel].pop(usrDelPal)
        
        case _:
            # Salir
            print("Valor no valido")

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
    print("  ──  ──  Añadir/Modificar Palabra  ──  ──   ")
    print("─────────────────────────────────────────────")
    print(" 1- Modifica una palabra")
    print(" 2- Añadir Palabra")
    opcion = input("Selecciona una opción (1-2): ")
    match int(opcion):
        case 1: dic = modificarPalabra(dic)
        case 2: anadirPalabra(dic)
        case _: print("Opcion no valida")

def mostrar_DeletePal(dic):
    clear()
    print("─────────────────────────────────────────────")
    print("  ──  ──  ──  Eliminar Palabra  ──  ──  ──   ")
    print("─────────────────────────────────────────────")
    EliminaPalabra(dic)
    
    #TODO PENDIENTE DE HACER