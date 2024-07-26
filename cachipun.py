import math
import random
"""# Actividad 2 - Cachipún
El Cachipún, conocido también como chin chan pu, pikachú, jankenpón, yan ken po, pin pon
papas, hakembó o how-are-you-speak, es un juego de manos en el que existen tres
elementos: la piedra que vence a la tijera rompiéndola, la tijera que vence al papel cortándolo
y el papel que vence a la piedra envolviéndola, dando lugar a un círculo o ciclo cerrado. Se
utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se
hace a veces usando una moneda, o para dirimir algún asunto.
Para poner en práctica lo que hemos aprendido a lo largo de la unidad, se implementará un
programa en Python que permite jugar al cachipún en contra del computador.
"""



# Lista de opciones válidas
opciones = ['piedra', 'papel', 'tijera']

# Solicitar al usuario que ingrese su elección
usuario = input("Elige piedra, papel o tijera: ").lower()

# Validación de la elección del usuario
while usuario not in opciones:
    print("Elección inválida. Las opciones válidas son: piedra, papel o tijera.")
    usuario = input("Elige piedra, papel o tijera: ").lower()

# Elección del computador
computador = random.choice(opciones)

# Mostrar elecciones
print(f"Tu jugaste: {usuario.capitalize()}")
print(f"Computador jugó: {computador.capitalize()}")

# Determinar el ganador
if usuario == computador:
    resultado = "Empate"
elif (usuario == 'piedra' and computador == 'tijera') or \
     (usuario == 'tijera' and computador == 'papel') or \
     (usuario == 'papel' and computador == 'piedra'):
    resultado = "¡Ganaste!"
else:
    resultado = "Perdiste"

# Mostrar el resultado
print(resultado +"!!")