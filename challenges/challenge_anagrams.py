# 4.1 - Retorne True se as palavras passadas por parâmetro forem anagramas;
# 4.2 - Retorne False se as palavras passadas por parâmetro não forem
# anagramas;
# 4.3 - Retorne False se alguma das palavras passadas por parâmetro for
# uma string vazia;
# 4.4 - A função deverá, por meio de análise empírica, se comportar
# (no avaliador remoto em sua Pull Request) como no máximo O(n log n),
# ou seja, com complexidade assintótica linearítmica.
# 4.5 - Retorne True se as palavras passadas forem anagramas sem diferenciar
# maiúsculas e minúsculas.

def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index += 1
        else:
            string[general_index] = right[right_index]
            right_index += 1


def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())
    merge_sort(first_string)
    merge_sort(second_string)
    first_string = "".join(first_string)
    second_string = "".join(second_string)

    return (first_string, second_string, first_string == second_string)
