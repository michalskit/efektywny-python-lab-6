# Zadanie 2
# Napisz program, który (używając wyrażeń regularnych) przefiltruje plik atoms.txt,
# tak by pozostały jedynie linie dot. bezproblemowego przebiegu eksperymentu,
# a następnie utworzy nowy plik o nazwie clean_atoms.txt i zapisze do niego
# przefiltrowane linie.
#
# Przykłady linii, które powinny zostać odrzucone:
# RUN 000039 COMPLETED. OUTPUT IN FILE yttrium.dat. 1 UNDERFLOW WARNING.
# RUN 000058 COMPLETED. OUTPUT IN FILE cerium.dat. ALGORITHM DID NOT CONVERGE AFTER 100000 ITERATIONS.
#
# Format każdej linii:
# RUN [[NUMER Z DOKŁADNIE 6 CYFR]] COMPLETED. OUTPUT IN FILE [[NAZWA]].dat. [[COKOLWIEK]]
#
# Program powinien działać w katalogu, w którym znajduje się plik atoms.txt
# i utworzyć w nim plik clean_atoms.txt

import re

pattern = ...

with open('atoms.txt', 'r') as atoms, open('clean_atoms.txt', 'w') as clean_atoms:
    for line in atoms:
        if ...:
            clean_atoms.write(line)