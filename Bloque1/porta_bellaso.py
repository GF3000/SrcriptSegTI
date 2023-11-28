grupo1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
grupo2 = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


claves = {}
for indice, letra in enumerate(grupo1):
    parte = []
    for indice2 in range(indice, len(grupo1)):
        parte.append(grupo2[indice2])
    for indice2 in range(0, indice):
        parte.append(grupo2[indice2])
    claves[(len(grupo1) - indice) % len(grupo1)] = [grupo1, parte]





def encontrar_coincidendia(texto, palabra):
    claves_posibles = [] 
    texto_binario = ""
    palabra_binario = ""
    texto_sin_espacios = texto.replace(" ", "")
    for letra in texto_sin_espacios:

        if letra in grupo1:
            texto_binario += "1"
        else:
            texto_binario += "2"
        
    for letra in palabra:
        if letra in grupo1:
            palabra_binario += "2"
        else:
            palabra_binario += "1"
    print("Texto original: \n" + texto_sin_espacios)
    print("Texto binario: \n" + texto_binario)
    print("Palabra binario: \n" + palabra_binario)
    find = texto_binario.find(palabra_binario)
    while find != -1:
        clave_final = []
        letra_descifrada = ""
        letra_cifrada = ""
        print("Coincidencia: " + str(find))
        for indice, letra in enumerate(palabra):
            letra_descifrada = letra
            letra_cifrada = texto_sin_espacios[find:find+len(palabra)][indice]
            print(f"{letra_descifrada} | {letra_cifrada}")
            for index in range(0, len(claves)):
                if letra_descifrada in grupo1:
                    indice_descifrada = claves[index][0].index(letra_descifrada)
                    if (claves[index][1][indice_descifrada] == letra_cifrada):
                        clave_final.append(index)
                else:
                    indice_descifrada = claves[index][1].index(letra_descifrada)
                    if (claves[index][0][indice_descifrada] == letra_cifrada):
                        clave_final.append(index)

        claves_posibles.append(clave_final)
        print("Clave = " + str(clave_final))

        
        find = texto_binario.find(palabra_binario, find+1)
    return claves_posibles


def descifrar(texto_cifrado, clave, palabra=""):
    texto_cifrado = texto_cifrado.replace(" ", "")
    for i in range(0, len(clave)):
        texto_impresion = ""
        clave_a_usar = []
        #append clave[i:] + clave[:i] element by element
        for indice in range(i, len(clave)):
            clave_a_usar.append(clave[indice])
        for indice in range(0, i):
            clave_a_usar.append(clave[indice])
        texto_impresion += "\nClave a usar: " + str(clave_a_usar) + "\n"
        espacios = 0
        for i in range(0, len(texto_cifrado)):
            letra_cifrada = texto_cifrado[i]
            if (letra_cifrada == " "):
                print(" ", end="")
                espacios += 1
                continue

            clave_en_uso = claves[clave_a_usar[(i-espacios)%len(clave_a_usar)]]
            if letra_cifrada in grupo1:
                indice = clave_en_uso[0].index(letra_cifrada)
                letra_descifrada = clave_en_uso[1][indice]
            else:
                indice = clave_en_uso[1].index(letra_cifrada)
                letra_descifrada = clave_en_uso[0][indice]
            texto_impresion += letra_descifrada
        if palabra in texto_impresion:
            print(texto_impresion)
            return texto_impresion
texto = "EUABA YSYNA KYHIY JVCIR JIBXB IUGKB GSTMV RGCIN VHYYR IGCUB PKIXJ NHBKE WKTHR OPQHH NIILT DTDWF RHHIZ CMQIR JHMTA YUZYR IWTLB PUXVV JMXLZ DLHFC UHSTB PDHIN PGIWV IHPFR JMXTB JGHFR IUKBV TNBFE WVTSK HICIP FTJRV IHOFZ FLXTP TTQEG WVTNR ZPHLN UTXHC PUELR USTVA TUHLE WLAIL EAGRZ FLTHC PYXUN KHWIB WHGWY RTXHC DLELR JYHIB DWIIE RHJXA DGIEP WSIMC DWCJG FILXB JSHWO WYMJR CMCJB NLATA UABKB WYRRR OPZKE WLWOR KPQEQ FUZOC YKGNY WLMTS YGZJB CYHWK HAPRS RWORA PLDRE WWOIJ ALZXV NGWIM JYGNR JMTUR XAFRR EXIWV SUYXE NYHW"
palabra = "HABITUALMENTE"
print(texto)
# clave = [6, 7, 9, 7, 4, 3]
# descifrar(texto, clave)
encontrar_coincidendia(texto, palabra)

#Introducir clave "a mano"
descifrar(texto, [7, 9, 2, 6, 1, 4, 0, 4, 6, 7], palabra)



                
