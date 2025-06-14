import random

array = [random.randint(1, 100) for _ in range(10)]
mayor = max(array)
menor = min(array)
print(f"El array es: {array}")
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")