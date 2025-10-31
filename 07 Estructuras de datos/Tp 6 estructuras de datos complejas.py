# # Ejercicio 1
# fruitPrices = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# fruitPrices['Naranja'] = 1200
# fruitPrices['Manzana'] = 1500
# fruitPrices['Pera'] = 2300

# print("Diccionario actualizado de precios:")
# print(fruitPrices)

# #----------------------------------------------------------------------------------
# # Ejercicio 2
# fruitPrices = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# fruitPrices['Banana'] = 1330
# fruitPrices['Manzana'] = 1700
# fruitPrices['Melon'] = 2800


# print(fruitPrices)

# #----------------------------------------------------------------------------------
# # Ejercicio 3
# fruitPrices = {'Banana': 1330, 'Anana': 2500, 'Melon': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# fruitList = list(fruitPrices.keys())

# print(fruitList)

# #----------------------------------------------------------------------------------
# # Ejercicio 4
# contacts = {}

# for i in range(5):
#     name = input(f"Ingrese el nombre del contacto {i + 1}: ")
#     phone = input(f"Ingrese el número telefónico de {name}: ")
#     contacts[name] = phone

# searchName = input("Ingrese un nombre para buscar: ")

# if searchName in contacts:
#     print(f"El número de {searchName} es {contacts[searchName]}")
# else:
#     print(f"{searchName} no se encuentra en la lista de contactos.")

# #----------------------------------------------------------------------------------
# # Ejercicio 5
# phrase = input("Ingrese una frase: ")

# words = phrase.split()

# uniqueWords = set(words)

# wordCount = {}

# for word in words:
#     if word in wordCount:
#         wordCount[word] += 1
#     else:
#         wordCount[word] = 1

# # Mostrar los resultados
# print(f"Palabras únicas: {uniqueWords}")
# print(f"Recuento: {wordCount}")

# #----------------------------------------------------------------------------------
# # Ejercicio 6
# students = {}


# for i in range(3):
#     name = input(f"Ingrese el nombre del alumno {i + 1}: ")
#     print(f"Ingrese las tres notas de {name}:")
    
#     note1 = float(input("Nota 1: "))
#     note2 = float(input("Nota 2: "))
#     note3 = float(input("Nota 3: "))
    
#     students[name] = (note1, note2, note3)

# print("Promedio de cada alumno:")
# for name, notes in students.items():
#     average = sum(notes) / len(notes)
#     print(f"{name}: {average:.2f}")

# #----------------------------------------------------------------------------------
# # Ejercicio 7
# partial1 = {"Ana", "Luis", "Marcos", "Sofia"}
# partial2 = {"Sofia", "Carlos", "Luis", "Lucia"}

# bothPassed = partial1 & partial2

# onePassed = partial1 ^ partial2

# atLeastOne = partial1 | partial2

# print(f"aprobaron ambos parciales: {bothPassed}")
# print(f"aprobaron solo uno de los dos: {onePassed}")
# print(f"aprobaron al menos un parcial: {atLeastOne}")

#----------------------------------------------------------------------------------
# Ejercicio 8
productStock = {
    "manzana": 10,
    "banana": 15,
    "pera": 8
}

print("Stock actual:")
print(productStock)

product = input("Ingrese el nombre del producto: ").lower()

if product in productStock:
    print(f"El producto '{product}' tiene un stock de {productStock[product]} unidades.")
    
    addUnits = input("¿Desea agregar unidades a este producto? (si/no): ").lower()
    if addUnits == "si":
        quantity = int(input("Ingrese la cantidad de unidades a agregar: "))
        productStock[product] += quantity
        print(f"Nuevo stock de '{product}': {productStock[product]}")
else:
    print(f"El producto '{product}' no existe en el inventario.")
    
    addNew = input("¿Desea agregar este producto? (si/no): ").lower()
    if addNew == "si":
        quantity = int(input("Ingrese la cantidad inicial de unidades: "))
        productStock[product] = quantity
        print(f"Producto '{product}' agregado con {quantity} unidades.")

print("Inventario actualizado:")
print(productStock)

#----------------------------------------------------------------------------------
# Ejercicio 9
schedule = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio"
}

print("Agenda semanal:")
for key, event in schedule.items():
    print(f"{key[0].capitalize()} a las {key[1]} → {event}")

day = input("Ingrese el día a consultar: ").lower()
hour = input("Ingrese la hora a consultar (ejemplo 10:00): ")

key = (day, hour)

if key in schedule:
    print(f"El evento en {day} a las {hour} es: {schedule[key]}")
else:
    print(f"No hay actividades registradas el {day} a las {hour}.")

# #----------------------------------------------------------------------------------
# # Ejercicio 10
# countries = {
#     "Argentina": "Buenos Aires",
#     "Chile": "Santiago",
#     "Uruguay": "Montevideo",
#     "Paraguay": "Asuncion"
# }

# inverted = {}

# for country in countries:
#     capital = countries[country]
#     inverted[capital] = country

# print("Diccionario original:")
# print(countries)

# print("Diccionario invertido (capitales como claves):")
# print(inverted)

