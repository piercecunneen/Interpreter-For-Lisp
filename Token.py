from Environment import default_environment
import re
env = default_environment()


class Token (object):
	def __init__(self, value, type):
		self.value = value
		self.type = type
	def __str__(self):
		return 'Token({type}, {value})'.format(type = self.type, value = self.value)
	def __repr__(self):
		return self.__str__()

class Integer(Token):
	def __init__(self, value):
		self.value = int(value)
	def __str__(self):
		return 'Integer({value})'.format( value = self.value)
	def __repr__(self):
		return self.__str__()

class Float(Token):
	def __init__(self, value):
		self.value = float(value)
	def __str__(self):
		return 'Float({value})'.format( value = self.value)
	def __repr__(self):
		return self.__str__()


class Symbol(Token):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return 'Symbol({value})'.format( value = self.value)
	def __repr__(self):
		return self.__str__()


class Operator(Token):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return 'Operator({value})'.format( value = self.value)
	def __repr__(self):
		return self.__str__()

class Binding(Token):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return 'Binding({value})'.format( value = self.value)
	def __repr__(self):
		return self.__str__()

class Variable(Token):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return 'Variable({value})'.format( value = self.value)
	def __repr__(self):
		return self.__str__()
class Conditional(Token):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return 'Conditional({value})'.format(value = self.value)
	def __repr__(self):
		return self.__str__()

class Function(Token):
	def __init__(self, name, arguments, definition):
		self.name = name
		self.arguments = arguments
		self.definition = definition
		self.number_of_arguments = len(arguments)
	def __str__(self):
		return 'Function({name}, {arguments} )'.format( name = self.name, arguments = self.arguments)
	def __repr__(self):
		return self.__str__()

class Keyword(Token):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return 'Keyword({value})'.format( value = self.value)
	def __repr__(self):
		return self.__str__()

def isInt(token):
	if re.search(r'^[+-]?(\d)+$|^\d+$', token):
		return True
	else:
		return False

def isFloat(token):
	if re.search(r"^[-+]?([0-9]*\.[0-9]+$|[0-9]+\.[0-9]*$)", token):
		return True
	else:
		return False
def isOperator(token):
	if re.search(r'^[+-/*<>]{1}$|^(<=)$|^(>=)$|^(eq)$', token):
		return True
	else:
		return False
def isVariable(token):
	if re.search(r'^[a-zA-Z_]+$', token):
		return True
	else:
		return False
def isConditional(token):
	if token == 'if':
		return True
	else:
		return False
def isKeyword(token):
	if token in env['keywords']:
		return True
	else:
		return False

def isFunction(token, env):
	if token in env['user_defined_functions']:
		return True
	else:
		return False



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


def interp(expression, env):
	print expression
	if isinstance(expression, Integer) or isinstance(expression, Float):
		return expression.value
	elif isinstance(expression, list):
		first_token = expression[0]

		if isinstance(first_token, Operator):
			args = [interp(i, env) for i in expression[1:]]
			return reduce(env[first_token.value], args)
		elif isinstance(first_token, Variable):
			value = env.get(first_token.value)
			if value == None:
				raise NameError("Variable  %s referenced before definition" %first_token.value)
			else:
				new_expression = [value] + expression[1:]
				return interp(new_expression, env)
		elif isinstance(first_token, Binding):
			if len(expression) != 3:
				raise TypeError("define takes 2 arguments (%d provided)" %(len(expression) - 1))
			var = expression[1]
			value = interp(expression[2], env)
			env[var.value] = value
		elif isinstance(first_token, Conditional):
			test = interp(expression[1], env)
			if test:
				return interp(expression[2], env)
			else:
				return interp(expression[3], env)
		elif isinstance(first_token, Function):

			function = env[first_token.name]
			if (len(expression) - 1 - function.number_of_arguments) != 0:
				raise TypeError("%s takes %d arguments (%d given)" %(function.name, function.number_of_arguments, len(expression) - 1))
			local_env = env.copy()

			for arg, value in zip(function.arguments, expression[1:]):
				local_env[arg.value] = interp(value, local_env)


			return interp(function.definition, local_env)
		#elif first_token.value == 'defun':
		elif isinstance(first_token, Keyword):
			if len(expression) != 4:
				raise TypeError("defun takes 3 arguments (%d given)" % (len(expression) - 1))

			function_name = expression[1]
			arguments  = expression[2]
			function_definition = expression[3]
			env[function_name.value] = Function(function_name.value, arguments, function_definition)
			env['user_defined_functions'].update({function_name.value:1})


	elif isinstance(expression, Variable):
		value = env.get(expression.value)
		if value == None:
			raise NameError("Variable  %s referenced before definition" %expression.value)
		else:
			return value





if __name__ == "__main__":
	while True:
		lisp = raw_input("PyLisp>> ")
		if  lisp.lower() == "exit":
			break
		elif lisp.replace(" ", "") == '':
			continue
		lisp_interpreted = interp(read_tokens(create_tokens(lisp)), env)
		if lisp_interpreted:
			print lisp_interpreted
