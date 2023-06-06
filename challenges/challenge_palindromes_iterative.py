# 6.1 - Retorne True se a palavra passada como parâmetro for um palíndromo,
# executando uma função iterativa;
# 6.2 - Retorne False se a palavra passada como parâmetro não for um
# palíndromo, executando uma função iterativa;
# 6.3 - Retorne False se nenhuma palavra for passada como parâmetro,
# executando uma função iterativa ;
# 6.4 - A função deverá, por meio de análise empírica, se comportar
# (no avaliador remoto em sua Pull Request)
# como no máximo O(n), ou seja, com complexidade assintótica linear.

def is_palindrome_iterative(word):
    if word == "" or word is None:
        return False
    low = 0
    high = len(word) - 1
    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1
    return True
