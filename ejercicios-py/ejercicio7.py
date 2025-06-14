import random

palabras = ["hola", "mundo", "python", "programación", "GitHub"]
palabra = random.choice(palabras)
invertida = palabra[::-1]
print(f"La palabra '{palabra}' invertida es '{invertida}'.")