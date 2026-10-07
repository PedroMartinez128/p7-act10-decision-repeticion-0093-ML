#Pedro Martinez 0093
print("--- 1. CONDICIONALES 'IF' (python_conditions) ---")

edad = 20
if edad >= 18:
    print("Ejemplo 1: Es mayor de edad y puede ingresar al recinto.")

stock = 0
if stock == 0:
    print("Ejemplo 2: Alerta, el producto está agotado.\n")


print("--- 2. CONDICIONALES CON 'ELIF' (python_if_elif) ---")

nota = 85
if nota >= 90:
    print("Ejemplo 1: Excelente (A)")
elif nota >= 80:
    print("Ejemplo 1: Buen trabajo (B)")

hora = 14
if hora < 12:
    print("Ejemplo 2: Buenos días")
elif hora < 19:
    print("Ejemplo 2: Buenas tardes\n")


print("--- 3. ESTRUCTURA COMPLETA 'IF / ELIF / ELSE' (python_if_else) ---")

temperatura = 12
if temperatura > 28:
    print("Ejemplo 1: Hace mucho calor.")
elif temperatura >= 15:
    print("Ejemplo 1: El clima está agradable.")
else:
    print("Ejemplo 1: Hace frío, abrígate.")

saldo = 50
precio_producto = 100
if saldo >= precio_producto:
    print("Ejemplo 2: Compra aprobada.")
else:
    print("Ejemplo 2: Saldo insuficiente para realizar la compra.\n")


print("--- 4. BUCLES 'FOR' (python_for_loops) ---")

frutas = ["Manzana", "Plátano", "Cereza"]
print("Ejemplo 1: Lista de compras:")
for fruta in frutas:
    print(f" - {fruta}")

numero = 5
print(f"Ejemplo 2: Tabla del {numero}:")
for i in range(1, 4):
    print(f" {numero} x {i} = {numero * i}\n")


print("--- 5. BUCLES 'WHILE' (python_while_loops) ---")

contador = 1
print("Ejemplo 1: Conteo del 1 al 3:")
while contador <= 3:
    print(f" Contador: {contador}")
    contador += 1

progreso = 0
print("Ejemplo 2: Proceso de descarga:")
while progreso < 100:
    progreso += 35
    if progreso > 100:
        progreso = 100
    print(f" Descargando... {progreso}%")

print("\n--- ¡Ejecución finalizada con éxito! ---")
print("===Pedro Martinez 0093===")