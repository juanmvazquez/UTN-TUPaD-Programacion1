# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for number in range(101):
#     print (number)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# number = input("Ingrese un numero para saber la cantidad de digitos que contiene: ")
# count = 0
# for i in number:
#     count += 1
# print(f"El número {number} tiene", count, "dígitos")

# 3) Escribe un programa que sume todos los núm3eros enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# print("Ingrese 2 numeros: ")
# numberA = int(input("Numero 1 : "))
# numberB = int(input("Numero 2 : "))
# suma = 0

# for i in range(numberA + 1, numberB):
#     suma += i
# print(f"La suma entre el numero {numberA} y el numero {numberB} es de : ", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.


# print("Ingrese numeros para sumarlos en secuencia")
# print("Cuando ingrese el numero 0 el programa finalizara")

# suma = 0

# while True:
#     number = int(input("Ingrese un numero: "))

#     if number == 0:
#         break

#     suma += number
#     print("La suma es: ", suma)

# print("La suma total es de de : ", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número

# import random

# print("Se elige al azar un numero entre 0 y 9 y tenes que elegir un numero para adivinarlo")
# randomNumber = random.randint(0,9)
# count = 0

# while True:
#     number = int(input("Ingrese un numero para adivinar: "))

#     if number < 0 and number > 9:
#         print("Numero incorrecto, ingrese un numero entre 0 y 9")
#         continue

#     count += 1

#     if number == randomNumber:
#         print(f"Correcto el numero al azar era {randomNumber} y la cantidad de intentos fue de: {count}")
#         break
#     else:
#         print("Numero incorreto, intenta de nuevo")

# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100, 0, -1):
#     if i % 2 == 0:
#         print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# print("Ingrese un numero para saber la suma de los numeros comprendidos entre el 0 y el num elegido")
# number = int(input("Ingrese un numero entero positivo : "))
# suma = 0


# if number > 0:
#     for i in range(number + 1):
#         suma += i

# print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# print("Ingre 100 numeros y el programa detectara cuales son pares impares positivos y negativos")

# count = 0
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# while count < 5:
#     number = int(input("Ingrese un numero"))

#     pares += number % 2 == 0
#     impares += number % 2 != 0

#     positivos += number > 0
#     negativos += number < 0


#     count += 1
    
# print("Pares:", pares)
# print("Impares:", impares)
# print("Positivos:", positivos)
# print("Negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# print("Ingre 100 numeros para calcular la media")

# count = 0
# suma = 0
# media = 0
# while count < 5:
#     number = int(input("Ingrese un numero: "))

#     suma += number
#     count += 1
    
# media = suma / count

# print ("La suma es de : ", suma)
# print ("la media es de : ", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

number = input("Ingrese un numero : ")
numeroInvertido = ""

for i in number:
    numeroInvertido = i + numeroInvertido

print("El número invertido es:", numeroInvertido)