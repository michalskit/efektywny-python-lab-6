# Zadanie 4
# Uzupenij ponizsze funckje korzystajac z zaimporotwanych klas

from collections import defaultdict

def count_letters(word):
    """ Zwraca slownik gdzie kluczami sa litery, a wartosci ilosc ich wystepowania """
    pass

# Testy
print(count_letters('aaaaa') == {'a': 5})
print(count_letters('abbccaaaa') == {'a': 5, 'b': 2, 'c': 2})
print(count_letters('abc') == {'a': 1, 'b': 1, 'c': 1})


def group_words_by_first_letter(text):
    """ Dzieli tekst po spacjach i zwraca slownik gdzie kluczami sa pierwsze litery,
      a wartosciami listy slow zaczynajacych sie na te litery"""
    pass


# Testowanie funkcji
print(group_words_by_first_letter("ala ma kota") == {'a': ['ala'], 'm': ['ma'], 'k': ['kota']})
print(group_words_by_first_letter("ala ma kota ala ma psa") == {'a': ['ala', 'ala'], 'm': ['ma', 'ma'], 'k': ['kota'], 'p': ['psa']})   
print(group_words_by_first_letter("ala ma kota ale marysia ma konia") == {'a': ['ala', 'ale'], 'm': ['ma', 'marysia', 'ma'], 'k': ['kota', 'konia']})