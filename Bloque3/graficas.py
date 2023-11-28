import matplotlib.pyplot as plt
import collections

file = open("secreto_largo_AMEN.txt", "r")
mensaje_cifrado = file.read()
file.close()

# Make an histogram of the frequencies of the letters
frecuencias = collections.Counter(mensaje_cifrado)
#Sort keys
frecuencias = collections.OrderedDict(sorted(frecuencias.items()))
#Set transparency
plt.bar(frecuencias.keys(), frecuencias.values(), alpha=0.5)



file = open("secreto_largo_preprocesado.txt", "r")
mensaje_cifrado = file.read()
file.close()

# Make an histogram of the frequencies of the letters
frecuencias = collections.Counter(mensaje_cifrado)
frecuencias = collections.OrderedDict(sorted(frecuencias.items()))
plt.bar(frecuencias.keys(), frecuencias.values(), alpha=0.5)
plt.show()