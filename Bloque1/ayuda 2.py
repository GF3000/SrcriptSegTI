entrada = " WHILE NOT REQUIRED THE SIGNERS CERTIFICATE CAN BE INCLUDED IN THE SIGNED DATA CERTIFICATES FIELD"
entrada = entrada.replace(" ", "")
cripto = [42,56,8,7,19,56,85,12,73,2,7,85,35,26,71,65,38,21,4,86,29,74,66,30,57,73,44,61,7]
diccionario = {}
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letra in abecedario:
    diccionario[letra] = []
for i in range(0, len(entrada)):
    diccionario[entrada[i]].append(i+1)

for entrada in diccionario:
    print(entrada + "-> " + str((diccionario[entrada])))

for i in range(0, len(cripto)):
    for letra in diccionario:
        if cripto[i] in diccionario[letra]:
            print(letra, end="")