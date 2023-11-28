import numpy as np

def crear_matriz(texto, orden):
    # Calcular el número de columnas necesario
    num_columnas = len(orden)

    # Calcular el número de filas necesario
    num_filas = len(texto) // num_columnas

    # Ajustar la longitud del texto si no es un múltiplo del número de columnas
    if len(texto) % num_columnas != 0:
        # Calcular cuántos caracteres adicionales se necesitan
        caracteres_adicionales = num_columnas - len(texto) % num_columnas
        # Rellenar el texto con espacios en blanco
        texto += ' ' * caracteres_adicionales

    # Crear una matriz vacía con el tamaño necesario
    matriz = np.empty((num_filas, num_columnas), dtype='U1')

    # Inicializar un índice para recorrer el texto
    indice_texto = 0

    # Llenar la matriz según el orden especificado
    for columna in orden:
        # Obtener los próximos n elementos del texto
        elementos = [c.upper() for c in texto[indice_texto:indice_texto + num_filas]]
        indice_texto += num_filas

        # Llenar la columna con los elementos
        matriz[:, columna] = elementos

    return matriz

# Ejemplo de uso
texto_ejemplo = "PYTHONISTICO"
orden_ejemplo = [0, 2, 1, 3, 4]  # Orden de escritura en las columnas

matriz_resultante = crear_matriz(texto_ejemplo, orden_ejemplo)

# Imprimir la matriz resultante
print(matriz_resultante)
