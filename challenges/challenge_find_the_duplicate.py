# 5.1 - Retorne o número repetivo se a função receber como parâmetro
# uma lista com números repetidos;
# 5.2 - Retorne False se a função não receber nenhum parâmetro;
# 5.3 - Retorne False se a função receber como parâmetro uma string;
# 5.4 - Retorne False se a função receber como parâmetro uma lista
# sem números repetidos;
# 5.5 - Retorne False se a função receber como parâmetro apenas um valor;
# 5.6 - Retorne False se a função receber como parâmetro um número negativo;
# 5.7 - A função deverá, por meio de análise empírica, se comportar
# (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja,
# com complexidade assintótica linearítmica.

def find_duplicate(nums):
    nums.sort()
    previous_num = 'not a number'
    for num in nums:
        if (type(num) == str or num < 0 or num == None or num == ''): return False
        if(previous_num == num): 
            return previous_num
        previous_num = num

    return False  