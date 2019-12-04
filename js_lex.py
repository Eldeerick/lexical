import ply.lex as lexer

reserved = {
  'boolean': 'BOOLEAN',
  'class': 'CLASS',
  'if': 'IF',
  'string': 'STRING',
  'integer': 'INTEGER',
  'real': 'REAL',
  'false': 'FALSE',
  'true': 'TRUE',
  'return': 'RETURN',
  'else': 'ELSE',
  'var': 'VAR',
  'let': 'LET',
  'const': 'CONST',
  'continue': 'CONTINUE',
  'try': 'TRY',
  'for': 'FOR',
  'while': 'WHILE',
  'function': 'FUNCTION',
  'catch': 'CATCH',
  'typeof': 'TYPEOF',
  'switch': 'SWITCH',
  'do': 'DO',
  'break': 'BREAK',
  'void' : 'VOID',
  'import': 'IMPORT',
  'export': 'EXPORT',
  'extends': 'EXTENDS',
  'await': 'AWAIT',
  'this': 'THIS',
  'new': 'NEW',
  'finally': 'FINALLY',
  'default': 'DEFAULT'  
}

tokens = [
  'PLUS', 'INCREMENT', 'DECREMENT', 'TIMES', 'EXPO', 'MINUS', 'DIVIDE', 'EQUALS', 'MOD', 'ID', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN' 
] + list(reserved.values())

t_ignore = ' \t'
t_ignore_SCOMMENT = r'//^\\n'
t_ignore_MCOMMENT = r'(\/\*)[^\\n]*(\*\/)'
t_INCREMENT = r'\+\+' 
t_PLUS = r'\+'
t_EXPO = r'\*\*'
t_TIMES = r'\*'
t_DECREMENT = r'--'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_MOD = '%'
t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ARRAY(t):
    #r'[\[\d..\d[\\]]'
    r'\[\d[.][.]\d\]'
    return t

def t_BOOLEAN(t):
    r'(true|false)'
    return t

def t_REAL(t):
    r'\d+[.]\d+'                
    t.value = float(t.value)
    return t
    
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  t.type = reserved.get(t.value, 'ID') # Check for reserved words
  return t

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
  
def t_STRING(t):
  r'[\'\"].*[\'\"]'
  t.value = str(t.value)
  return t

lexer.lex() #Builds the lexer
lexer.input('let nome = \'Andre\' const port = 3001.01')

while True:
    tok = lexer.token()
    if not tok: break
    print(tok)