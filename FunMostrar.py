def imprimir_matriz(matriz: list) -> None:
    """
    imprime la matriz por consola
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end=" ")
 
def imprimir_lista(lista: list) -> None:
    """
    imprime la lista por consola
    """
    
    for i in range(len(lista)):
            print(f"{lista[i]}", end=" ")

def mostrar_datos_cargados(matriz_calificaciones:list,lista_nombres:list,lista_generos:list,lista_legajos:list,lista_estados:list)->None:
    """
    Muestra los datos ya cargados en el programa.
    Args:
    matriz_calificaciones, lista_nombres, lista_generos, lista_estados
    """
    for i in range(len(lista_estados)):
         if lista_estados[i]==1:
              print("DATOS DE ALUMNOS CARGADOS")
              print("-Legajo:", lista_legajos[i])
              print("-Nombre:", lista_nombres[i])
              print("-Género:", lista_generos[i])
              print("-Calificaciones: ")
              print("Mat_1\tMat_2\tMat_3\tMat_4\tMat_5")
              print()
              for j in range(len(matriz_calificaciones[i])):
                    print(f"{matriz_calificaciones[i][j]:>5}",end="  ")
                              
def buscar_estudiante_por_legajo(legajos:list, legajo:str)->int:
    """
    Busca el estudiante segun el numero de legajo ingresado
    Args:
        lista legajos
        numero de legajo a buscar
    Retuns:
        indice de el estudiante buscado
    """
    for i in range(len(legajos)):
        if legajos[i] == legajo:

            return i + 1
    return 0

def mostrar_indice_mayor_promedio(indice_materia:int)->None:
    """
    Muestra el nombre de la materia segun el requerimiento dado MATERIA_ i+1
    Args:
        indice de la materia
    Retuns:
        nombre de la materia
    """
    print("MATERIA_",indice_materia+1)

def mostrar_estudiante_por_legajo(promedios:list, nombre:list, genero:list, legajo:list, legajo_buscado:int)->None:
    """
    Muestra los datos de un estudiante buscado segun su numero de legajo
    Args:
        lista promedios
        lista nombres
        lista generos
        lista legajos
        numero de legajo buscado
    Retuns:
        Datos de el estudiante
    """
    encontrado = False
    for i in range(len(legajo)):
        if legajo[i] == legajo_buscado:
            print("Estudiante encontrado.")
            print(f"Número de legajo: {legajo[i]}")
            print(f"-Nombre: {nombre[i]}")
            print(f"-Genero: {genero[i]}")
            print(f"-Promedio: {promedios[i]}")
            encontrado = True
            break
    if encontrado == False:
        print("Legajo no encontrado.")

def mostrar_conteo_calificaciones(repeticiones:list)->None:
    """
    Muestra la cantidad de repeticiones que tiene cada nota en determinada materia
    Args:
        repeticiones de las notas
    Returns:
        cantidad de veces que se repite cada nota
    """
    for nota in range(1, 11):
        print(f"La nota {nota} se repite: {repeticiones[nota]}")

def salir_programa()->None:
    """
    salir del programa
    """
    print("Cerrando programa.")






