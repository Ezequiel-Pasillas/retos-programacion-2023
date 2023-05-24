"""
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 *
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
"""

rango = range(14)
numerosPrimosLista = []
iterador = 0

for numero in rango:
    if numero % 2 != 0 or numero == 2:
        if numero % 3 != 0 or numero == 3:
            if numero % 5 != 0 or numero == 5:
                if numero == 1:
                    continue
                else:
                    # print(f'Numeros primos: {numero}') # Se imprimen los numeros primos
                    numerosPrimosLista.append(numero) # Se guardan todos los numeros primos en una lista

# print(len(numerosPrimosLista)) # Se visualiza el tamaño de la lista

while iterador < len(numerosPrimosLista):
    if iterador+1 >= len(numerosPrimosLista): # Si el iterador sobre pasa el tamaño del arreglo se termina la ejecucion
        break
    else:
        numerosPrimosGemelos = numerosPrimosLista[iterador+1] - numerosPrimosLista[iterador] # Se hace la resta para saber si son Primos Gemelos
        if numerosPrimosGemelos == 2: # Si el resultado es igual a dos entonces son primos gemelos
            print(f'({numerosPrimosLista[iterador]}, {numerosPrimosLista[iterador+1]}),', end= ' ')
        iterador += 1
