
def validar_calificacion(calificacion:int)->bool:
    """
    Valida que una calificación esté en el rango permitido(1-10)
    Args:
        calificacion: calificacion a validar
    Returns:
        True si está entre 1 y 10, False cuando no
    """
    
    if calificacion <= 10 and calificacion >=1:
        return True
    else:
        return False

def validar_legajo(numero_legajo:str)->bool:
    """
    valida que el numero de legajo tenga 6 cifras
    args:
        numero_legajo: número de legajo a validar
    returns:
        True si tiene 6 cifras o False si no
    """
    numero_legajo = (int(numero_legajo))
    if numero_legajo <= 100000 or numero_legajo >= 999999:
        return False
    else:
        return True

def validar_estado(estado:int)->bool:
    """
    Valida que el estado este en 0 o en 1
    Args:
        estado: valor que tiene el estado
    returns:
        True si es 1
        False si es 0
    """
    if estado == 1:
        return True
    else:
        return False
   
def validar_genero(genero: str)->bool:
    """
    Valida que el género sea uno de los valores permitidos
    Args:
        genero: carácter que representa el género
    Returns:
        True si es 'F', 'M' o 'X', False en caso contrario
    """
    genero_mayus = convertir_a_mayusculas(genero)
    if genero_mayus == "F" or genero_mayus == "M" or genero_mayus == "X":
        return True
    else:
        return False
    
def convertir_a_mayusculas(cadena)->str:
    """
    Convierte un string a letras mayusculas
    Args:
        cadena de caracteres a transformar
    Returns:
        cadena ingresada pero en mayusculas
    """

    resultado = ""
    for caracter in cadena:
        if ord(caracter) >= 97 and ord(caracter) <= 122:
            codigo_minuscula = ord(caracter) - 32
            resultado += chr(codigo_minuscula)
        else:
            resultado += caracter
    return resultado

def validar_nombre(nombre:str)->bool:
    """
    Valida si el nombre ingresado es correcto
    args:
        nombre
    returns:
        True si es valido o False si no
    """
    for caracter in nombre:
        if (ord(caracter)>=65 and ord(caracter) <=90) or (ord(caracter) >=97 and ord(caracter) <=122) or (ord(caracter) ==32):
            continue
        else:
            return False
    return True
    # verificar_nombre = validar_nombre("Bruno Costazos")
    # print(f"verificacion: {verificar_nombre}")

 






























