arcoiris = ("azul","verde","rojo","amarillo")
print(arcoiris)
print("--longitud arcoiris--")
print(len(arcoiris))
animales = ("pantera",20, "estatura",1.7)
print(animales)
print("elementos de la tupla")
print(animales[0])

ratero = (" el men", "edgar", "cesar viejon")
y = list(ratero)
y[1] = "kiwi"
ratero= tuple(y)

print(ratero)
print("agregando elementos")

animal=("polly","kiara")
y=list(animal)
y.append("choco")
otratupla= tuple(y)
print(otratupla)
print("uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)