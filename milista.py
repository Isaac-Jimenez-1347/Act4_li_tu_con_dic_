# ejemplo de uso de lista
misnovias = ["Mayra", "Angelica", "Garces"]
misnumeros = [666, 69, 4]
print(misnovias)
# mostrando a sus novios
print(misnumeros )
# mostrando mis numeros
print("----accediendo a los elementos de la lista----")
print(misnovias [1])
if "Mayra" in misnovias:
    print("Si, 'Mayra' esta en la lista de sus novios") 
else:
    print("no tienes esa novia mi niño")
    
nnovias = len(misnovias)
print(f"numero de novias = {nnovias}")
posicion=0
for michavalilla in misnovias:
    print(posicion," ",michavalilla)
    posicion= posicion +1