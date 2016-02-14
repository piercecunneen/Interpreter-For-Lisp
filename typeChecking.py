import re
from Environment import default_environment
env = default_environment()

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
