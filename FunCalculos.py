def crear_lista(n,valor):
    """
    Crea una lista segun los valores ingresados.
    Args:
        n = numero de posiciones que tendra el vector
        valor = valor inicial de los elementos del vector
    Returns:
        lista
    PD: creo esta funcion para no importarla ya qeu genereaba bugs
    """
    lista= [valor] * n
    return lista

def calcular_promedios(matriz_calificaciones:list)->list:
    """
    Calcula el promedio de las columnas de la matriz de calificaciones
    Args:
        matriz de calificaciones
    Returns:
        lista de promedios
    """
    lista_promedios = crear_lista(len(matriz_calificaciones),0)
    for i in range(len(matriz_calificaciones)):
        suma = 0
        cant = 0
        for j in range(len(matriz_calificaciones[i])):
            suma = suma + matriz_calificaciones[i][j]
            cant = cant + 1
        if cant > 0:
            promedio = suma / cant
        else:
            promedio = 0
        lista_promedios[i] = promedio
    return lista_promedios

def indice_max_promedio(lista_promedios:list)->int:
    """
    Busca el indice con el promedio mas alto
    Args:
        lista de promedios
    Returns:
        indice de la materia con mayor promedio
    """
    indice_max = 0
    max_valor = lista_promedios[0]
    for i in range(0, len(lista_promedios)):
        if lista_promedios[i] > max_valor:
            max_valor = lista_promedios[i]
            indice_max = i
    return indice_max

def ordenar_burbuja_ascendente(lista: list) -> list:
    """
    Ordena una lista de forma ascendente.
    """
    for i in range(len(lista)):
        for j in range(0, (len(lista) - i) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_burbuja_descendente(lista: list) -> list:
    """
    Ordena una lista de forma descendente.
    """
    for i in range(len(lista)):
        for j in range(0, (len(lista) - i) - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def buscar_por_legajo(lista_legajos:list, numero_legajo:int, estados:list)->int:
    """
    Busca el indice segun un numero de legajo ingresado
    Args:
    lista de estados
    lista de legajos
    numero de legajo
    Returns:
        numero de indice
    """
    for i in range(len(lista_legajos)):
        if str(lista_legajos[i]) == str(numero_legajo):
            if estados[i] == 1:
                return i
    return -1

def contar_calificaciones_en_materia(matriz:list, columna:int)->list:
    """
    Devuelve una lista de conteos para calificaciones 1..10 en la columna dada.
    """
    repeticiones = crear_lista(11, 0)
    for i in range(len(matriz)):
        nota = matriz[i][columna -1]
        if nota >= 1 and nota <= 10:
            repeticiones[nota] = repeticiones[nota] + 1
    return repeticiones






























