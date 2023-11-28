#!/bin/bash

# Función para mostrar la ayuda y las opciones disponibles
show_help() {
  echo "Uso: $0 [OPCIÓN]..."
  echo "Cifra o descifra archivos utilizando OpenSSL."
  echo ""
  echo "Opciones disponibles:"
  echo "  -e, --encrypt           Cifra un archivo."
  echo "  -d, --decrypt           Descifra un archivo."
  echo "  -i, --input INPUT_FILE  Especifica el archivo de entrada."
  echo "  -o, --output OUTPUT_FILE  Especifica el archivo de salida."
  echo "  -a, --algorithm ALGORITHM  Especifica el algoritmo de cifrado (por ejemplo, aes-256-cbc)."
  echo "  -p, --password PASSWORD  Especifica la contraseña."
  echo "  -k, --key KEY_FILE       Especifica un archivo de clave."
  echo "  -s, --salt              Utiliza sal en el cifrado."
  echo "  -h, --help              Muestra esta ayuda."
  echo ""
  echo "Ejemplos de uso:"
  echo "  $0 -e -i archivo.txt -o archivo_cifrado.enc -a aes-256-cbc -p secreto"
  echo "  $0 -d -i archivo_cifrado.enc -o archivo_descifrado.txt -a aes-256-cbc -p secreto"
  exit 1
}

# Variables predeterminadas
encrypt=false
decrypt=false
input_file=""
output_file=""
algorithm=""
password=""
key_file=""
use_salt=false

# Procesar argumentos de línea de comandos
while [[ $# -gt 0 ]]; do
  case "$1" in
    -e | --encrypt)
      encrypt=true
      shift
      ;;
    -d | --decrypt)
      decrypt=true
      shift
      ;;
    -i | --input)
      input_file="$2"
      shift 2
      ;;
    -o | --output)
      output_file="$2"
      shift 2
      ;;
    -a | --algorithm)
      algorithm="$2"
      shift 2
      ;;
    -p | --password)
      password="$2"
      shift 2
      ;;
    -k | --key)
      key_file="$2"
      shift 2
      ;;
    -s | --salt)
      use_salt=true
      shift
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

# Verificar que se haya especificado al menos una operación (cifrado o descifrado)
if ! $encrypt && ! $decrypt; then
  echo "Debes especificar una operación: cifrado (-e) o descifrado (-d)."
  show_help
fi

# Verificar que se hayan especificado los archivos de entrada y salida
if [ -z "$input_file" ] || [ -z "$output_file" ]; then
  echo "Debes especificar archivos de entrada (-i) y salida (-o)."
  show_help
fi

# Realizar operación de cifrado o descifrado
if $encrypt; then
  if [ -z "$algorithm" ] || [ -z "$password" ]; then
    echo "Debes especificar un algoritmo de cifrado (-a) y una contraseña (-p) para cifrar."
    show_help
  fi
  if [ ! -z "$key_file" ]; then
    openssl enc -"$algorithm" -e -salt -in "$input_file" -out "$output_file" -pass "file:$key_file"
  elif $use_salt; then
    openssl enc -"$algorithm" -e -salt -in "$input_file" -out "$output_file" -k "$password"
  else
    openssl enc -"$algorithm" -e -in "$input_file" -out "$output_file" -k "$password"
  fi
fi

if $decrypt; then
  if [ -z "$algorithm" ] || [ -z "$password" ]; then
    echo "Debes especificar un algoritmo de cifrado (-a) y una contraseña (-p) para descifrar."
    show_help
  fi
  if [ ! -z "$key_file" ]; then
    openssl enc -"$algorithm" -d -in "$input_file" -out "$output_file" -pass "file:$key_file"
  elif $use_salt; then
    openssl enc -"$algorithm" -d -salt -in "$input_file" -out "$output_file" -k "$password"
  else
    openssl enc -"$algorithm" -d -in "$input_file" -out "$output_file" -k "$password"
  fi
fi
