import collections
import string

frecuencias_esperadas = {
    'A': 0.1152, 'B': 0.022, 'C': 0.0411, 'D': 0.0501, 'E': 0.1217,
    'F': 0.0069, 'G': 0.017, 'H': 0.0073, 'I': 0.0568, 'J': 0.0021,
    'K': 0.0011, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'O': 0.0868,
    'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798, 'T': 0.0463,
    'U': 0.0291, 'V': 0.0111, 'W': 0.0004, 'X': 0.0024, 'Y': 0.0106,
    'Z': 0.0047, 'Ñ': 0.0031
}

def calcular_chi_cuadrado(texto, frecuencias_esperadas = frecuencias_esperadas):
    # Calcular las frecuencias observadas de letras en el texto
    frecuencias_obs = collections.Counter(texto.upper())

    chi_squared = 0
    for letra in string.ascii_uppercase + 'Ñ':
        Oi = frecuencias_obs[letra]
        Ei = frecuencias_esperadas[letra] * len(frecuencias_obs)
        chi_squared += ((Oi - Ei) ** 2) / Ei
    return chi_squared

if __name__ == "__main__":
    #Pregunta si quiere abrir un archivo o ingresar un texto
    print("Elija una opción: ")
    print("1. Abrir archivo")
    print("2. Ingresar texto")
    opcion = input("Opción: ")
    if (opcion == "1"):
        archivo = input("Ingrese el nombre del archivo: ")
        with open(archivo, 'r') as archivo:
            texto = archivo.read()
    else:
        texto = input("Ingrese el texto para calcular el chi-cuadrado: ")

    chi_cuadrado = calcular_chi_cuadrado(texto, frecuencias_esperadas)

    print(f"Valor de chi-cuadrado: {chi_cuadrado}")




