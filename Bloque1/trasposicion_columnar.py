import itertools

def descifrar_transposicion(mensaje_cifrado, clave):
    mensaje_cifrado = mensaje_cifrado.replace(" ", "")
    longitud_mensaje = len(mensaje_cifrado)


    # Calcular numero de columnas

    numero_columnas = len(clave)
    elementos_por_columnas = longitud_mensaje // numero_columnas 

    
    # Inserta el mensaje en una matriz
    
    lista_columnas = []
    tamanno_fila = len(mensaje_cifrado) // numero_columnas
        
    for i in range(numero_columnas):
        lista_columnas.append([])
    puntero_letra = 0
    for columna in range(numero_columnas):
        for i in range(tamanno_fila):
            if puntero_letra >= len(mensaje_cifrado):
                break
            lista_columnas[columna].append(mensaje_cifrado[puntero_letra])
            puntero_letra += 1
    # Add the remaining letters
    for i in range(puntero_letra, len(mensaje_cifrado)):
        lista_columnas[i%numero_columnas].append(mensaje_cifrado[i])
        
    # Ordenar las columnas segun la clave2
    clave_numerica = calcular_clave_numerica(clave)
    #Sort clave2_numerica
    clave_numerica = sorted(clave_numerica.items(), key=lambda x: x[1])


    nueva_lista_columnas = [[] for i in range(numero_columnas)]


    for dupla in clave_numerica:
        nueva_lista_columnas[dupla[0]] = lista_columnas[dupla[1]]
    
    print(nueva_lista_columnas)

    texto_devolver = ""
    for i in range(tamanno_fila):
        for columna in nueva_lista_columnas:
            if i >= len(columna):
                continue
            texto_devolver += columna[i]





        
    return texto_devolver
    
def calcular_clave_numerica(clave):
    clave2 = clave.upper()
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    indice = 0
    clave2_lista = list(clave)
    clave2_numerica = {i: "" for i in range(len(clave2))}
    for letra in abecedario:
        if letra in clave2_lista:
            aparciones = clave2.count(letra)
            for i in range(aparciones):
                clave2_numerica[(clave2_lista.index(letra))] = indice
                clave2_lista[clave2_lista.index(letra)] = " "
                indice += 1
    for letra in clave2_lista:
        print(letra)
    guiones = ("-" for i in range(len(clave2)))
    print("".join(guiones))
    for i in range(len(clave2)):
        print(str(clave[i]) + "-> " + str(clave2_numerica[i]+1))
    print()

    return(clave2_numerica)
        

# Mensaje cifrado proporcionado
# mensaje_cifrado = "ESCLI UMSSD YLOAA KCOSE TKEEY NEHAN ISTPI SAEUL TBEOW"
# print("Mensaje cifrado: " + mensaje_cifrado)
# mensaje_intermedio = descifrar_transposicion(mensaje_cifrado, "BRUTA")
# print("Mensaje intermedio: " + mensaje_intermedio)
# mensaje_descifrado = descifrar_transposicion(mensaje_intermedio, "FUERZA")
# print("Mensaje descifrado: " + mensaje_descifrado)
print(calcular_clave_numerica("CONTUMAZ"))
