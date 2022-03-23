import random

numero = random.randint(5, 10)
print(f"Número: {numero}")

horas = 0
minutos = 1

while numero != horas:
    minutos = minutos + 1
    if minutos > 60:
        print("passou")
        minutos = 0
        horas = horas + 1
    if horas == numero:
        print(f"Passaram {horas} horas")




