def descifrar_homofonico(clave, texto_cifrado):
    # Convertir el texto cifrado en una lista de números
    numeros = texto_cifrado.split()
    
    # Descifrar el texto
    texto_descifrado = ""
    for numero in numeros:
        if numero in clave:
            texto_descifrado += clave[numero]
        else:
            texto_descifrado += "?"  # Carácter desconocido
    
    return texto_descifrado

# Ejemplo de clave homofónica como diccionario
clave_homofonica = {
    '01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E',
    '06': 'F', '07': 'G', '08': 'H', '09': 'I', '10': 'J',
    '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O',
    '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T',
    '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y',
    '26': 'Z'
    # ... Pueden haber más símbolos para cada letra para aumentar la seguridad
}

# Ejemplo de texto cifrado
texto_cifrado = "08 05 12 12 15"

# Descifrar el texto
texto_descifrado = descifrar_homofonico(clave_homofonica, texto_cifrado)
print("Texto descifrado:", texto_descifrado)
