
import random

def decimalABinario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

def decimalAOctal(numero):
    if numero == 0:
        return "0"
    
    octal = ""
    while numero > 0:
        resto = numero % 8
        octal = str(resto) + octal
        numero = numero // 8
    return octal

def decimalAHexadecimal(numero):
    if numero == 0:
        return "0"

    digitosHex = "0123456789ABCDEF"  
    hexadecimal = ""

    while numero > 0:
        resto = numero % 16
        hexadecimal = digitosHex[resto] + hexadecimal
        numero //= 16 

    return hexadecimal

print("*" * 82)
print("*" + " " * 80 + "*")
print("*" + "BIENVENIDOS AL JUEGO DE CONVERSIONES DE SISTEMAS NUMERICOS".center(80) + "*")
print("*" + " " * 80 + "*")
print("*" + "El programa eligira aleatoriamente una base: binaria, octal o hexadecimal.".center(80) + "*")
print("*" + "El objetivo es convertir el numero mostrado a la base indicada.".center(80) + "*")
print("*" + "Para salir del juego ingrese -> salir cuando lo pida".center(80) + "*")
print("*" + " " * 80 + "*")
print("*" * 82)


bases = ["binario", "octal", "hexadecimal"]
puntosTotales = 0
rondas = 0

while True:
    convertirA = random.choice(bases)  
    numero = random.randint(1,100) 
    puntos = 0

    if convertirA == "binario":
        print("-" * 38)
        print("----------------BINARIO---------------")
        print(f"{'El numero a convertir es : ' + str(numero):^38}")
        print("-" * 38)
        print("-" * 38)
        print("Opciones:")
        print("1 - Ingresar el numero convertido. (1 solo intento) 1 punto")
        print("2 - Pedir ayuda al programa 0,5 puntos")
        print("3 - Salir del juego")
        
        while True:
            opcion = input("Elegir opcion 1/2 (o 'salir' para terminar): ").lower()
            if opcion in ["1", "2"]:
                break  
            elif opcion == "salir":
                print("Juego terminado por el usuario.")
                break                
            else:
                print("Opcion invalida. Debes elegir 1, 2 o 'salir'.")
        puntos = 0

        if opcion == "1":
            respuesta = input("Ingresa el numero convertido a binario: ")
            if respuesta == decimalABinario(numero):
                puntos += 1
                print("CORRECTO! sumaste 1 punto")
            else: 
                print(f"Incorrecto. La respuesta era: {decimalABinario(numero)}")

        if opcion == "2":
            print("--------------------------------------")
            print("Te voy a mostrar los digitos del numero binario uno por uno")
            print("Podes intentar adivinar en cualquier momento ingresando el numero completo.")
            print("--------------------------------------")
            
            temporal = numero
            digitos = []

            while temporal > 0:
                digito = temporal % 2
                digitos.insert(0, str(digito))
                temporal //=2        

                respuesta = input(f"AYUDA: {digitos} : ")
                print("Presiona ENTER para ver el siguiente digito, o escribe el numero completo para adivinar: ")        

                if respuesta != "":
                    if respuesta == decimalABinario(numero):
                        puntos += 0.5
                        print("CORRECTO NUMERO BINARIO ADIVINADO (+0,5 puntos)")                    
                        break
                    else:
                        print("INCORRECTO. Seguimos con las pistas")

            if respuesta == "":  
                print(f"La conversion a numero binario es: {decimalABinario(numero)}")
                print("No lograste adivinar aunque tuviste ayuda. 0 puntos")

        print("--------------------------------------")
        print(f"PUNTAJE FINAL: {puntos}")
        print("--------------------------------------")

    elif convertirA == "octal":
        print("--------------------------------------")
        print("-----------------OCTAL----------------")
        print(f"{'El numero a convertir es : ' + str(numero):^38}")
        print("--------------------------------------")
        print("--------------------------------------")
        print("Opciones:")
        print("1 - Ingresar el numero convertido. (1 solo intento) 1 punto")
        print("2 - Pedir ayuda al programa 0,5 puntos")      

        while True:
            opcion = input("Elegir opcion 1/2 (o 'salir' para terminar): ").lower()
            if opcion in ["1", "2"]:
                break  
            elif opcion == "salir":
                print("Juego terminado por el usuario.")
                break                
            else:
                print("Opcion invalida. Debes elegir 1, 2 o 'salir'.")
        puntos = 0

        if opcion == "1":
            respuesta = input("Ingresa el numero convertido a octal: ")
            if respuesta == decimalAOctal(numero):
                puntos += 1
                print("CORRECTO! sumaste 1 punto")
            else: 
                print(f"Incorrecto. La respuesta era: {decimalAOctal(numero)}")    

        if opcion == "2":
            print("--------------------------------------")
            print("Te voy a mostrar los digitos del numero octal uno por uno")
            print("Podes intentar adivinar en cualquier momento ingresando el numero completo.")
            print("--------------------------------------")      

            temporal = numero
            digitos = [] 

            while temporal > 0:
                digito = temporal % 8
                digitos.insert(0, str(digito))
                temporal //= 8       

                respuesta = input(f"AYUDA: {digitos} : ")  
                print("Presiona ENTER para ver el siguiente digito, o escribe el numero completo para adivinar: ")   

                if respuesta != "":
                    if respuesta == decimalAOctal(numero):
                        puntos += 0.5
                        print("CORRECTO NUMERO OCTAL ADIVINADO (+0,5 puntos)")                    
                        break
                    else:
                        print("INCORRECTO. Seguimos con las pistas")

            if respuesta == "":  
                print(f"La conversion a numero octal es: {decimalAOctal(numero)}")
                print("No lograste adivinar aunque tuviste ayuda. 0 puntos")

        print("--------------------------------------")
        print(f"PUNTAJE FINAL: {puntos}")
        print("--------------------------------------")
        

    elif convertirA == "hexadecimal":
        print("--------------------------------------")
        print("--------------HEXADECIMAL-------------")
        print(f"{'El numero a convertir es : ' + str(numero):^38}")
        print("--------------------------------------")
        print("--------------------------------------")
        print("Opciones:")
        print("1 - Ingresar el numero convertido. (1 solo intento) 1 punto")
        print("2 - Pedir ayuda al programa 0,5 puntos")

        while True:
            opcion = input("Elegir opcion 1/2 (o 'salir' para terminar): ").lower()
            if opcion in ["1", "2"]:
                break  
            elif opcion == "salir":
                print("Juego terminado por el usuario.")
                break                
            else:
                print("Opcion invalida. Debes elegir 1, 2 o 'salir'.")
        
        puntos = 0

        if opcion == "1":
            respuesta = input("Ingresa el numero convertido a hexadecimal: ").upper()
            if respuesta.upper() == decimalAHexadecimal(numero):
                puntos += 1
                print("CORRECTO! sumaste 1 punto")
            else: 
                print(f"Incorrecto. La respuesta era: {decimalAHexadecimal(numero)}")

        if opcion == "2":
            print("--------------------------------------")
            print("Te voy a mostrar los digitos del numero hexadecimal uno por uno")
            print("Podes intentar adivinar en cualquier momento ingresando el numero completo.")
            print("--------------------------------------")
            
            temporal = numero
            digitos = []
            digitosHex = "0123456789ABCDEF"

            while temporal > 0:
                digito = temporal % 16
                digitos.insert(0, digitosHex[digito])
                temporal //= 16       

                respuesta = input(f"AYUDA: {digitos} : ")
                print("Presiona ENTER para ver el siguiente digito, o escribi el numero completo para adivinar: ")        

                if respuesta != "":
                    if respuesta.upper() == decimalAHexadecimal(numero):
                        puntos += 0.5
                        print("CORRECTO NUMERO HEXADECIMAL ADIVINADO (+0,5 puntos)")                    
                        break
                    else:
                        print("INCORRECTO. Seguimos con las pistas")

            if respuesta == "":  
                print(f"La conversion a numero hexadecimal es: {decimalAHexadecimal(numero)}")
                print("No lograste adivinar aunque tuviste ayuda. 0 puntos")

        print("--------------------------------------")
        print(f"PUNTAJE FINAL: {puntos}")
        print("--------------------------------------")    

    puntosTotales += puntos
    rondas += 1

    print("--------------------------------------")
    print(f"PUNTAJE TOTAL ACUMULADO: {puntosTotales}")
    print("--------------------------------------")

    salir = input("Desea salir del juego? (escriba 'salir' para terminar, ENTER para seguir): ")
    if salir.lower() == "salir":
        print("Juego terminado.")
        print(f"Jugaste {rondas} rondas y obtuviste {puntosTotales} puntos.")
        break
    