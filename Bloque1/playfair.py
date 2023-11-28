def contruir_matriz(clave):
    if ("J" in clave):
        clave = clave.replace("J", "I")
    matriz = []
    for i in clave:
        if i not in matriz:
            matriz.append(i)
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for i in alfabeto:
        if i not in matriz:
            matriz.append(i)

    #Convert matrix to 5x5
    matriz = [matriz[i:i+5] for i in range(0, len(matriz), 5)]
    return matriz

def cifrar(texto, matriz):
    #Check if J is in the text
    for i in range(len(texto)):
        if texto[i] == "J":
            texto = texto[:i] + "I" + texto[i+1:]
    texto = texto.replace(" ", "")
    #Check if the text has an odd number of characters
    if len(texto) % 2 != 0:
        texto += "Z"
    #Divide text in pairs
    texto = [texto[i:i+2] for i in range(0, len(texto), 2)]
    texto_cifrado = ""
    for par in texto:
        fila1 = 0
        columna1 = 0
        fila2 = 0
        columna2 = 0
        for i in range(5):
            for j in range(5):
                if matriz[i][j] == par[0]:
                    fila1 = i
                    columna1 = j
                if matriz[i][j] == par[1]:
                    fila2 = i
                    columna2 = j
        if fila1 == fila2:
            texto_cifrado += matriz[fila1][(columna1+1)%5] + matriz[fila2][(columna2+1)%5]
        elif columna1 == columna2:
            texto_cifrado += matriz[(fila1+1)%5][columna1] + matriz[(fila2+1)%5][columna2]
        else:
            texto_cifrado += matriz[fila1][columna2] + matriz[fila2][columna1]

    return texto_cifrado

def descifrar(texto_cifrado, matriz):
    #Check if J is in the text
    for i in range(len(texto_cifrado)):
        if texto_cifrado[i] == "J":
            texto_cifrado = texto_cifrado[:i] + "I" + texto_cifrado[i+1:]
    texto_cifrado = texto_cifrado.replace(" ", "")
    #Divide text in pairs
    texto_cifrado = [texto_cifrado[i:i+2] for i in range(0, len(texto_cifrado), 2)]
    texto_descifrado = ""
    for par in texto_cifrado:
        fila1 = 0
        columna1 = 0
        fila2 = 0
        columna2 = 0
        for i in range(5):
            for j in range(5):
                if matriz[i][j] == par[0]:
                    fila1 = i
                    columna1 = j
                if matriz[i][j] == par[1]:
                    fila2 = i
                    columna2 = j
        if fila1 == fila2:
            texto_descifrado += matriz[fila1][(columna1-1)%5] + matriz[fila2][(columna2-1)%5]
        elif columna1 == columna2:
            texto_descifrado += matriz[(fila1-1)%5][columna1] + matriz[(fila2-1)%5][columna2]
        else:
            texto_descifrado += matriz[fila1][columna2] + matriz[fila2][columna1]

    return texto_descifrado

matrix = contruir_matriz("SALVACION")

texto_cifrado = cifrar("POR NOTICIAS DE FUENTE FIDEDIGNA SABEMOS", matrix)
print(" ".join(texto_cifrado[i:i+2] for i in range(0, len(texto_cifrado), 2)))

texto_descifrado = descifrar(texto_cifrado, matrix)
print(" ".join(texto_descifrado[i:i+2] for i in range(0, len(texto_descifrado), 2)))