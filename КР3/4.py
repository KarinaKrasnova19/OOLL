#Словарь
def synonym(n, synonym_pairs, word):
    synonyms_dict = {}

    for pair in synonym_pairs:
        word1, word2 = pair.split()
        synonyms_dict[word1] = word2
        synonyms_dict[word2] = word1
    
    return synonyms_dict.get(word, "Синоним не найден")

n = int(input("Введите количество пар синонимов: "))
synonym_pairs = [input().strip() for _ in range(n)]
word = input("Введите слово для поиска синонима: ").strip()

result = synonym(n, synonym_pairs, word)
print(result)
