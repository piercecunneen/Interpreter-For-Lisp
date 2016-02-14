from Token import *

def interp(expression, env):
    if isinstance(expression, Integer) or isinstance(expression, Float):
        return expression.value
    elif isinstance(expression, list):
        first_token = expression[0]

        if isinstance(first_token, Operator):
            #interp each individual argument, then apply operator at the end
            args = [interp(i, env) for i in expression[1:]]
            return reduce(env[first_token.value], args)
        elif isinstance(first_token, Variable):
            value = env.get(first_token.value) # use .get to avoid keyError
            if value == None:
                raise NameError("Variable  %s referenced before definition" %first_token.value)
            else:
                # get the value of variable, insert that into the expression in place of the variable, and then re-evaluate expression
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

        elif isinstance(first_token, Keyword):
            if first_token.value == 'defun':
                if len(expression) != 4:
                    raise TypeError("defun takes 3 arguments (%d given)" % (len(expression) - 1))

                function_name = expression[1]
                arguments  = expression[2]
                function_definition = expression[3]
                env[function_name.value] = Function(function_name.value, arguments, function_definition)
                env['user_defined_functions'].update({function_name.value:1})
            elif first_token.value == 'sqrt':
                if (len(expression) != 2):
                    raise TypeError("sqrt takes 2 arguments (%d given)" % (len(expression) - 1))
                return env['sqrt'](interp(expression[1], env))
            elif first_token.value == 'exp':
                if (len(expression) != 3):
                    raise TypeError("exp takes 3 arguments (%d given)" % (len(expression) - 1))
                return env['exp'](interp(expression[1], env), interp(expression[2], env))
            elif first_token.value == 'random':
                if (len(expression) != 1):
                    raise TypeError("random takes 1 arguments (%d given)" % (len(expression) - 1))
                return env['random']()
            elif first_token.value == 'quote':
                if (len(expression) != 2):
                    raise TypeError("%s takes 1 arguments (%d given)" %  (first_token.value, len(expression) - 1))
                return  return_quoted_text(expression[1])
            elif first_token.value == 'list':
                list_elements = [str(interp(i, env)) for i in expression[1:]]
                return "(" + " ".join(list_elements) + ")"
    elif isinstance(expression, Variable):
        value = env.get(expression.value)
        if value == None:
            raise NameError("Variable  %s referenced before definition" %expression.value)
        else:
            return value

def return_quoted_text(expression):
    text = '('
    if  isinstance(expression, list):
        for sub_exp in expression:
            text = text + return_quoted_text(sub_exp) + " "
        return text + ")"
    elif isinstance(expression, Function):
        return expression.name
    else:
        return str(expression.value)
