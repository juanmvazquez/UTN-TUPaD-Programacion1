import csv
import os

CSVNAME = "parcial.csv"

def getCatalog():
    catalog = []
    if not os.path.exists(CSVNAME):
        with open(CSVNAME, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["titulo","cantidad"])
            escritor.writeheader()
        return catalog

    with open(CSVNAME, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            catalog.append({"titulo": fila["titulo"], "cantidad": int(fila["cantidad"])})
    return catalog

def saveCatalog(catalog):
    with open(CSVNAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["titulo", "cantidad"])
        writer.writeheader()
        writer.writerows(catalog)

def getIntInput(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Error: debe ingresar un numero entero.")

def getNonEmptyTitle():
    title = input("Ingrese el titulo del libro: ").strip()

    while title == "":
        print("El titulo no puede estar vacio.")
        title = input("Ingrese el titulo del libro: ").strip()

    return title

def titleExists(title):
    catalog = getCatalog()

    for book in catalog:
        if book["titulo"].strip().lower() == title.strip().lower():
            return True

    return False

def addBook(book):
    # Escribir header solo si el archivo no existe o esta vacio
    writeHeader = not os.path.exists(CSVNAME) or os.path.getsize(CSVNAME) == 0
    with open(CSVNAME, "a", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["titulo", "cantidad"])
        if writeHeader:
            writer.writeheader()
        writer.writerow(book)

def normalizeTitle(s: str) -> str:    
    return " ".join(s.split()).lower()

def findBookIndex(catalog: list, title: str):
    wanted = normalizeTitle(title)
    for i, book in enumerate(catalog):
        if normalizeTitle(book["titulo"]) == wanted:
            return i
    return None

def addMultipleTitles():
    while True:
        addTitle()
        if not askYesNo("¿Desea agregar otro titulo?"):
            print("Carga de titulos finalizada.")
            break

def addTitle():
    while True:
        title = getNonEmptyTitle()

        if titleExists(title):
            print("El titulo ingresado ya existe. Ingrese otro.")
        else:
            break

    copies = getIntInput("Ingrese la cantidad de ejemplares: ")
    while copies < 0:
        print("Error: la cantidad no puede ser negativa.")
        copies = getIntInput("Ingrese la cantidad de ejemplares: ")

    addBook({"titulo": title, "cantidad": copies})
    print("El titulo fue agregado correctamente.")

def addCopies():
    title = getNonEmptyTitle()
    catalog = getCatalog()
    idx = findBookIndex(catalog, title)
    if idx is None:
        print("No se encontro un libro con ese titulo.")
        return

    book = catalog[idx]
    print(f"Libro encontrado: {book['titulo']} (Cantidad actual: {book['cantidad']})")

    extra = getIntInput("Ingrese la cantidad a agregar (>= 0): ")
    while extra <= 0:
        print("Error: la cantidad no puede ser negativa ni 0.")
        extra = getIntInput("Ingrese la cantidad a agregar (>= 0): ")

    book["cantidad"] += extra
    print(f"Nueva cantidad : {book['cantidad']} ejemplares")

    saveCatalog(catalog)
    print("Catalogo actualizado correctamente.")

def showCatalog():
    catalog = getCatalog()

    print(f"{'TITULO':<35} {'CANTIDAD':>10}")
    print("-" * 47)
    for book in catalog:
        print(f"{book['titulo'].strip():<35} {book['cantidad']:>10}")
        
def checkAvailability():
    catalog = getCatalog()

    if not catalog:
        print("El catalogo esta vacio. Primero agregue libros, por favor.")
        return

    title = getNonEmptyTitle()

    idx = findBookIndex(catalog, title)
    if idx is None:
        print("El titulo no existe en el catalogo.")
        return

    book = catalog[idx]
    if book["cantidad"] > 0:
        print(f"El libro '{book['titulo']}' tiene {book['cantidad']} ejemplares disponibles.")
    else:
        print(f"El libro '{book['titulo']}' no tiene ejemplares disponibles.")

def listOutOfStock():
    catalog = getCatalog()

    if not catalog:
        print("El catalogo esta vacio.")
        return

    found = False
    for book in catalog:
        if book["cantidad"] == 0:
            print(f"Titulo {book['titulo']} agotado")
            found = True

    if not found:
        print("No hay libros agotados.")

def processAction(book, action):
    if action == "p":
        if book["cantidad"] > 0:
            book["cantidad"] -= 1
            print(f"Prestamo registrado. Nueva cantidad: {book['cantidad']}")
            if book["cantidad"] == 0:
                print("El libro quedo agotado.")
            return True
        else:
            print("No hay ejemplares disponibles para prestar.")
            return False  
    else:  
        book["cantidad"] += 1
        print(f"Devolución registrada. Nueva cantidad: {book['cantidad']}")
        return True

def updateCopies():
    catalog = getCatalog()
    if not catalog:
        print("El catalogo esta vacio. No hay libros para actualizar.")
        return
    
    title = getNonEmptyTitle()
    idx = findBookIndex(catalog, title)
    if idx is None:
        print("El titulo no existe en el catalogo.")
        return

    book = catalog[idx]
    print(f"Libro encontrado: {book['titulo']} (Cantidad actual: {book['cantidad']})")

    action = input("¿Registrar prestamo o devolucion? (p/d): ").strip().lower()
    while action not in ("p", "d"):
        print("Error: ingrese 'p' (prestamo) o 'd' (devolucion).")
        action = input("¿Registrar préstamo o devolución? (p/d): ").strip().lower()

    if processAction(book, action):
        saveCatalog(catalog)
        print("Catalogo actualizado correctamente.")

def askYesNo(question: str) -> bool:
    resp = input(f"{question} (s/n): ").strip().lower()
    while resp not in ("s", "n"):
        print("Error: debe ingresar 's' para si o 'n' para no.")
        resp = input(f"{question} (s/n): ").strip().lower()
    return resp == "s"

def mainMenu():
    while True:
        print("#" * 50)
        print("#                 MENU PRINCIPAL                 #")
        print("#" * 50)
        print("# 1. Ingresar titulos (multiples)                #")
        print("# 2. Ingresar ejemplares                         #")
        print("# 3. Mostrar catalogo                            #")
        print("# 4. Consultar disponibilidad                    #")
        print("# 5. Listar agotados                             #")
        print("# 6. Agregar titulo                              #")
        print("# 7. Actualizar ejemplares (prestamo/devolucion) #")
        print("# 8. Salir                                       #")
        print("#" * 50)
        option = input("Ingrese opcion: ").strip()

        match option:
            case "1":         
                print("----------Ingresar titulos (multiples)----------")       
                addMultipleTitles()
            case "2":
                print("----------Ingresar ejemplares----------")
                addCopies()
            case "3":
                print("--------------Mostrar catalogo-----------------")
                showCatalog()
            case "4":
                print("----------Consultar disponibilidad----------")
                checkAvailability()
            case "5":
                print("----------Listar libros agotados----------")
                listOutOfStock()
            case "6":
                print("----------Agregar titulo nuevo----------")
                addTitle()
            case "7":
                print("----------Actualizar ejemplares (prestamo/devolucion)----------")
                updateCopies()
            case "8":
                if askYesNo("Esta seguro que desea salir del programa?"):
                    print("----------Muchas gracias por usar el programa----------")
                    break
            case _:   
                print("----------Opcion invalida. Intente nuevamente----------")

mainMenu()

