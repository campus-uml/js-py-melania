import random

palabras = [
    "Aceituna", "Murciélago", "Educación", "Aeropuerto", 
    "Otorrinolaringólogo", "Euforia", "Aceite", 
    "Paleontólogo", "Arquitectura", "Hipopótamo"
]

palabra = random.choice(palabras)
vocales = "AEIOUaeiou"
contador = [letra for letra in palabra if letra in vocales]
print(f"La palabra '{palabra}' tiene las vocales: {contador} ({len(contador)} vocales).")