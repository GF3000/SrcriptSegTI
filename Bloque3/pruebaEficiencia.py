import cProfile
import random as Random
import criptoanalisis_vigenere as vigenere


archivo_cifrado = "Pruebas/secreto_largo_AMEN.txt"
mensaje_cifrado = open(archivo_cifrado, 'r').read()
cProfile.run("vigenere.obtener_clave(mensaje_cifrado)", sort="cumtime")