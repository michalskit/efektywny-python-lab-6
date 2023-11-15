# Zadanie 3
# Napisz program który wypisze linie z logu systemowego "messages.txt"
# które zawierają informacje o nieprawidłowej nazwie użytkownika (invalid user)

# Przerób program tak, żeby wyświetlał sformatowane komunikaty, tzn.
# ```
# Jun 29 20:18:40 noether sshd[5805]: Invalid user tester from 218.189.194.200
# ```
# powinno zostać przerobione na
# ```
# Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18
# ```

import re

pattern = ...

with open('messages.txt') as messages, open('formatted_messages.txt', 'w') as outfile:
    for line in messages:

        if ...:
            outfile.write(... + '\n')

