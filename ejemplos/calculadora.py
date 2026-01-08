#calculadora basica

#pedir al usuario que ingrese una operacion(suma. resta multiplicacion division) y luego pedirle los dos numeros
#ejecutar la operacion y mostrar el resultado
#debe ejecutarse hasta que el usuario escriba salir como operacion

while True:
    operacion = input("Ingrese una operacion (suma, resta, multiplicacion, division) o 'salir' para salir: ")
    if operacion == "salir":
        break
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    if operacion == "suma":
        resultado = numero1 + numero2
    elif operacion == "resta":
        resultado = numero1 - numero2
    elif operacion == "multiplicacion":
        resultado = numero1 * numero2
    elif operacion == "division":
        resultado = numero1 / numero2
    else:
        print("Operacion no valida")
        continue
    print(f"El resultado de la operacion es: {resultado}")