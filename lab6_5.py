# Zadanie 5

# Uzupełnij brakujące metody poniższej klasy.

class FrozenDictionary(object):
    def __init__(self, dictionary):
        """Tworzy nowy zamrożony słownik z podanego słownika"""
        pass
    
    def __hash__(self):
        """Zwraca hasz słownika (int)"""
        pass    

    def __eq__(self, other):
        """Porównuje nasz słownik z zamrożonym słownikiem d"""
        pass
    
    def __repr__(self):
        """Zwraca reprezentację naszego słownika jako string"""
        pass
    
    def __getitem__(self, key):
        """Zwraca wartość dla podanego klucza"""
        pass
    

dicts = [FrozenDictionary({'ala': 4}), 
         FrozenDictionary({'ala': 1, 'jacek': 0}),
         FrozenDictionary({'ala': 4}), 
         FrozenDictionary({'ala': 2}), 
         FrozenDictionary({'jacek': 0, 'ala': 1})]

s = set(dicts)
print(dicts[0] == dicts[2])
print(dicts[0] != dicts[3])
print(len(s) == 3)
for d in dicts:
    print(d in s)

# Powinno wyświetlić coś w stylu set([{'ala': 4}, {'ala': 1, 'jacek': 0}, {'ala': 2}])
print(s)