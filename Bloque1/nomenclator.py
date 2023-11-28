import random


nomenclator = {
    "A": [23, 33, 38, 40, 65, 74, 84, 86, 93, 102, 109, 113, 125, 143, 163, 166, 172, 175, 180, 186, 204],
    "B": [16, 24, 26, 70, 81, 155],
    "C": [1, 32, 73, 85, 92, 101, 124, 139, 152, 179, 205],
    "D": [7, 20, 41, 54, 66, 75, 89, 99, 133, 136, 188],
    "E": [18, 21, 31, 35, 43, 50, 56, 58, 60, 68, 76, 90, 100, 116, 132, 134, 137, 149, 150, 158, 161, 183, 189, 192, 198, 202],
    "F": [141],
    "G": [61, 97, 106, 184, 194],
    "H": [13, 34, 55, 110, 191],
    "I": [25, 28, 37, 46, 63, 80, 118, 127, 140, 154, 170],
    "J": [39, 47, 121],
    "K": [206],
    "L": [10, 22, 27, 79, 91, 95, 104, 145, 182, 190],
    "M": [3, 15, 45, 117, 157, 167],
    "N": [44, 51, 64, 69, 78, 128, 135, 174, 196, 199, 203],
    "O": [2, 4, 6, 8, 11, 14, 29, 42, 67, 83, 88, 96, 98, 105, 107, 111, 120, 122, 129, 146, 156, 165, 168, 178, 195, 197],
    "P": [57, 130, 159, 162, 177],
    "Q": [114, 147, 200],
    "R": [17, 59, 62, 82, 112, 142, 144, 153, 160, 164, 169, 171],
    "S": [9, 12, 19, 72, 87, 108, 119, 123, 126, 138, 151, 176, 181, 187],
    "T": [5, 30, 52, 94, 103],
    "U": [48, 53, 71, 77, 115, 131, 148, 173, 185, 201],
    "V": [36, 49],
    "W": [207],
    "X": [193],
    "Y": [208],
    "Z": [209]
}

def cifrar (texto):
    devuelve = ""
    for letra in texto:
        if letra.isalpha():
            numero = random.choice(nomenclator[letra.upper()])
            devuelve += str(numero) + " "
            print(f"{letra} -> {numero}")
        else:
            print(f"{letra} -> {letra}")
            devuelve += letra
    return devuelve

def descifrar (texto):
    devuelve = ""
    for numero in texto.split():
        if numero.isdigit():
            for letra in nomenclator:
                if int(numero) in nomenclator[letra]:
                    print(f"{numero} -> {letra}")
                    devuelve += letra
        else:
            print(f"{numero} -> {numero}")
            devuelve += numero
    return devuelve

if __name__ == "__main__":
    texto_cifrado = "78 105 99 149 121 18 87 114 201 50 176 116 87 84 95 194 186 203 73 195 128 79 93 19 71 208 143"
    print(descifrar(texto_cifrado))
