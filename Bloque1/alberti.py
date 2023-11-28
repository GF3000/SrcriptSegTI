import random

class Clave:
    coincidencia = []
    frec_giro = 0
    giro = []
    disco_interno = []

    def __init__(self, coincidencia, frec_giro, giro, disco_interno):
        self.coincidencia = coincidencia
        self.frec_giro = frec_giro
        self.giro = giro
        self.disco_interno = disco_interno
    def __str__(self) -> str:
        return f"Clave: {self.coincidencia}, {self.frec_giro}, {self.giro}, {self.disco_interno}"

class DiscoAlberti:
    def __init__(self, clave):
        self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.clave = clave
        self.posicion = ord(clave.coincidencia[1])-ord(clave.coincidencia[0])
        self.caracteres_cifrados = 0
        self.tuplas = self.construir_duplas()
        print("Tuplas:")
        print(self.tuplas)

    def girar(self, cantidad):
        print("[+] Girando:", cantidad)
        self.posicion = (self.posicion + cantidad)
        self.tuplas = self.construir_duplas()

    def cifrar(self, letra):

        if self.caracteres_cifrados == self.clave.frec_giro:
            self.girar(self.clave.giro)
            self.caracteres_cifrados = 0
        self.caracteres_cifrados += 1
        for tupla in self.tuplas:
            if tupla[0] == letra:
                print("[+] Cifrando:", letra, "por", tupla[1])
                return tupla[1]
        
        
    def construir_duplas(self):
        tuplas = []

        clave = self.alfabeto[self.posicion:] + self.alfabeto[:self.posicion]
        for i in range(len(self.alfabeto)):
            tuplas.append((self.alfabeto[i], clave[i]))
        return tuplas
        

def generar_clave_aleatoria():
    alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    clave = random.sample(alfabeto, len(alfabeto))
    return ''.join(clave)

def cifrar_texto(texto, clave):
    disco = DiscoAlberti(clave)
    texto_cifrado = []
    for letra in texto:
        texto_cifrado.append(disco.cifrar(letra))
    return ''.join(texto_cifrado)

def descifrar_texto(texto, clave):

    clave_inversa = ''.join(sorted(clave.disco_interno))
    nueva_clave = Clave(clave.coincidencia, clave.frec_giro, clave.giro, clave_inversa)
    disco = DiscoAlberti(nueva_clave)
    texto_descifrado = []
    for letra in texto:
        texto_descifrado.append(disco.cifrar(letra))
    return ''.join(texto_descifrado)

def print_texto_cifrado(texto, intervalo):
    print("Texto cifrado:")
    cad = ""
    for i in range(0, len(texto)):
        cad += texto[i]
        if (i+1) % intervalo == 0:
            cad += " "
    print(cad)

# Ejemplo de uso
texto_original = "SIFUERAPRECISODECIR"
clave = Clave(["M", "B"], 4, 3, "ABCDZEFHIJKLGMNOPQRSTUVWXYZ")

texto_cifrado = cifrar_texto(texto_original, clave)

print("Texto original:", texto_original)
print("Clave utilizada:", clave)
print_texto_cifrado(texto_cifrado, 5)

