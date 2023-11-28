#NO FUNCIONA

# def ubchi_cifrar(texto, clave1, clave2):
#     texto_cifrado = ""
#     texto = texto.replace(" ", "") 
#     clave1_numerica = clave_to_number(clave1)
#     clave2_numerica = clave_to_number(clave2)

#     for clave in [clave1_numerica, clave2_numerica]:
#         # Divide el texto en una matriz de len(clave1) columnas
#         texto = [texto[i:i+len(clave1)] for i in range(0, len(texto), len(clave1))]
#         print(texto)

#         # Ordena las columnas de la matriz según la clave1
#         texto_ordenado = []
#         for columna in clave1_numerica:
#             texto_ordenado.append([])
#         for columna in clave1_numerica:
#             #Coge los caracteres de la columna
#             nueva_columna = []
#             for fila in texto:
#                 nueva_columna.append(fila[columna-1])
#             #Añade la columna a la matriz
#             texto_ordenado[clave1_numerica.index(columna)-1] = nueva_columna
        
#         nueva_columna = []
#         for fila in range(len(clave)):
#             nueva_columna.append([])
#         for columna, indice in enumerate(clave1_numerica):
#             nueva_columna[columna+1] = texto_ordenado[indice-1]

#         nueva_columna = texto_ordenado
#         #Aplana la matriz
#         texto_ordenado = [item for sublist in texto_ordenado for item in sublist]
#         texto = "".join(texto_ordenado)

#     print(texto_ordenado)
#     return texto_cifrado

# def clave_to_number(clave):
#     #Replace each letter with its position in the alphabet
#     clave = [ord(letra)-65 for letra in clave]
#     #Convert the lowest number to 1, the second lowest to 2, etc.
#     clave_numerica = []
#     # Fill clave_numerica with len(clave) zeros
#     for i in range(len(clave)):
#         clave_numerica.append(0)
#     for i in range(len(clave)):
#         clave_numerica[(clave.index(min(clave)))] = i+1
#         clave[clave.index(min(clave))] = 100
#     return clave_numerica

# # Ejemplo de uso
# texto_original = "ESTO ES ALGO QUE LOS DEMAS NO DEBERAN SABER NUNCA"
# clave1 = "CASTILLA"
# clave2 = "CASTILLA"

# texto_cifrado = ubchi_cifrar(texto_original, clave1, clave2)
# print("Texto cifrado:", texto_cifrado)

