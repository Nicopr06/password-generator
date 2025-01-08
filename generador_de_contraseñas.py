import random
import string

password = ""
letras = list(string.ascii_letters)
digitos = list(string.digits)
simbolos = list(string.punctuation)

print("Bienvenido a su generador de contraseñas aleatorio")

num_letras = int(input("\n¿Cuántas letras quieres?: "))
for let in range(num_letras):
    password += random.choice(letras)

num_digitos = int(input("¿Cuántos dígitos quieres?: "))
for dig in range(num_digitos):
    password += random.choice(digitos)

num_simbolos = int(input("¿Cuántos símbolos quieres?: "))
for sim in range(num_simbolos):
    password += random.choice(simbolos)

print(f"Su contraseña es: {password}")
