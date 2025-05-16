# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código

# 2. Crea una función llamada es_palindromo(texto)
def es_palindromo(texto):
    # Convierte el texto a minúsculas y elimina los espacios
    texto_limpio = texto.lower().replace(" ", "")
    # Compara el texto con su reverso
    return texto_limpio == texto_limpio[::-1]

# 1. Solicita al usuario una palabra o frase
frase = input("Ingresa una palabra o frase: ")

# 3. Muestra si es o no un palíndromo con un mensaje claro
if es_palindromo(frase):
    print("✅ Es un palíndromo.")
else:
    print("❌ No es un palíndromo.")