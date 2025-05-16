# 📝 ejercicio1.py
# ✖️ Tabla de multiplicar con función y bucle for
# Puntaje: 7 puntos

# Instrucciones:
# 1. Crea una función llamada mostrar_tabla(n)
# 2. Esta función debe imprimir la tabla de multiplicar del número n desde 1 hasta 10
# 3. Utiliza un bucle para generar e imprimir los resultados
# 4. Luego, solicita al usuario un número y llama a la función con ese valor

# 👇 Aquí comienza tu código

# 1. Crea una función llamada mostrar_tabla(n)
def mostrar_tabla(n):
    # 2. Imprime la tabla de multiplicar del número n desde 1 hasta 10
    print(f"\nTabla de multiplicar del {n}")
    # 3. Utiliza un bucle para generar e imprimir los resultados
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

# 4. Solicita al usuario un número y llama a la función con ese valor
while True:
    try:
        numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
        break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

mostrar_tabla(numero)