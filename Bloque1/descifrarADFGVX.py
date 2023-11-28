# Definimos el tablero ADFGVX
tablero = [
    ["L", "I", "9", "B", "2", "E"],
    ["5", "R", "A", "1", "C", "3"],
    ["D", "4", "F", "6", "G", "7"],
    ["H", "8", "J", "0", "K", "M"],
    ["N", "O", "P", "Q", "S", "T"],
    ["U", "V", "W", "X", "Y", "Z"]
]

# Definimos la clave de permutación
permutacion = "CONTUMAZ"

# Definimos el criptograma
criptograma = "VAVVV AXVVA VAADA XVDVV GXFAD DADDA DGVXG VDVVA DAXXX VXAAF ADXAD FAXDA XDVXA VGVVV VAVDF ADVXD DDXD"

# Eliminamos los espacios del criptograma
criptograma = criptograma.replace(" ", "")

# Desciframos la fase de trasposición
def descifrar_trasposicion(criptograma, permutacion):
    # Calculamos el tamaño de las columnas
    longitud = len(criptograma)
    num_cols = len(permutacion)
    num_rows = int(longitud / num_cols) + (longitud % num_cols > 0)
    
    # Inicializamos la matriz de descifrado
    matriz = ['' for _ in range(num_rows)]
    
    # Ordenamos la permutación y creamos un índice para las columnas
    permutacion_ordenada = sorted([(char, i) for i, char in enumerate(permutacion)])
    indice_columnas = {char: i for i, (char, _) in enumerate(permutacion_ordenada)}
    
    # Rellenamos la matriz con el criptograma
    pos = 0
    for _, original_index in permutacion_ordenada:
        for row in range(num_rows):
            if pos < longitud and (row < num_rows - 1 or original_index < longitud % num_cols):
                matriz[row] += criptograma[pos]
                pos += 1
    
    # Leemos la matriz en el orden correcto para obtener el texto cifrado con ADFGVX
    descifrado = ''
    for row in matriz:
        for char in permutacion:
            col = indice_columnas[char]
            if col < len(row):
                descifrado += row[col]

    
    
    return descifrado

# Desciframos la fase de sustitución
def descifrar_sustitucion(descifrado, tablero):
    texto_plano = ''
    for i in range(0, len(descifrado), 2):
        # Buscamos el índice de la letra en el tablero
        fila = 'ADFGVX'.index(descifrado[i])
        columna = 'ADFGVX'.index(descifrado[i + 1])
        # Añadimos el caracter correspondiente al texto plano
        texto_plano += tablero[fila][columna]
    return texto_plano

# Ejecutamos las funciones de descifrado
descifrado_trasposicion = descifrar_trasposicion(criptograma, permutacion)
texto_plano = descifrar_sustitucion(descifrado_trasposicion, tablero)

# Mostramos el resultado
print("Texto descifrado:", texto_plano)