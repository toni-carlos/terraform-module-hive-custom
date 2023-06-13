#!/bin/bash

while getopts f:h flag

do
        case "${flag}" in
                f) filename="$OPTARG";;
                h) help ;;
                *) echo "Invalid option: -$flag." ;;
        esac
done

command=$(cat $filename)

echo "comando sql: $command"

response=$(curl -H 'Content-Type: application/json' \
  -d "{ 'sql': '$command' }" \
  -X POST \
  http://127.0.0.1:5000/create-alter-table)

if [[ -z "$response" ]]; then
  echo "Erro na chamada da API !!!"
  exit 1
fi

echo "Retorno de chamada da API: ${response}"

status=$(echo $response | tr , '\n' | grep status | awk -F ':' '{print $2}')

if [[ $status == *"error"* ]]; then
  echo "Arquivo '$filename' processado com falha!!"
  exit 1
else
  echo "Arquivo '$filename' processado com sucesso!!"
  exit 0
fi
