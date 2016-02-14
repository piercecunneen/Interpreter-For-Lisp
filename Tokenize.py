from typeChecking import isInt, isFloat, isOperator, isVariable, isConditional, isKeyword, isFunction
from Token import *
def translate_to_type(token):
	if isKeyword(token):
		return Keyword(token)
	elif isInt(token):
		return Integer(token)
	elif isFloat(token):
		return Float(token)
	elif isOperator(token):
		return Operator(token)
	elif token == 'define':
		return Binding(token)
	elif isConditional(token):
		return Conditional(token)
	elif isVariable(token):
		return Variable(token)
	else:
		print token
		raise SyntaxError("ERROR!!!")

def read_tokens(tokens):
	if len(tokens) == 0:
		raise SyntaxError('End of line ... not expected')
	elif tokens[0] == ")":
		raise SyntaxError("unexpected closure of parenthesis")
	token = tokens.pop(0)
	if token == "(":
		new_group = []
		while tokens[0] != ')':
			new_group.append(read_tokens(tokens))
		tokens.pop(0)
		return new_group
	else:
		return translate_to_type(token)


def create_tokens(text):
	"""
	takes in lisp and tokenizes the code

	"""
	return text.replace("(", " ( ").replace(")", " ) ").split()
