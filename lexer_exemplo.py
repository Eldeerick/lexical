import ply.lex as lex

tokens = [ 'NAME', 'NUMBER', 'PLUS', 'MINUS', 'TIMES',
           'DIVIDE', 'EQUALS' ]
#tokens list specifies all of the possible tokens

t_ignore = ' \t'
t_PLUS = r'\+' #The names must match with the list
t_MINUS = r'-'
t_TIMES = r'\*' #For simple tokens, strings are used
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*' #Tokens are defined by regular expressions
#Each token has a matching declaration of the form t_TOKNAME

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
#Functions are used when special action code must execute

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

lexer = lex.lex() #Build a lexer

lex.input("int i")
while True:
    tok = lexer.token()
    if not tok: break

    print(tok)