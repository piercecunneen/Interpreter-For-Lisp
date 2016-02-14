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
		
