
edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")



nota = int(input("Ingresa tu calificación (1 a 7): "))

if nota == 7:
    print("Excelente")
elif nota >= 6:
    print("Muy bien")
elif nota >= 5:
    print("Bien")
elif nota >= 4:
    print("Suficiente")
else:
    print("Insuficiente")



numero_entero = int(input("Ingresa un número entero: "))

if numero_entero >= 0:
    if numero_entero == 0:
        print("Es cero")
    else:
        print("Número positivo")
else:
    print("Número negativo")


numero_rango = int(input("Ingresa un número entre 1 y 100: "))

if numero_rango == 1 or numero_rango == 100:
    print("Estás en un límite permitido")
elif 1 < numero_rango < 100:
    print("Dentro del rango")
else:
    print("Fuera del rango")