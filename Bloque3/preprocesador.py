import unicodedata

def eliminar_tildes(texto):
    # Normalizar el texto para eliminar las tildes
    texto_normalizado = unicodedata.normalize('NFKD', texto)

    # Eliminar los caracteres que no sean ASCII
    texto_sin_tildes = texto_normalizado.encode('ASCII', 'ignore').decode('ASCII')

    return texto_sin_tildes

def eliminar_tildes_archivo (input, output):
    with (open(input, 'r')) as archivo_entrada, (open(output, 'w')) as archivo_salida:
        for linea in archivo_entrada:
            linea_sin_tildes = eliminar_tildes(linea)
            archivo_salida.write(linea_sin_tildes)

eliminar_tildes_archivo(input("Ingrese el nombre del archivo de entrada: "), input("Ingrese el nombre del archivo de salida: "))
