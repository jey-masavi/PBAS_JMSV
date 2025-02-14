#Problema 9
#Descripción: Este programa  genera una lista de números pares e impares hasta un límite dado.

def generar_lista(limite):
    pares = []
    impares = []

    for num in range(limite + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares

limite = int(input("Introduzca el limite: "))
pares, impares = generar_lista(limite)

print(f"{'Número par':<10} | {'Número impar':<10}")
print("-" * 22)
for p, i in zip(pares, impares):
    print(f"{p:<10} | {i:<10}")

if len(pares) > len(impares):
    for p in pares[len(impares):]:
        print(f"{p:<10} | {'':<10}")
elif len(impares) > len(pares):
    for i in impares[len(pares):]:
        print(f"{'':<10} | {i:<10}")