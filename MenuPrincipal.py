from FunValidaciones import *
from FunCalculos import *
from FunMostrar import *
from FunCargaDatos import *
def menu_principal()->None:
    """
    Muestra el menu principal
    """
    filas = 2
    cols = 5

    matriz_calificaciones = crear_matriz(filas, cols, 0)
    nombres = crear_lista(filas, 0)
    generos = crear_lista(filas, 0)
    legajos = crear_lista(filas, 0)
    estados = crear_lista(filas, 0)
    promedios = crear_lista(filas, 0)
    datos_cargados = False

    while True:
        print("\nBienvenido al programa de notas y promedios!")
        print("1-Cargar datos de los estudiantes.")
        print("2-Mostrar datos de los estudiantes.")
        print("3-Calcular el promedio de los estudiantes.")
        print("4-Ordenar el promedios de los estudiantes.")
        print("5-Calcular promedio de cada materia.")
        print("6-Buscar estudiante por número de legajo.")
        print("7-Contar repeticiones de notas.")
        print("8-Salir.")

        opcion = int(input("Ingrese el numero de opcion (1-8): "))

        match opcion:
            case 1:
                poblar_lista_nombres(nombres, estados)
                poblar_lista_genero(generos, estados)
                poblar_lista_legajos(legajos, estados)
                poblar_matriz_calificaciones(matriz_calificaciones,estados)
                datos_cargados = True
                print("Carga completa.")

            case 2:
                if datos_cargados == False:
                    print("Error. Cargue los datos primero.")
                else:
                    mostrar_datos_cargados(matriz_calificaciones, nombres, generos, legajos, estados)

            case 3:
                if datos_cargados == False:
                    print("Error. Cargue los datos primero.")
                else:
                    promedios = calcular_promedios(matriz_calificaciones)

            case 4:
                if datos_cargados == False:
                    print("Error. Cargue los datos primero.")
                else:
                    print("¿Desea ordenar los promedios de manera DESCENDENTE?")
                    opcion = input("S/N")
                    if opcion == "S" or opcion == "s":
                        promedios = calcular_promedios(matriz_calificaciones)
                        ordenar_burbuja_descendente(promedios)
                        print("Promedios (DESC):", promedios)
                    elif opcion == "N" or opcion == "n":
                        promedios = calcular_promedios(matriz_calificaciones)
                        ordenar_burbuja_ascendente(promedios)
                        print("Promedios (DESC):", promedios)
            
            case 5:
                if datos_cargados == False:
                    print("Error. Cargue los datos primero.")
                else:
                    indices = indice_max_promedio(matriz_calificaciones)
                    mostrar_indice_mayor_promedio(indices)

            case 6:
                if datos_cargados == False:
                    print("Error. Cargue los datos primero.")
                else:
                    numero_legajo = input("Ingrese el numero de legajo: ")
                    indice = buscar_por_legajo(legajos, numero_legajo,estados)
                    if indice == -1:
                        print("Número de legajo no encontrado.")
                    else:
                        mostrar_estudiante_por_legajo(promedios,nombres,generos,legajos, numero_legajo)

            case 7:
                if datos_cargados == False:
                    print("Error. Cargue los datos primero.")
                else:
                    materia = int(input("Ingrese el numero de materia (1-5): "))
                    repeticiones = contar_calificaciones_en_materia(matriz_calificaciones, materia)
                    mostrar_conteo_calificaciones(repeticiones)
                
            case 8:
                salir_programa()
                break

            case _:
                print("Opcion inválida.")
            


            








