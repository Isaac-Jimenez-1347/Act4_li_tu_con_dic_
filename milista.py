# ejemplo de uso de listas
misnovios=["Alexis", "Fernando", "Mendoza"]
misnumeros=[656,269,5250]
#Mostrando mis novios
print(misnovios)
#Mostrando mis numeros
print(misnumeros)
print("---accediendo a los elementos de la lista---")
print(misnovios[-2])
if "moreno" in misnovios:
    print("si, moreno esta en la lista de mis novios")
else:
    print("chale no eres mi novio")
print("numero de novios")
Nnovios=len(misnovios)
print(f"numero de novios {Nnovios}")
print("ciclo de for en listas")
posicion = 0
for medianaranja in misnovios:
    print(posicion, " ", medianaranja)
    posicion=posicion+1

