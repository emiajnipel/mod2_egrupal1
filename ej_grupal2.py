import paquete_cientifico
a=9
b=10

# área de un rectangulo, dados sus lados
cara_1 = 4
cara_2 = 8

area_rectangular = paquete_cientifico.area_rect(cara_1, cara_2)
print("el área del rectangulo es")
print(area_rectangular)

# perímetro de un rectangulo, dados sus lados

perimetro_rectangular = paquete_cientifico.perim_rect(cara_1, cara_2)
print("el perimetro es")
print(perimetro_rectangular)

# distancia recorrida tiempo*velocidad
velocidad = 5
tiempo = 60

distancia = paquete_cientifico.distancia_rec(velocidad, tiempo)
print("la distancia recorrida es")
print(distancia)