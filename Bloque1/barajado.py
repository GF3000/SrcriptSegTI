def cifrar(texto, columnas):
    texto = texto.replace(" ", "")
    texto_cifrado = ""
    for i in range(columnas):
        for j in range(i, len(texto), columnas):
            texto_cifrado += texto[j]
    return texto_cifrado

# NO FUNCIONA
# def descifrar(texto_cifrado, columnas):
#     texto_descifrado = ""
#     filas = len(texto_cifrado) // columnas
#     for i in range(filas):
#         for j in range(i, len(texto_cifrado), filas):
#             texto_descifrado += texto_cifrado[j]
#     return texto_descifrado

print(cifrar("ESTE ES UN MENSAJE QUE DEBERÍA PERMANECER EN SECRETO DURANTE AÑOS", 3))