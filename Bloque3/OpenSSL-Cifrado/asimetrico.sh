#!/bin/bash

# Función para mostrar la ayuda y las opciones disponibles
show_help() {
  echo "Uso: $0 [OPCIÓN]..."
  echo "Cifra o descifra archivos utilizando OpenSSL con cifrado asimétrico."
  echo ""
  echo "Opciones disponibles:"
  echo "  -e, --encrypt           Cifra un archivo."
  echo "  -d, --decrypt           Descifra un archivo."
  echo "  -i, --input INPUT_FILE  Especifica el archivo de entrada."
  echo "  -o, --output OUTPUT_FILE  Especifica el archivo de salida."
  echo "  -k, --public-key PUBLIC_KEY_FILE  Especifica el archivo de clave pública."
  echo "  -p, --private-key PRIVATE_KEY_FILE  Especifica el archivo de clave privada."
  echo "  -h, --help              Muestra esta ayuda."
  echo ""
  echo "Ejemplos de uso:"
  echo "  $0 -e -i archivo.txt -o archivo_cifrado.enc -k clave_publica.pem"
  echo "  $0 -d -i archivo_cifrado.enc -o archivo_descifrado.txt -p clave_privada.pem"
  exit 1
}

# Variables predeterminadas
encrypt=false
decrypt=false
input_file=""
output_file=""
public_key_file=""
private_key_file=""

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
    -k | --public-key)
      public_key_file="$2"
      shift 2
      ;;
    -p | --private-key)
      private_key_file="$2"
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

# Realizar operación de cifrado o descifrado asimétrico
if $encrypt; then
  if [ -z "$public_key_file" ]; then
    echo "Debes especificar un archivo de clave pública (-k) para cifrar."
    show_help
  fi
  openssl rsautl -encrypt -pubin -inkey "$public_key_file" -in "$input_file" -out "$output_file"
fi

if $decrypt; then
  if [ -z "$private_key_file" ]; then
    echo "Debes especificar un archivo de clave privada (-p) para descifrar."
    show_help
  fi
  openssl rsautl -decrypt -inkey "$private_key_file" -in "$input_file" -out "$output_file"
fi
