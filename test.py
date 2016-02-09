"""
Testing suite for lisp interpreter


"""
from Token import *

def addition_tests():

    lisp = "(+ 2 4)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 6)


    lisp = "(+ 2 -5)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -3)

    lisp = "(+ (+ 12 5) (+ 6 -4))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 19)

    lisp = "(+ (+ (+ 3 2) 2) (+ 2 (+ 4 6) ))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 19)

def subtraction_tests():

    lisp = "(- 5 4)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 1)


    lisp = "(- 2 -5)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 7)

    lisp = "(- (- 6 1) (- 6 -4))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -5)

    lisp = "(- (- (- 34 1) 4) (- -4 (- 1 22) ))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 12)

def multiplication_tests():

    lisp = "(* 5 4)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 20)


    lisp = "(* 2 -5)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -10)

    lisp = "(* (* 4 3) (* 10 -6))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -720)

    lisp = "(* (* (* 34 1) 4) (* -4 (* 1 22) ))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -11968)


def division_tests():

    lisp = "(/ 5 4)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 1)


    lisp = "(/ 2 -5)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -1)

    lisp = "(/ (/ 40 3) (/ 10 -6))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -7)

    lisp = "(/ (/ (/ 34 1) 4) (/ -4 (/ 22 22) ))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == -2)

    lisp = "(/ 1 2)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 0)

def mixed_arithmatic_tests():
     lisp = "(+ 5 (* 2 3)))"
     lisp_tokens = read_tokens(create_tokens(lisp))
     assert(interp(lisp_tokens, env) == 11)


     lisp = "(+ (* (- 3 1) (/ 34 2)) 3)"
     lisp_tokens = read_tokens(create_tokens(lisp))
     assert(interp(lisp_tokens, env) == 37)

     lisp = "(/ (+ 40 3) (* 10 (- 2 4)))"
     lisp_tokens = read_tokens(create_tokens(lisp))
     assert(interp(lisp_tokens, env) == -3)

     lisp = "(* (- (+ 34 1) 4) (* -4 (/ 24 22) ))"
     lisp_tokens = read_tokens(create_tokens(lisp))
     assert(interp(lisp_tokens, env) == -124)

     lisp = "(- (+ (* 3 4) 3 4) (+ (/ 3 2) (* 2 4) 4))"
     lisp_tokens = read_tokens(create_tokens(lisp))
     assert(interp(lisp_tokens, env) == 6)


def define_variables():
    # reset default_environment
    env = default_environment()

    lisp = "(define r 10)"
    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(+ r r)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 20)

    lisp = "(define r 12)"
    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(+ r (* r r))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 156)



    lisp = "(define r (- (+ (* 3 4) 3 4) (+ (/ 3 2) (* 2 4) 4)))"

    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(define p (* (- (+ 34 1) 4) (* -4 (/ 24 22) )))"
    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(* p r p)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == ((-124)**2 * 6))

    lisp = "(define r (- (+ (* 3 4) 3 4) (+ (/ 3 2) (* 2 4) 4)))"

    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(define p 5.2)"
    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(* (+ r p) p r)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == (11.2 * 6 * 5.2))

def type_checker_functions():

    # check integers
    assert(isInt('1') == True)
    assert(isInt('1233') == True)
    assert(isInt('0') == True)
    assert(isInt('1.') == False)
    assert(isInt('.1') == False)
    assert(isInt('a') == False)
    assert(isInt('1b') == False)
    assert(isInt('') == False)

    # check Floats
    assert(isFloat('1.') == True)
    assert(isFloat('1.3') == True)
    assert(isFloat('1') == False)
    assert(isFloat('1.r') == False)
    assert(isFloat('1.3423') == True)
    assert(isFloat('.1') == True)
    assert(isFloat('r.') == False)
    assert(isFloat('123') == False)
    assert(isFloat('12..3') == False)
    assert(isFloat('1..') == False)
    assert(isFloat('..123') == False)
    assert(isFloat('12.32353r') == False)

    # check operators
    assert(isOperator('+') == True)
    assert(isOperator('-') == True)
    assert(isOperator('/') == True)
    assert(isOperator('*') == True)
    assert(isOperator('++') == False)
    assert(isOperator('+-') == False)
    assert(isOperator('+/') == False)
    assert(isOperator('+r') == False)
    assert(isOperator('r+') == False)
    assert(isOperator('+r') == False)
    assert(isOperator('+.') == False)
    assert(isOperator('.+') == False)
    assert(isOperator('+ ') == False)
    assert(isOperator(' +') == False)
    assert(isOperator('eq') == True)
    assert(isOperator('<') == True)
    assert(isOperator('>') == True)
    assert(isOperator('<=') == True)
    assert(isOperator('>=') == True)
    assert(isOperator('><') == False)
    assert(isOperator('<>') == False)




    # check variable
    assert(isVariable('variable') == True)
    assert(isVariable('camelCase') == True)
    assert(isVariable('_under_score_test') == True)
    assert(isVariable('ending_with_underscore__') == True)
    assert(isVariable('UPPERCASE') == True)
    assert(isVariable('r4R') == False)





def checkFunctions():
    # # reset default_environment
    env = default_environment()

    # # simple function define and call
    lisp = "(defun foo (x) (+ x x)))"
    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(foo 3)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 6)

     # using a function call as an argument to a call to the same function
    lisp = "(foo (foo 4))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 16)

    # multiple arguments, more complicated function body, unused argument (no error should be raised as a result of an unused argument)
    lisp = "(defun bar (x y) (+ (* 2 x) 7))"
    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(bar 8 9)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 23)

    # # calling two seperate functions at once (checking also to see if defining a second function causes problems for call of first)
    lisp = "(bar (foo 2) (foo 4))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 15)

    # # functions inside functions inside function
    lisp = "(bar (foo (bar 4 2)) (foo 4))"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 67)


    # function as explicit argument to function
    lisp = "(defun take_a_function (a b) (+ (a 2 3) b))"
    interp(read_tokens(create_tokens(lisp)), env)
    lisp = "(take_a_function bar 3)"
    lisp_tokens = read_tokens(create_tokens(lisp))
    assert(interp(lisp_tokens, env) == 14)

















if __name__ == "__main__":
    addition_tests()
    subtraction_tests()
    multiplication_tests()
    division_tests()
    mixed_arithmatic_tests()
    define_variables()
    type_checker_functions()
    checkFunctions()
    print "Passed all test cases"
