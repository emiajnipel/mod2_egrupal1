import paquete_cientifico
a=9
b=10

# dimensiones cilindro
radio_cilindro = 10
altura_cilindro = 5

# calculo de area base cilindro
area_base = paquete_cientifico.PI * radio_cilindro * radio_cilindro

#c alculo de volumen cilindro
volumen_cilindro = paquete_cientifico.vol_cilindro(altura_cilindro, area_base)
print("Volumen Cilindro:")
print(volumen_cilindro)

# multiplicación de a y b
multiplicacion = paquete_cientifico.multiplica(a,b)
print("la multiplicación es:")
print(multiplicacion)
