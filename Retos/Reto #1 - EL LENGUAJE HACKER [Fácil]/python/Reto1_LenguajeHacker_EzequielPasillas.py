"""
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""

cadena = input('Escribe un mensaje para transformarlo: ')

for letra in cadena:
    if letra == 'a':
        print('4', end=' ')
        continue
    elif letra == 'b':
        print('I3', end= ' ')
        continue
    elif letra == 'c':
        print('[', end= ' ')
        continue
    elif letra == 'd':
        print(')', end=' ')
        continue
    elif letra == 'e':
        print('3', end=' ')
        continue
    elif letra == 'f':
        print('|=', end= ' ')
        continue
    elif letra == 'g':
        print('&', end= ' ')
        continue
    elif letra == 'h':
        print('#', end= ' ')
        continue
    elif letra == 'i':
        print('i', end= ' ')
        continue
    elif letra == 'j':
        print(',_|', end= ' ')
        continue
    elif letra == 'k':
        print('>|', end= ' ')
        continue
    elif letra == 'l':
        print('1', end= ' ')
        continue
    elif letra == 'm':
        print('/\/' + chr(92), end= ' ')
        continue
    elif letra == 'n':
        print('^/', end= ' ')
        continue
    elif letra == 'o':
        print('0', end= ' ')
        continue
    elif letra == 'p':
        print('|*', end= ' ')
        continue
    elif letra == 'q':
        print('(_,)', end= ' ')
        continue
    elif letra == 'r':
        print('I2', end= ' ')
        continue
    elif letra == 's':
        print('5', end= ' ')
        continue
    elif letra == 't':
        print('7', end=' ')
        continue
    elif letra == 'u':
        print('(_)', end=' ')
        continue
    elif letra == 'v':
        print('\/', end= ' ')
        continue
    elif letra == 'w':
        print('\/\/', end= ' ')
        continue
    elif letra == 'x':
        print('><', end= ' ')
        continue
    elif letra == 'y':
        print('j', end= ' ')
        continue
    elif letra == 'z':
        print('2', end= ' ')
        continue
