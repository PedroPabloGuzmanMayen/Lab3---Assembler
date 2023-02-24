import numpy as np
import FunLab3 as fn
print("Bienvenido, en este programa podrás escribir números binarios de 8 bits y convertirlos a complemento A y complemento A2, también podrás ")
print()
condition = True 

while condition: 
    print("Opción 1: Ingresar un número binario y obtener el complemento A y el complemento A2")
    print()
    print("Opción 2: Ingresar un número hexadecimal y obtenerlo en decimal")
    print()
    print("Opción 3: Ingresar un número decimal y obtener el hexadecimal")
    print()
    print("Opción 4:Salir del programa")
    print()

    option = int(input("Ingresa la opción que quieras: "))
    while (option > 4 or option < 1):
       option = int(input("Valor no valido, intenta de nuevo: "))
    
    if (option == 1):
        binary = input("Ingresa el binario (solo 8 bits): ")
        while (len(binary) > 8 or len(binary) <8):
            binary = input("ERROR: ingresa otro valor: ")
        print("Complemento A: " + fn.complementoA(binary))
        print("Complemento A2: " + fn.complementoA2(binary))
        print()
    
    if (option == 2):
        hex = input("Ingresa el valor hexadecimal (solo 3 digitos): ")
        while (len(hex) > 3 or len(hex) < 3):
            hex = input("Error, intenta con otro valor: ")
        print(hex + " en decimal es: " + fn.hexToDec(hex))
        print()
    if (option == 3):
        dec = input("Ingresa el valor decimal (este debe poder representarse con 3 digitos, ingresa valor mayores a 256 y menores a 4096): ")
        while (int(dec) > 4095 or int(dec) < 256):
            dec = input("Error no valido, intenta con un valor nuevo: ")
        print(dec + " en hexadecimal es:  " + fn.decToHex(dec))
        print()
    if (option == 4):
        print("Gracias por usar el programa")
        condition = False



