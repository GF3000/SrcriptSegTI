import string

def cifrar(texto, clave):
    resultado = ""
    alfabeto = string.ascii_uppercase
    if isinstance(clave, str) and clave in alfabeto:
        clave = alfabeto.index(clave)
    for caracter in texto:
        mayuscula = caracter.isupper()
        caracter = caracter.upper()
        if caracter.isalpha() and caracter in alfabeto:
            indice_caracter = alfabeto.index(caracter)
            indice_caracter_cifrado = (indice_caracter + clave) % 26
            caracter_cifrado = alfabeto[indice_caracter_cifrado]
            if not mayuscula:
                caracter_cifrado = caracter_cifrado.lower()
            resultado += caracter_cifrado
            #print(f"El caracter {caracter} se cifra como {caracter_cifrado}")
        else:
            if not mayuscula:
                caracter = caracter.lower()
            resultado += caracter

    return resultado

def cifrar_archivo (archivo, clave):
    with open(archivo, 'r') as archivo:
        texto = archivo.read()
    texto_cifrado = cifrar(texto, clave)
    return texto_cifrado

def descifrar (texto, clave):
    resultado = ""
    alfabeto = string.ascii_uppercase
    if isinstance(clave, str) and clave in alfabeto:
        clave = alfabeto.index(clave)
    for caracter in texto:
        mayuscula = caracter.isupper()
        caracter = caracter.upper()
        if caracter.isalpha() and caracter in alfabeto:
            indice_caracter = alfabeto.index(caracter)
            indice_caracter_cifrado = (indice_caracter - clave) % 26
            caracter_cifrado = alfabeto[indice_caracter_cifrado]
            if not mayuscula:
                caracter_cifrado = caracter_cifrado.lower()
            resultado += caracter_cifrado
            #print(f"El caracter cifrado {caracter} se descifra como {caracter_cifrado}")
        else:
            if not mayuscula:
                caracter = caracter.lower()
            resultado += caracter
    return resultado

def descifrar_archivo (archivo, clave):
    with open(archivo, 'r') as archivo:
        texto = archivo.read()
    texto_descifrado = descifrar(texto, clave)
    return texto_descifrado

if __name__ == "__main__":
    respuesta = input("¿Quiere trabajar con un archivo o con un texto? (a/t): ")
    archivoB = False
    if respuesta == "a":
        archivoB = True
    respuesta = input("¿Quiere cifrar o descifrar? (c/d): ")
    if respuesta == 'c':
        if archivoB:
            archivo = input("Nombre del archivo a cifrar: ")
            clave = input("Ingrese la clave: ")
            texto_cifrado = cifrar_archivo(archivo, clave)
            print(f"Texto cifrado: {texto_cifrado}")
            texto_descifrado = descifrar(texto_cifrado, clave)
            print(f"Texto descifrado: {texto_descifrado}")
        else:
            texto = input("Ingrese texto: ")
            clave = input("Ingrese la clave: ")
            texto_cifrado = cifrar(texto, clave)
            print(f"Texto cifrado: {texto_cifrado}")
            texto_descifrado = descifrar(texto_cifrado, clave)
            print(f"Texto descifrado: {texto_descifrado}")
    else:
        if archivoB:
            archivo = input("Nombre del archivo a descifrar: ")
            clave = input("Ingrese la clave: ")
            texto_descifrado = descifrar_archivo(archivo, clave)
            print(f"Texto descifrado: {texto_descifrado}")
            texto_cifrado = cifrar_archivo(texto_descifrado, clave)
            print(f"Texto cifrado: {texto_cifrado}")
        else:
            texto = input("Ingrese texto: ")
            clave = input("Ingrese la clave: ")
            texto_descifrado = descifrar(texto, clave)
            print(f"Texto descifrado: {texto_descifrado}")
            texto_cifrado = cifrar(texto_descifrado, clave)
            
    respuesta = input("¿Quiere guardar el resultado en un archivo? (s/n): ")
    if respuesta == "s":
        archivo = input("Ingrese el nombre del archivo: ")
        with open(archivo, 'w') as archivo:
            archivo.write(texto_cifrado)
        print(f"El archivo {archivo} ha sido creado")
    else:
        print("El resultado no ha sido guardado")
   
