import matplotlib.pyplot as plt
import collections

file1 = open("Pruebas/secreto_largo_AMEN.txt", "r")
file2 = open("Pruebas/secreto_largo_preprocesado.txt", "r")

mensaje_cifrado = file1.read()
file1.close()

# Primera gráfica

frecuencias = collections.Counter(mensaje_cifrado)
frecuencias = collections.OrderedDict(sorted(frecuencias.items()))
plt.bar(frecuencias.keys(), frecuencias.values(), alpha=0.5)

# Segunda gráfica

mensaje_cifrado = file2.read()
file2.close()

frecuencias = collections.Counter(mensaje_cifrado)
frecuencias = collections.OrderedDict(sorted(frecuencias.items()))
plt.bar(frecuencias.keys(), frecuencias.values(), alpha=0.5)

# Muestra las gráficas
plt.show()