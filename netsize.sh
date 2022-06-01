#! /bin/bash
echo "Filename : ../data/Saavedra2013/n1.txt" #IMPRIMIR TEXT DE UNA CARPETA 
echo "Número de filas" #IMPRIME EL NÚMERO DE FILAS
cat  ../Saavedra2013/n1.txt | wc -l #IMPRIME ALGO QUE ESTA HECHO
echo "Número de columnas" #IMPRIME EL NÚMERO DE COLUMNAS
head -n1 ../Saavedra2013/n1.txt | tr -d " " | tr -d "\n" | wc -c #LEE LO CARACTERES DELA PRIMERA LÍNEA 
 
