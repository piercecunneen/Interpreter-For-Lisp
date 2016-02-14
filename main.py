from Environment import default_environment
from Tokenize import read_tokens, create_tokens
from interp import interp, return_quoted_text




if __name__=='__main__':
    env = default_environment()
    while True:
        lisp = raw_input("PyLisp>> ")
        if (lisp.lower() == 'exit' or lisp.lower() == 'exit()'):
            break
        elif lisp.replace(" ","") == '':
            continue
        lisp_tokens = read_tokens(create_tokens(lisp))
        lisp_interpreted = interp(lisp_tokens,env)
        if lisp_interpreted:
            print lisp_interpreted
