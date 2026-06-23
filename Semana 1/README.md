# Reto 01 - Calculadora de Sumas

##  Descripcion
Este programa lee multiples lineas desde la entrada estandar (stdin). Cada linea contiene numeros separados por comas y el programa debe limpiar caracteres no validos, convertir los valores a enteros, truncar los decimales (NO redondear), sumar los valores e imprimir el resultado por cada linea.

##  Reglas del Problema
- Si la linea esta vacia  resultado = 0  
- Los numeros pueden tener espacios  
- Se deben ignorar caracteres no numericos  
- Los decimales se truncan (ejemplo: 3.9 = 3)  
- Valores invalidos cuentan como 0  
- Puede haber comas extra, valores vacios, caracteres mezclados y numeros negativos  

##  Ejemplos
Entrada:
1,2,3  
4.9,5.1  
10,a,20  

Salida:
6  
9  
30  

##  Como Ejecutarlo
En Linux / Mac:
python3 main.py < input.txt

En Windows:
python main.py < input.txt

Tambien puedes ejecutar:
python main.py
y escribir las lineas manualmente.



##  Autor
Cesar Gonzalez