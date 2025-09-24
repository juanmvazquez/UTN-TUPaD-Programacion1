print("----------Bienvenido a la biblioteca escolar----------")
print("------------------------------------------------------")

titles = ["Batman"]
# copies = [0] * len(titles) # se crea una lista vacia por cada titulo agregado.
copies = [1]

while True:
    print("#" * 50)
    print("#" + " " * 48 + "#")
    print("#" + "-------------------MENU-------------------".center(48) + "#")
    print("#" + " " * 48 + "#")
    print("#" + "1- Ingresar título de libros".center(48) + "#")
    print("#" + "2- Ingresar ejemplares del libro".center(48) + "#")
    print("#" + "3- Mostrar catálogo".center(48) + "#")
    print("#" + "4- Consultar disponibilidad".center(48) + "#")
    print("#" + "5- Listar agotados".center(48) + "#")
    print("#" + "6- Agregar título".center(48) + "#")
    print("#" + "7- Actualizar ejemplares (préstamo/devolución)".center(48) + "#")
    print("#" + "8- Salir".center(48) + "#")
    print("#" + " " * 48 + "#")
    print("#" * 50)

    option = input("Ingrese la opcion que desee: ")

    if option not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Numero incorrecto - Ingrese unicamente los numeros mostrados en el menu")
        continue

    if option == "1":
        print("------------------------Ingresar titulos--------------------------")

        while True:

            newTitle = input("Ingrese un nuevo libro: ").title()

            while newTitle in titles or newTitle == "":            
                print("El titulo ya existe ingrese otro titulo")
                newTitle = input("Ingrese nuevo titulo: ").title()
            
            titles.append(newTitle)
            copies.append(0)

            print(f"Libro agregado: {newTitle}")

            print("====================CATALOGO COMPLETO====================")
            for i in range(len(titles)):
                print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")

            newOptions = input ("Desea agregar otro libro? s/n: ")

            if newOptions == "n".lower():
                print("------------------------Volviendo al menu principal------------------------")
                print("###########################################################################")
                break 

    if option == "2":
        print("------------------------Ingresar ejemplares--------------------------")

        if len(titles) == 0:
            print("No hay libros cargados. Primero debe agregar libros antes de ingresar ejemplares.")
            continue
        else:
            while True:
                print("A que libro deseas agregarle un ejemplar?")

                for i in range(len(titles)):
                    print(f"{i+1} : {titles[i]}")
                
                numberTitle = 0
                while numberTitle < 1 or numberTitle > len(titles):
                    userInput  = input("seleccione el numero de titulo al que desea agregar ejemplares : ")

                    if userInput.isdigit():
                        numberTitle = int(userInput)
                        if numberTitle < 1 or numberTitle > len(titles):
                            print(f"{numberTitle} no existe dentro de la lista, por favor reintente con los numeros listados.")         
                    else:
                        print("Debe ingresar un numero valido, intente nuevamente.")

                print(f"Seleccionaste: {titles[numberTitle - 1]}")

                stock = 0
                while stock < 1:
                    userInput = input(f"Ingrese la cantidad de ejemplares que contiene el libro {titles[numberTitle - 1]} : ")

                    if userInput.isdigit():
                        stock = int(userInput)
                        if stock < 1:
                            print(f"El numero ingresado no puede ser 0 ni menor a 0 porque {titles[numberTitle - 1]} contiene {copies[numberTitle - 1]} ejemplares.")
                            print("Reintentelo nuevamente.")
                    else:
                        print("La opcion 2 es unicamente para agregar ejemplares, si quiere eliminar ingrese la opcion 7 intente nuevamente")

                
                copies[numberTitle - 1] = copies[numberTitle -1] + stock

                print("====================CATALOGO COMPLETO====================")
                for i in range(len(titles)):
                    print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")

                newOptions = input ("Desea agregar mas ejemplares? s/n: ")
                if newOptions == "n".lower():
                    print("------------------------Volviendo al menu principal------------------------")
                    print("###########################################################################")
                    break
                else:
                    print("-----------------------Vuelva a seleccionar el libro.-------------------------")

    if option == "3":
        print("------------------------CATALOGO COMPLETO--------------------------") 

        while True:
            for i in range(len(titles)):
                print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")  

            input ("Presione enter para continuar... ")            
            print("------------------------Volviendo al menu principal------------------------")
            print("###########################################################################")
            break

    if option == "4":
        print("------------------------Consultar disponibilidad--------------------------")

        while True:
            findBook = input("Ingrese el titulo del libro que desee buscar: ").title()

            if findBook in titles:
                index = titles.index(findBook)
                print(f"{findBook} cantidad de ejemplares: {copies[index]}")
            else:
                print(f"{findBook} no existe en la lista.")

            newOptions = input ("Desea buscar otro libro? s/n: ")
            if newOptions == "n":
                print("------------------------Volviendo al menu principal------------------------")
                print("###########################################################################")
                break

    if option == "5":
        print("------------------------Libros con 0 ejemplares--------------------------")

        while True:
            stock = False

            for i in range(len(titles)):
                if copies[i] == 0:                
                    print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")
                    stock = True
            
            if not stock:
                print("No hay libros sin ejemplares")

            input ("Presione enter para continuar... ")   
            print("------------------------Volviendo al menu principal------------------------")
            print("###########################################################################")
            break

    if option == "6":
        print("------------------------Ingresar nuevo titulos con ejemplares--------------------------")

        while True:
            newTitle = input("Ingrese un nuevo libro: ").title()

            while newTitle in titles or newTitle == "":            
                print("El titulo ya existe ingrese otro titulo")
                newTitle = input("Ingrese nuevo titulo: ").title()
            
            titles.append(newTitle)
            print(f"Libro agregado: {newTitle}")

            while True:
                userInput = input("Ingrese la cantidad de ejemplares que ingresaron del libro: ")
                
                if userInput.isdigit():  
                    copy = int(userInput)
                    if copy < 0:
                        print("La cantidad de ejemplares no puede ser negativa. Vuelva a agregar una cantidad de ejemplares.")
                    else:
                        break
                else:
                    print("Debe ingresar un numero (positivo) valido, no letras ni simbolos.")
            
            copies.append(copy)

            print("====================CATALOGO COMPLETO====================")
            for i in range(len(titles)):
                print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")

            newOptions = input ("Desea agregar otro libro? s/n: ")

            if newOptions == "n".lower():
                print("------------------------Volviendo al menu principal------------------------")
                print("====================CATALOGO ACTUALIZADO====================")
                for i in range(len(titles)):
                    print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")
                print("###########################################################################")
                break
    if option == "7":          
        print("------------------------Actualizacion de stock------------------------")

        if len(titles) == 0:
            print("No hay libros cargados. Primero debe agregar libros antes de ingresar ejemplares.")
            continue
        else:
            while True:  
                print("A que libro deseas modificarle el stock?")

                for i in range(len(titles)):
                    print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")
                    
                numberTitle = 0
                while numberTitle < 1 or numberTitle > len(titles):
                    userInput  = input("seleccione el numero de titulo al que desea modificar el stock : ")

                    if userInput.isdigit():
                        numberTitle = int(userInput)
                        if numberTitle < 1 or numberTitle > len(titles):
                            print(f"{numberTitle} no existe dentro de la lista, por favor reintente con los numeros listados.")         
                    else:
                        print("Debe ingresar un numero valido, no letras ni simbolos.")

                index = numberTitle - 1
                print(f"Seleccionaste: {titles[numberTitle - 1]} que contiene : {copies[index] } ejemplares ")  

               
                userInput = input("Ingrese el stock a modificar (negativo para restar - postivo para sumar) : ")

                if userInput.lstrip("-").isdigit():
                    stock = int(userInput)   
                    new_stock = copies[index] + stock

                    if new_stock < 0:            
                        copies[index] = 0
                        print(f"Intento eliminar mas ejemplares de los que habia, el stock del libro {titles[index]} queda en {copies[index]} ")
                    elif stock < 0 and new_stock >= 0:
                        copies[index] = new_stock
                        print(f"Se eliminaron {-stock} ejemplares a {titles[index]} el total es de : {copies[index]} ejemplares ")
                    elif stock > 0 and new_stock >= 0:
                        copies[index] = new_stock
                        print(f"Se agregaron {stock} ejemplares a {titles[index]} el total es de : {copies[index]} ejemplares ")

                    newOptions = input ("Desea agregar continuar modificando stocks? s/n: ")
                else:
                    print("Debe ingresar un numero valido, no letras ni simbolos.")
                    continue
                                            
                if newOptions == "n".lower():
                    print("------------------------Volviendo al menu principal------------------------")
                    print("====================CATALOGO ACTUALIZADO====================")

                    for i in range(len(titles)):
                       print(f"{i+1} : {titles[i]} - Ejemplares {copies[i]}")

                    print("###########################################################################")
                    break

    if option == "8":
        print("Muchas gracias por usar la app! ")
        print("###########################################################################")
        break

                
            



