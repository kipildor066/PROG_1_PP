from FunValidaciones import validar_calificacion, validar_nombre, convertir_a_mayusculas,validar_legajo



def crear_matriz(filas:int,columnas:int,valor_inicial:int)->list:
    """
    Crea una matriz bidimensional segun valores iniciales dados
    Args:
        filas: número de filas de la matriz
        columnas: número de columnas de la matriz
        valor_inicial: valor con el que se iniciliza la matriz
    Returns:
        matriz bidimensional 
    """
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def crear_lista(posiciones:int, valor_inicial:any)->list:
    """
    Crea una lista
    Args:
        posiciones: cantidad de elementos de la lista
        valor_inicial: valor con el que se inicializa la lista
    Returns:
        lista unidimensional
    """
    lista = [valor_inicial] * posiciones
    return lista

def poblar_lista_nombres(lista_nombres:list,lista_estados:list)->list:
    """
    Rellena la lista de nombres y cambia la lista de estados de 0 a 1
    Args:
        lista_nombres
        lista_estados
    Returns:
        lista_nombres poblada
    """
 
    for i in range(len(lista_nombres)):
        if lista_estados[i]==0:
            nombre = input("Ingrese el nombre del alumno: ")

            if (len(nombre) > 0) and validar_nombre(nombre):
                    lista_nombres[i] = nombre
                    lista_estados[i] = 1  
                    break
            else:
                print("Nombre iválido. Por favor ingrese el nombre nuevamente.")
        
        continuar = input("Continuar? S/N")
        if continuar == "N" or continuar == "n":
            break
    return lista_nombres

def poblar_matriz_calificaciones(matriz_calificaciones:list, lista_estados:list) ->list:
    """
    Carga las calificaiones de los estudiantes en la matriz correspondiente
    Args:
        matriz de calificaciones
        lista de estados
    Returns:
        matriz poblada de calificaciones
    """
    for i in range(len(matriz_calificaciones)):
        if lista_estados[i] == 1:
            for j in range(len(matriz_calificaciones[i])):
                    if matriz_calificaciones[i][j] == 0:
                        while True:
                            calificacion = int(input("Ingrese la nota: "))
                            if validar_calificacion(calificacion):
                                matriz_calificaciones[i][j] = calificacion
                                break
                            else:
                                print("Nota fuera del rango permitido. Ingrese una nota entre 1 y 10.")

    return matriz_calificaciones

def poblar_lista_genero(lista_generos:list,lista_estados:list) ->list:
    """
    rellena la lista de generos con los datos proporcionados
    Args:
        lista de generos
        lista de estados
    Retuns:
        lista de generos poblada
    """
    for i in range (len(lista_generos)):
        if lista_estados[i] == 1 and lista_generos[i] == 0:
            genero = convertir_a_mayusculas(input("Ingrese el genero del estudiante:(M|F|X)"))
            lista_generos[i] = genero
    return lista_generos

def poblar_lista_legajos(lista_legajos:list,lista_estados:list)-> list:
    """
    Rellena con el numero de legajo la lista legajos
    Args:
        lista legajos
        lista estados
    Retuns:
        lista de legajos poblada
    """
    for i in range(len(lista_legajos)):
        if lista_estados[i] == 1 and lista_legajos[i] == 0:
            while True:
                legajo = input("Ingrese el numero de legajo (6 cifras): ")
                if validar_legajo(legajo):
                    lista_legajos[i] = legajo
                    break
                else:
                    print("Numero de legajo inválido. Debe tener exactamente 6 cifras numéricas.")
    return lista_legajos


   