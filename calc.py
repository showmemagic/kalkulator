# kalkulator

import sys

if len(sys.argv) != 4:
    print("Użycie: calc.py <liczba_1> <operacja +-> <liczba_2>")
    sys.exit(1)

liczba_1 = int(sys.argv[1])
operacja = sys.argv[2]
liczba_2 = int(sys.argv[3])

if operacja == "+":
    result = liczba_1 + liczba_2
elif operacja == "-":
    result = liczba_1 - liczba_2
else:
    print("Niepoprawny operator")
    sys.exit(1)

with open("/tmp/wynik.txt", "w") as file:
    file.write( str(result) )

print( result )
