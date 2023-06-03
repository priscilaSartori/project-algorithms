# Recebe uma string message e um inteiro key como parâmetros
# Se key e message não possuírem os tipos corretos,
# uma exceção deve ser lançada
# Se key não for um índice positivo válido de message,
# retorna a string message invertida
# Se key for ímpar:
# divide message no índice key, inverte os caracteres de cada parte,
# e retorna a união das partes novamente com "_" entre elas
# Se key for par:
# divide message no índice key, inverte a posição das partes,
# inverte os caracteres de cada parte, e retorna a união das partes
# novamente com "_" entre elas


from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 0)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('message', 'key')

    assert encrypt_message("message", -2) == 'egassem'
    assert encrypt_message("message", 1) == 'm_egasse'
    assert encrypt_message("message", 2) == 'egass_em'
