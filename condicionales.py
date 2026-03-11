# --- Bloque 1: Verificación de mayoría de edad ---
# Solicitamos un número y lo convertimos a entero (int)
edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# --- Bloque 2: Evaluación de calificaciones con elif ---
# Usamos float por si la calificación tiene decimales (ej: 5.5)
nota = float(input("Ingresa tu calificación (1 a 7): "))

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


# --- Bloque 3: Condiciones anidadas (Número positivo, cero o negativo) ---
# Un if dentro de otro para separar primero los no-negativos
numero_entero = int(input("Ingresa un número entero: "))

if numero_entero >= 0:
    if numero_entero == 0:
        print("Es cero")
    else:
        print("Número positivo")
else:
    print("Número negativo")


# --- Bloque 4: Condición de borde (Rango 1 a 100) ---
# Verificamos límites exactos y pertenencia al rango
numero_rango = int(input("Ingresa un número entre 1 y 100: "))

if numero_rango == 1 or numero_rango == 100:
    print("Estás en un límite permitido")
elif 1 < numero_rango < 100:
    print("Dentro del rango")
else:
    print("Fuera del rango")