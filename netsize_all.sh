#! /bin/bash
echo "Numero de filas" 
for i in ../Saavedra2013/*.txt #FOR CREA BUCLE
do cat $i | wc -l #IMPRIMIR LAS FILAS CON CAT
done #FINALIZA
echo "Número de columnas" #IMPRIMER LAS COLUMNAS
for i in ../Saavedra2013/*.txt #FOR CREA UN BUCLE
do head -n 1 $i| tr -d " " | tr -d "\n" | wc -c #CONTAR LOS CARACTERES DE LA PRIEMRA FILA PARA OBTENER LAS COLUMNAS
done #FINALIZA
