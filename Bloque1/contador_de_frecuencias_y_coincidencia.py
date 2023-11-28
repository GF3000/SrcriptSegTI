texto = "Anticorrupcion intenta evitar que el error de la jueza tumbe la macrooperacion contra la mafia rusa ligada a cargos del PP"
texto= texto.replace(" ", "")
texto = texto.upper()
distancia_objetivo = abs(ord("A")-ord("E"))

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frecuencias_alfabeto = {}
for letra in alfabeto:
    frecuencias_alfabeto[letra] = 0

for letra in texto:
    frecuencias_alfabeto[letra] += 1

#Método Kasiski
print(f"Conteo total de letras:\n{frecuencias_alfabeto}")
print("\n\n")

frecuencias_alfabeto = sorted(frecuencias_alfabeto.items(), key=lambda x: x[1], reverse=True)
frecuencias_alfabeto_copia = frecuencias_alfabeto[:6]
print(f"Top 6 letras mas frecuentes:\n{frecuencias_alfabeto_copia}")

for dupla1 in frecuencias_alfabeto_copia:
    letra1 = dupla1[0]
    for dupla2 in frecuencias_alfabeto_copia:
        letra2 = dupla2[0]
        if letra1 != letra2:
            if ord(letra1)-ord(letra2)== distancia_objetivo:
                print(f"COINCIDENCIA: {letra2} = A, {letra1} = E, frecuencias: {dupla2[1]}, {dupla1[1]}")

#Test de Kullback
print("\n\n")
suma = 0
for dupla in frecuencias_alfabeto:
    suma += dupla[1]*(dupla[1]-1)
print(f"Esperado aleatorio: {int(len(texto)*(len(texto)-1)/26)}") #IC aleatorio = 1/26
print(f"Esperado español: {int(len(texto)*(len(texto)-1)*0.0744)}") #IC español = 0.0744
print(f"Esperado ingles: {int(len(texto)*(len(texto)-1)*0.0667)}") #IC ingles = 0.0667
print(f"Observado: {suma}")


