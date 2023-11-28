nombres_columnas = {
    0: "A",
    1: "D",
    2: "F",
    3: "G",
    4: "V",
    5: "X"
}


def cifrar(texto, permutacion, tablero, espaciar_cada = 5):
    texto_entrada = texto.replace(" ", "")
    texto_salida = ""
    for letra in texto_entrada:
        for n_fila, fila in enumerate(tablero):
            for n_columna, columna in enumerate(fila):
                if letra == columna:
                    primer_caracter = nombres_columnas[n_fila]
                    segundo_caracter = nombres_columnas[n_columna]
                    texto_salida += primer_caracter + segundo_caracter

    permutacion = list(permutacion)
    copia_permutacion = permutacion.copy()
    copia_permutacion.sort()
    permutacion_numerica = []

    for letra in permutacion:
        permutacion_numerica.append(copia_permutacion.index(letra)+1)

    #dividir el texto en len(permutacion) grupos
    #ordenar los grupos segun la permutacion
    #unir los grupos en un solo texto

    print(permutacion_numerica)

    texto_salida = list(texto_salida)
    texto_salida_dividido = []
    texto_salida_dividido_ordenado = []
    for i in range(0, len(permutacion)):
        texto_salida_dividido.append([])
        texto_salida_dividido_ordenado.append([])

    for indice, letra in enumerate(texto_salida):
        columna = indice % len(permutacion)
        texto_salida_dividido[columna].append(letra)

    for i, indice in enumerate(permutacion_numerica):
        texto_salida_dividido_ordenado[indice-1] = texto_salida_dividido[i]

    #Aplanar la lista
    texto_salida_dividido_ordenado = [item for sublist in texto_salida_dividido_ordenado for item in sublist]
    texto_salida_dividido_ordenado = "".join(texto_salida_dividido_ordenado)
    texto_salida_dividido_ordenado = " ".join(texto_salida_dividido_ordenado[i:i+espaciar_cada] for i in range(0, len(texto_salida_dividido_ordenado), espaciar_cada))
    return texto_salida_dividido_ordenado


if __name__ == "__main__":
    tablero= [
        ["A", "1", "M", "E", "5", "N"],
        ["O", "S", "B", "2", "C", "3"],
        ["D", "4", "F", "6", "G", "7"],
        ["H", "8", "I", "9", "J", "0"],
        ["K", "L", "P", "Q", "R", "T"],
        ["U", "V", "W", "X", "Y", "Z"]
    ]

    texto_entrada = "CON UN POCO DE PACIENCIA ESTO SE PUEDE LEER"
    permutacion = "CRIPTA"

    print(cifrar(texto_entrada, permutacion, tablero, 5))