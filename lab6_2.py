# Zadanie 2

# Napisz program, który (używając wyrażeń regularnych) przefiltruje plik atoms.txt,
# tak by pozostały jedynie linie dot. bezproblemowego przebiegu eksperymentu,
# a następnie utworzy nowy plik o nazwie clean_atoms.txt i zapisze do niego
# przefiltrowane linie.
# czyli np. powinny zostać odrzucone takie linie jak
# ```
# RUN 000039 COMPLETED. OUTPUT IN FILE yttrium.dat. 1 UNDERFLOW WARNING.
# ```
# czy
# ```
# RUN 000058 COMPLETED. OUTPUT IN FILE cerium.dat. ALGORITHM DID NOT CONVERGE AFTER 100000 ITERATIONS.
# ```
# można jedynie założyć, że każda linijka pasuje do poniższego schematu
# ```
# RUN [[NUMER Z DOKŁADNIE 6 CYFR]] COMPLETED. OUTPUT IN FILE [[NAZWA]].dat. [[COKOLWIEK]]

import re

pattern = ...

with open('atoms.txt', 'r') as atoms, open('clean_atoms.txt', 'w') as clean_atoms:
    for line in atoms:
        if ...:
            clean_atoms.write(line)