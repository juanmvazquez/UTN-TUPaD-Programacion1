# ejercicio 1

print("Hola mundo")

# ejercicio 2

nombre = input("Ingrese su nombre : ")
print(f"Mi nombre es {nombre}")

# ejercicio 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Hola {nombre} {apellido} tu edad es de {edad} anios y tu lugar de residencia es en {residencia}")

# ejercicio 4

print("Ingrese el radio de un circulo para calcular el area")
radio = float(input("Radio de circulo: "))
area = 3.14 * (radio * radio)
perimetro = 2 * 3.14 * radio
print(f"el area del circulo es de {area} y el perimetro es de {perimetro}")

# ejercicio 5

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"la cantidad de horas que son los {segundos} segundos es de {horas} horas")

# ejercicio 6

numero = int(input("Ingrese un numero para saber su tabla de multiplicar: "))
resultado = numero * 1
print(f"{numero} * 1 : {resultado}")
resultado = numero * 2
print(f"{numero} * 2 : {resultado}")
resultado = numero * 3
print(f"{numero} * 3 : {resultado}")
resultado = numero * 4
print(f"{numero} * 4 : {resultado}")
resultado = numero * 5
print(f"{numero} * 5 : {resultado}")
resultado = numero * 6
print(f"{numero} * 6 : {resultado}")
resultado = numero * 7
print(f"{numero} * 7 : {resultado}")
resultado = numero * 8
print(f"{numero} * 8 : {resultado}")
resultado = numero * 9
print(f"{numero} * 9 : {resultado}")
resultado = numero * 10
print(f"{numero} * 10 : {resultado}")

# ejercicio 7

numA = int(input("Ingrese el numero 1 : "))
numB = int(input("Ingrese el numero 2 : "))

suma = numA + numB
print(f"el resultado de la suma es : {suma}")
resta = numA - numB
print(f"el resultado de la resta es : {resta}")
division = numA / numB
print(f"el resultado de la division es : {division}")
multiplicacion = numA * numB
print(f"el resultado de la multiplicacion es : {multiplicacion}")
resto = numA % numB
print(f"el resultado de la resto es : {resto}")

# ejercicio 8 

peso = int(input("Ingrese su peso en kg : "))
altura = int(input("Ingrese su altura en centimetros : "))
metros = altura/100
imc = peso / (metros*metros)
print(f"Su indice de masa corporal es de {imc}")

# ejercicio 9 

celsius = int(input("Ingrese la temperatura en grados celcius : "))
faren = 9/5 * celsius + 32
input(f"La temperatura en grados farenheit es de {faren}")

# ejercicio 10

numA = int(input("Ingrese el numero 1 : "))
numB = int(input("Ingrese el numero 2 : "))
numC = int(input("Ingrese el numero 3 : "))

promedio = (numA + numB + numC)/3
print(f"El promedio es de {promedio}")
