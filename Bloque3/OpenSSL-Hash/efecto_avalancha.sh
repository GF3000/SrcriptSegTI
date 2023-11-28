#!/bin/bash

# Función para mostrar la ayuda y las opciones disponibles
show_help() {
  echo "Uso: $0 -funcion_hash FUNCION_HASH -num_bits NUM_BITS"
  echo "Genera 10,000 entradas de texto similares y calcula su hash."
  echo ""
  echo "Opciones disponibles:"
  echo "  -funcion_hash FUNCION_HASH  Especifica la función de resumen hash (por ejemplo, sha256)."
  echo "  -num_bits NUM_BITS          Especifica la cantidad de bits del hash (por ejemplo, 256)."
  echo "  -h, --help                  Muestra esta ayuda."
  echo ""
  exit 1
}

# Variables predeterminadas
funcion_hash=""
num_bits=""

# Procesar argumentos de línea de comandos
while [[ $# -gt 0 ]]; do
  case "$1" in
    -funcion_hash)
      funcion_hash="$2"
      shift 2
      ;;
    -num_bits)
      num_bits="$2"
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

# Verificar que se hayan especificado la función de resumen hash y el número de bits
if [ -z "$funcion_hash" ] || [ -z "$num_bits" ]; then
  echo "Debes especificar la función de resumen hash (-funcion_hash) y el número de bits (-num_bits)."
  show_help
fi

# Crear directorio de salida
output_directory="hash_outputs"
mkdir -p "$output_directory"

# Generar 100 entradas de texto similares y calcular sus hashes
for i in {1..100}; do
  entrada="Texto de entrada $i"
  valor_hash=$(echo -n "$entrada" | openssl dgst -"$funcion_hash" -binary | xxd -p -c "$num_bits" | tr -d '\n')
  echo "$entrada: $valor_hash" >> "$output_directory/hashes.txt"
done

echo "Hashes calculados y guardados en el directorio $output_directory/hashes.txt."
