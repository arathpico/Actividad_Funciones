# Programa para determinar si un número es primo

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Probar divisores impares hasta la raíz cuadrada
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Entrada de datos y validación
num = int(input("Ingrese un número: "))
if es_primo(num):
    print("Es primo")
else:
    print("No es primo")
