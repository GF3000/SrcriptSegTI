import string
import cesar
import chicuadrado
import time

# Frecuencias esperadas de letras en español
frecuencias_esperadas = {
    'A': 0.1152, 'B': 0.022, 'C': 0.0411, 'D': 0.0501, 'E': 0.1217,
    'F': 0.0069, 'G': 0.017, 'H': 0.0073, 'I': 0.0568, 'J': 0.0021,
    'K': 0.0011, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'O': 0.0868,
    'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798, 'T': 0.0463,
    'U': 0.0291, 'V': 0.0111, 'W': 0.0004, 'X': 0.0024, 'Y': 0.0106,
    'Z': 0.0047, 'Ñ': 0.0031
}

# Función para calcular el chi-cuadrado
def calcular_chi_cuadrado(frecuencias_obs, frecuencias_esp = frecuencias_esperadas):
    chi_squared = 0
    for letra in string.ascii_uppercase + 'Ñ':
        Oi = frecuencias_obs[letra]
        Ei = frecuencias_esp[letra] * len(frecuencias_obs)
        chi_squared += ((Oi - Ei) ** 2) / Ei
    #print(f"Chi-cuadrado: {chi_squared}")
    return chi_squared


if __name__ == "__main__":
    archivo_cifrado = input("Nombre del archivo cifrado: ")
    with open(archivo_cifrado, 'r') as archivo:
        mensaje_cifrado = archivo.read()

    # Calcular frecuencias de letras en el mensaje cifrado

    # Inicializar variables para mantener un seguimiento de la clave y el chi-cuadrado mínimo
    clave_minima = 0
    chi_cuadrado_minimo = 0.1

    # Probar todas las posibles claves César
    claves = {}
    for clave in range(27):  # Ahora incluye la 'Ñ'
        mensaje_descifrado = cesar.descifrar(mensaje_cifrado, clave)
        chi_cuadrado = chicuadrado.calcular_chi_cuadrado(mensaje_descifrado)
        claves[clave] = chi_cuadrado
    claves = dict(sorted(claves.items(), key=lambda item: item[1]))
    print(claves)
    #input("Presione Enter para continuar...")
    # Encuentra la clave con el menor valor de chi-cuadrado
    clave_minima = min(claves, key=claves.get)

    # Descifrar el mensaje utilizando la clave encontrada
    mensaje_descifrado = cesar.descifrar(mensaje_cifrado, clave_minima)

    print(f"Clave César encontrada: {clave_minima}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    while True:
        respuesta = input("¿Es este el mensaje original? (s/n): ")
        if respuesta == 's':
            respuesta = input("¿Desea guardar el resultado? (s/n): ")
            if respuesta == 's':
                archivo_descifrado = input("Nombre del archivo: ")
                with open(archivo_descifrado, 'w') as archivo:
                    archivo.write(mensaje_descifrado)
                print(f"Archivo guardado como {archivo_descifrado}")
            else:
                exit()
        else:
            frecuencia_max = min(claves, key=claves.get)
            claves.pop(frecuencia_max)
            clave_minima = min(claves, key=claves.get)
            mensaje_descifrado = cesar.descifrar(mensaje_cifrado, clave_minima)
            print(f"La clave encontrada es: {clave_minima}")
            print(f"Mensaje descifrado: {mensaje_descifrado}")


