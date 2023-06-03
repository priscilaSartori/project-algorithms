# 3.1 - Retorne True se a palavra passada por parâmetro for um palíndromo;
# 3.2 - Retorne False se a palavra passada por parâmetro não for um palíndromo;
# 3.3 - Retorne False se nenhuma palavra for passada por parâmetro.


def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False
    if low_index >= high_index:
        return True
    if word[low_index] == word[high_index]:
        low_index += 1
        high_index -= 1
        return is_palindrome_recursive(word, low_index, high_index)
