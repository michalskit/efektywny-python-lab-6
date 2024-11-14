# Zadanie 3
# Napisz program który wypisze linie z logu systemowego "messages.txt"
# które zawierają informacje o nieprawidłowej nazwie użytkownika (invalid user)
#
# Przykład linii wejściowej:
# Jun 29 20:18:40 noether sshd[5805]: Invalid user tester from 218.189.194.200
#
# Format wyjściowy:
# Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18:40
#                                                                                                         ^^^
# - Program powinien działać w katalogu, w którym znajduje się plik messages.txt
# - Wynik należy zapisać do pliku formatted_messages.txt
# - Nazwy miesięcy należy przetłumaczyć na język polski
# - W przypadku nazw użytkowników zawierających znaki specjalne (np. "/"), należy je zachować

import re

pattern = ...

with open('messages.txt') as messages, open('formatted_messages.txt', 'w') as outfile:
    for line in messages:

        if ...:
            outfile.write(... + '\n')

