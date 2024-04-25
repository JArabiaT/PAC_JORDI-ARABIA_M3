import misFunciones

diccionario = {} # ← Aqui se guardan los indices (palabras clave)
palabraIndx = {} # ← Aqui se guardan las palabras
palabraDesc = "" # ← Aqui se guarda la descripcion de una palabra

def main():
    while True:
        misFunciones.cls()
        misFunciones.mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        match int(opcion):
            case 1:
                misFunciones.cls()
                print("Has seleccionado ''")
                opcion = input("Selecciona una opción (1-3): ")
                print(diccionario)
            case 2:
                print("Has seleccionado 'Añadir palabra'")
                diccionario.update(palabraIndx.update(palabraDesc))
            case 3:
                print("Has seleccionado 'eliminar palabra'")
            case 4:
                print("has seleccionado salir")
                break
            case _:
                print("Valor no valido")
        input()

if __name__ == "__main__":
    main()


# paraules = {
#     "xarxa": {
#         "PESCA": 
#             """
#             Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal, 
#             anomenada malla. Són anomenades filats i, preferentment, arts.",
#             """
#         "TÈXTIL": 
#             """
#             Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà, 
#             de cànem, de lli o, modernament, de niló.",
#             """
#     },
#     "informàtica": {
#         "TECNOLOGIA": 
#             """
#             Conjunt de ciències, tècniques o activitats relacionades amb el tractament automatitzat de dades. 
#             Informàtica de gestió. Informàtica d’oficina.",
#             """
#         "NÚVOL": 
#             """
#             Organització d’un sistema informàtic en què l’usuari fa ús de recursos i serveis de processament 
#             i emmagatzematge de dades allotjats en servidors externs accessibles a través d’internet.",
#             """
#     },
#     "acrònim": {
#         "NOM": 
#             """
#             Qualsevol abreviació formada amb lletres o segments inicials o finals extrets dels mots
#             que componen una frase, que és pronunciable com un mot ordinari; per exemple, radar, làser, UNESCO,
#             etc."
#             """
#     }
# }

