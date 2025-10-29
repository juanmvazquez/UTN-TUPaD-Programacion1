# def holaMundo():
#     print("Hola Mundo!")

# holaMundo()

# --------------------------------------------------------------

# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# def saludarUsuario(nombre):
#     saludo = "Hola " + nombre + "!"
#     return saludo


# name = input("Ingrese su nombre: ")
# message = saludarUsuario(name)
# print(message)

# --------------------------------------------------------------

# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# def personalInformation(firstName, lastName, age, residence):
#     print(f"Soy {firstName} {lastName}, tengo {age} anios y vivo en {residence}.")

# firstName = input("Ingrese su nombre: ")
# lastName = input("Ingrese su apellido: ")
# age = input("Ingrese su edad: ")
# residence = input("Ingrese su lugar de residencia: ")

# personalInformation(firstName, lastName, age, residence)

# --------------------------------------------------------------

# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# import math

# def calculateCircleArea(radius):
#     area = math.pi * radius ** 2
#     return area

# def calculateCirclePerimeter(radius):
#     perimeter = 2 * math.pi * radius
#     return perimeter


# radius = float(input("Ingrese el radio del circulo: "))

# areaResult = calculateCircleArea(radius)
# perimeterResult = calculateCirclePerimeter(radius)

# print(f"El area del circulo es: {areaResult:.2f}")
# print(f"El perímetro del circulo es: {perimeterResult:.2f}")

# --------------------------------------------------------------

# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# def secondsToHours(seconds):
#     hours = seconds / 3600
#     return hours

# seconds = float(input("Ingrese la cantidad de segundos: "))

# hoursResult = secondsToHours(seconds)
# print(f"{seconds} segundos equivalen a {hoursResult:.2f} horas.")

# --------------------------------------------------------------

# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def multiplicationTable(number):
#     print(f"Tabla de multiplicar del {number}:")
#     for i in range(1, 11):
#         result = number * i
#         print(f"{number} x {i} = {result}")

# number = int(input("Ingrese un numero: "))
# multiplicationTable(number)

# --------------------------------------------------------------

# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# def basicOperations(a, b):
#     addition = a + b
#     subtraction = a - b
#     multiplication = a * b
#     division = a / b if b != 0 else "Indefinida (division por cero)"
#     return (addition, subtraction, multiplication, division)

# numberA = float(input("Ingrese el primer numero: "))
# numberB = float(input("Ingrese el segundo numero: "))

# results = basicOperations(numberA, numberB)

# print("Resultados de las operaciones:")
# print(f"Suma: {results[0]}")
# print(f"Resta: {results[1]}")
# print(f"Multiplicación: {results[2]}")
# print(f"División: {results[3]}")

# --------------------------------------------------------------

# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# def calculateImc(weight, height):
#     imc = weight / (height ** 2)
#     return imc

# weight = float(input("Ingrese su peso en kilogramos: "))
# height = float(input("Ingrese su altura en metros: "))

# imcResult = calculateImc(weight, height)

# print(f"Su indice de masa corporal (IMC) es: {imcResult:.2f}")

# --------------------------------------------------------------

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


# def celsiusToFahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# fahrenheitResult = celsiusToFahrenheit(celsius)

# print(f"{celsius:.2f}°C equivalen a {fahrenheitResult:.2f}°F")

# --------------------------------------------------------------

# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# def calculateAverage(a, b, c):
#     average = (a + b + c) / 3
#     return average


# numberA = float(input("Ingrese el primer numero: "))
# numberB = float(input("Ingrese el segundo numero: "))
# numberC = float(input("Ingrese el tercer numero: "))

# averageResult = calculateAverage(numberA, numberB, numberC)

# print(f"El promedio de los tres numero es: {averageResult:.2f}")
