"""
Módulo do livro head first.
"""
# Nessa função está sendo especificado o tipo do valor e retorno que a função deve receber e retornar
# O tipo é especificado da seginte forma (word:str)
# O retorno é especificado da seguinte forma (-> set). set é a definição de um conjunto.
def search4vowels(phrase:str) -> set:
	"""
	Retorna as vogais contidas na entrada.
	"""
	vowels = set('aeiou')
	return vowels.intersection(set(phrase))


# Seta o valor padrão de do conjunto a ser encontrado.
def search4letters(phrase:str, letters:str='aeiou') -> set:
	"""
	Retorna o conjunto de letras especificados.
	"""
	return set(letters).intersection(set(phrase))
