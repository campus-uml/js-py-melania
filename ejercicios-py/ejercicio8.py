import random

array = [random.randint(1, 100) for _ in range(10)]
suma = sum(array)
print(f"El array es: {array}")
print(f"La suma de los elementos es: {suma}")