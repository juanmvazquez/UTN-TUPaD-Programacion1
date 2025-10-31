# Ejercicio 1 \n para que cada dato se escriba en filas separadas
productos = [
    "Nombre,Precio,Cantidad\n",
    "Manzana,1200,50\n",
    "Banana,800,100\n",
    "Pera,950,75\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)

print("Archivo 'productos.txt' creado correctamente.")

# --------------------------------------------------------------------------
#Ejercicio 2
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas[1:]:
    partes = linea.strip().split(",")  
    nombre = partes[0]
    precio = partes[1]
    cantidad = partes[2]

    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# --------------------------------------------------------------------------
#Ejercicio 3
with open("productos.txt", "r") as file:
    for line in file:
        name, price, quantity = line.strip().split(",")
        print(f"Producto: {name} | Precio: ${price} | Cantidad: {quantity}")

name = input("Ingrese el nombre del nuevo producto: ")
price = input("Ingrese el precio: ")
quantity = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as file:
    file.write(f"{name},{price},{quantity}\n")

print("Producto agregado correctamente.")

productos = []

# --------------------------------------------------------------------------
#Ejercicio 4
with open("productos.txt", "r") as file:
    next(file)  # Salta la primera líneaf
    for line in file:
        name, price, quantity = line.strip().split(",")
        producto = {
            "nombre": name,
            "precio": float(price),
            "cantidad": float(quantity)
        }
        productos.append(producto)

for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# --------------------------------------------------------------------------
#Ejercicio 5
productos = []

with open("productos.txt", "r") as file:
    next(file)  # Salta la primera líneaf
    for line in file:
        name, price, quantity = line.strip().split(",")
        producto = {
            "nombre": name,
            "precio": float(price),
            "cantidad": int(quantity)
        }
        productos.append(producto)

buscar = input("Ingrese el nombre del producto que desea buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("El producto no existe.")

# --------------------------------------------------------------------------
#Ejercicio 6
productos = []

with open("productos.txt", "r") as file:
    next(file)  # Salta la primera líneaf
    for line in file:
        name, price, quantity = line.strip().split(",")
        producto = {
            "nombre": name,
            "precio": float(price),
            "cantidad": int(quantity)
        }
        productos.append(producto)

print("Productos actuales:")
for p in productos:
    print(f"- {p['nombre']} (${p['precio']}) Cantidad: {p['cantidad']}")

buscar = input("Ingrese el nombre del producto que desea modificar: ")

for p in productos:
    if p["nombre"].lower() == buscar.lower():
        nuevoPrecio = input("Ingrese el nuevo precio: ")
        nuevaCantidad = input("Ingrese la nueva cantidad: ")
        p["precio"] = float(nuevoPrecio)
        p["cantidad"] = int(nuevaCantidad)
        print("Producto actualizado.")
        break
else:
    print("El producto no existe.")

with open("productos.txt", "w") as file:
    for p in productos:
        file.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo actualizado correctamente.")
