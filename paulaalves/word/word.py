"""
Given two strings of letters, determine whether the second can be made from the first by removing one letter. 
The remaining letters must stay in the same order.
"""

def word_size(firstword, secondword):
	if len(firstword) < len(secondword):
		return False
	else:
		change_word(firstword, secondword)
		return True


def change_word(firstword, secondword):
	for n in range(len(firstword)):
		if firstword[:n] + firstword[n + 1:] == secondword:
			return True
	return False

test1 = word_size('motor', 'moto')
print(test1)
test2 = word_size('mato', 'ato')
print(test2)
 
assert word_size('dados', 'caso') == True
assert word_size('motor', 'moto') == True
assert word_size('casa', 'árvore') == False
assert word_size('asa', 'casa') == False

assert change_word('motor', 'moto') == True
assert change_word('mato', 'ato') == True
assert change_word('casa', 'asa') == True
assert change_word('lente', 'tele') == False
