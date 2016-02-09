

def default_environment():
	import operator as op
	from random import random
	environment = {}
	environment.update({
		'keywords': set(['defun', 'pow', 'sqrt','random']),
		'user_defined_functions': {},
		'+':op.add, '-':op.sub, '*':op.mul, '/':op.div, '>':op.gt, '<':op.lt,
		'>=':op.ge, '<=':op.le, 'eq':op.eq,
		'defun':"function_define",
		"sqrt": lambda x: x**.5, "pow": lambda x,y: x**y,
		"random": lambda: random(),
		'#t': True, '#T':True,
		'#f': False, '#F': False
		})
	return environment
