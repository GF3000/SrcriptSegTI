#Using descifrado_vigenere.py
import time
import string
import collections
import vigenere
import cesar
import chicuadrado

frecuencias_esperadas = {
    'A': 0.1152, 'B': 0.022, 'C': 0.0411, 'D': 0.0501, 'E': 0.1217,
    'F': 0.0069, 'G': 0.017, 'H': 0.0073, 'I': 0.0568, 'J': 0.0021,
    'K': 0.0011, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'O': 0.0868,
    'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798, 'T': 0.0463,
    'U': 0.0291, 'V': 0.0111, 'W': 0.0004, 'X': 0.0024, 'Y': 0.0106,
    'Z': 0.0047, 'Ñ': 0.0031
}

def calcular_ic(texto):
    n = len(texto)
    frecuencias = collections.Counter(texto)
    ic = sum(f * (f - 1) for f in frecuencias.values()) / (n * (n - 1))
    return ic

def encontrar_longitud_clave(mensaje_cifrado):
    max_longitud = len(mensaje_cifrado) // 2
    ic_español = 0.0744
    error_max = 0.005
    ic_promedio_max = 0
    longitud_clave = 1

    for longitud in range(1, max_longitud + 1):
        grupos = [mensaje_cifrado[i::longitud] for i in range(longitud)]
        ic_promedio_grupo = sum(calcular_ic(grupo) for grupo in grupos) / longitud
        error = abs(ic_promedio_grupo - ic_español)

        #print(f"Longitud de clave: {longitud}, IC promedio: {ic_promedio_grupo}, error: {error}")
        if error < error_max:
            return longitud
        else:
            if error > abs(ic_promedio_max-ic_español):
                ic_promedio_max = ic_promedio_grupo
                longitud_clave = longitud

    return longitud_clave
# Función para encontrar la clave en función de las frecuencias

def descifrar_vigenere(mensaje_cifrado, clave):
    return vigenere.descifrar(mensaje_cifrado, clave)

def obtener_clave(mensaje_cifrado):
    longitud_clave = encontrar_longitud_clave(mensaje_cifrado)
    print(f"Longitud de clave: {longitud_clave}")
    grupos = [mensaje_cifrado[i::longitud_clave] for i in range(longitud_clave)]
    claves_cesar = []
    for grupo in grupos:

        clave_minima = 0
        chi_cuadrado_minimo = 1e10

        # Probar todas las posibles claves César para este grupo
        for clave in range(26):
            grupo_descifrado = cesar.descifrar(grupo, chr(ord('A') + clave))
            chi_cuadrado = chicuadrado.calcular_chi_cuadrado(grupo_descifrado)
            if chi_cuadrado < chi_cuadrado_minimo:
                chi_cuadrado_minimo = chi_cuadrado
                # print(f"{clave} es mejor clave que {clave_minima}")
                clave_minima = clave
        
        # print(f"Clave César encontrada para grupo {grupos.index(grupo)}: {chr(ord('A') + clave_minima)}")

        claves_cesar.append(chr(ord('A') + clave_minima))

    # Unir las claves César para obtener la clave Vigenère
    clave_vigenere = ''.join(claves_cesar)
    return clave_vigenere

if __name__ == "__main__":
    archivo_cifrado = input("Archivo a descifrar: ")
    with open(archivo_cifrado, 'r') as archivo:
        mensaje_cifrado = archivo.read()

    start_time = time.time()
    clave_vigenere = obtener_clave(mensaje_cifrado)

    # Descifrar el mensaje completo utilizando la clave Vigenère
    mensaje_descifrado = vigenere.descifrar(mensaje_cifrado, clave_vigenere)

    print(f"Clave Vigenère encontrada: {clave_vigenere}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")
    #Imprime el tiempo de ejecución
    print(f"Tiempo de ejecución: {time.time() - start_time:.3f} segundos")
    #Pregunta si quiere guardar el archivo
    respuesta = input("¿Desea guardar el resultado? (s/n): ")
    if respuesta == 's':
        archivo_descifrado = input("Nombre del archivo: ")
        with open(archivo_descifrado, 'w') as archivo:
            archivo.write(mensaje_descifrado)
        print(f"Archivo guardado como {archivo_descifrado}")
    else:
        exit()
