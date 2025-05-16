# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código


# 1. Solicita cuántas notas ingresará el usuario.
while True:
    try:
        cantidad_notas = int(input("¿Cuántas notas deseas ingresar? "))
        if cantidad_notas <= 0:
            print("Por favor, ingresa un número mayor que 0.")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
notas = []
for i in range(cantidad_notas):
    while True:
        try:
            nota = float(input(f"Ingrese la nota #{i+1} (entre 1.0 y 7.0): "))
            if 1.0 <= nota <= 7.0:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número decimal.")

# 3. Calcula el promedio con dos decimales.
promedio = round(sum(notas) / cantidad_notas, 2)

# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
print(f"\nPromedio: {promedio:.2f}")
if promedio >= 4.0:
    print("¡Aprobaste! 🎉")
else:
    print("No aprobaste. 💡 Esfuérzate un poco más.")

# 5. Validación de rango ya incluida en el punto 2.