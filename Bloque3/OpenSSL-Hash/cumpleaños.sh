#!/bin/bash

# Función para mostrar la ayuda y las opciones disponibles
show_help() {
  echo "Uso: $0 -iter_max NUM_MAX_ITERACIONES"
  echo "Genera pares de texto con identificadores aleatorios y busca colisiones en sus resúmenes hash SHA-256."
  echo ""
  echo "Opciones disponibles:"
  echo "  -iter_max NUM_MAX_ITERACIONES  Especifica el número máximo de iteraciones."
  echo "  -h, --help                     Muestra esta ayuda."
  echo ""
  exit 1
}

# Valor predeterminado para iter_max
iter_max=2000

# Captura el tiempo de inicio
start_time=$(date +%s)

# Procesar argumentos de línea de comandos
while [[ $# -gt 0 ]]; do
  case "$1" in
    -iter_max)
      iter_max="$2"
      shift 2
      ;;
    -h | --help)
      show_help
      ;;
    *)
      echo "Opción no válida: $1"
      show_help
      ;;
  esac
done

for ((iteracion = 0; iteracion < iter_max; iteracion++)); do
    ident=$(openssl rand -hex 6)
    texto_1="{\"mensaje\": \"ALZA\", \"id\": \"$ident\"}"
    ident=$(openssl rand -hex 6)
    texto_2="{\"mensaje\": \"BAJA\", \"id\": \"$ident\"}"
    resumen_1=$(echo -n "$texto_1" | openssl dgst -sha256 -binary | xxd -p -c 256 | tr -d '\n')
    resumen_2=$(echo -n "$texto_2" | openssl dgst -sha256 -binary | xxd -p -c 256 | tr -d '\n')
    echo "Iteración: $iteracion"
    echo "Texto 1: $texto_1"
    echo "Texto 2: $texto_2"
    echo "Resumen 1: $resumen_1"
    echo "Resumen 2: $resumen_2"
    if [ "${resumen_1:0:2}" == "${resumen_2:0:2}" ]; then
        echo "Colisión encontrada!"
        echo "Texto 1: $texto_1"
        echo "Resumen 1: $resumen_1"
        echo "Texto 2: $texto_2"
        echo "Resumen 2: $resumen_2"
        break
    fi
done

# Captura el tiempo de finalización
end_time=$(date +%s)

# Calcula el tiempo transcurrido
elapsed_time=$((end_time - start_time))

# Muestra el tiempo transcurrido
echo "Tiempo empleado: $elapsed_time segundos."
