import math

def calcola_area_cerchio(raggio):
    area = math.pi * (raggio ** 2)
    return f"L'area di un cerchio con raggio {raggio} è {area:.2f}."

raggio = 5
output = calcola_area_cerchio(raggio)
print(output)
