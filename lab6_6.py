# Zadanie 6

# Napisz klasę "Bag of words", która będzie "workiem słów" z zadanego dokumentu. Oznacza to, że ma w sobie przechowywać informacje o tym ile razy każde słowo wystąpiło w dokumencie. Dodatkowo ma udostępniać następującą funkcjonalność:
# * Można utworzyć go na dwa sposoby:
# ```
# bow = BagOfWords("ala ma kota ala ma ala")
# bow = BagOfWords(open("plik.txt"))
# ```
# * Możliwość wyświetlania go po prostu pisząc print(bow) (kolejność taka sama jak przy przeglądaniu forem)
# ```
# ala:3, ma:2, kota:1
# ```
# * Sprawdzanie czy jakieś słowo należy do naszego worka pisząc
# ```
# if 'ala' in bow:
#     ...
# ```
# * Przeglądanie słów w worku od najczęściej do najrzadziej występującego, czyli
# ```
# for word in bow:
#   print(word)
# ```
#     powinniśmy zobaczyć
# ```
# ala
# ma
# kota
# ```
# * Możliwość dodawania dwóch worków, pisząc
# ```
# bow1 = BagOfWords("ala ma kota ala ma ala")
# bow2 = BagOfWords("tomek tez ma kota")
# bow3 = bow1 + bow2
# print('tomek' in bow1) # False
# print('tomek' in bow3) # True
# print('ala' in bow3) # True
# print(bow3) # ala:3, ma:3, kota:2, tez:1, tomek:1
#     ```
# * Odczytywanie częstości wystąpień słów poprzez nawiasy kwadratowe
# ```
# print(bow1["ala"]) # 3
# print(bow3["ala"]) # 3
# ```
# * Aktualizację cześtości wystąpień
# ```
# bow3['tomek'] = 10
# for el in bow3:
#     print el
# ```
#     powinno wyświetlić najpierw `tomek`

class BagOfWords:
    """
    Klasa BagOfWords reprezentuje strukturę danych typu "worek słów", 
    która zlicza wystąpienia każdego słowa w podanym dokumencie (ciągu znaków) lub pliku tekstowym.
    """
    pass


# Przykładowe użycie
bow1 = BagOfWords("ala ma kota ala ma ala")
bow2 = BagOfWords("tomek tez ma kota")
bow3 = bow1 + bow2

print(bow3) # ala:3, ma:3, kota:2, tez:1, tomek:1
print('tomek' in bow1) # False
print('tomek' in bow3) # True
print('ala' in bow3) # True
print(bow3["ala"]) # 3

bow3['tomek'] = 10
for word in bow3:
    print(word)