#Regra para reconhecer:
    #Comentarios DONE
    #Palavras Reservadas * DONE
    #Tipos primitivos  DONE
    #Simbolos *
    #Identificadores  DONE
    #Numeros DONE
    #String DONE
import ply.lex as lex

#Palavras reservadas
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'and' : 'AND',
    'integer' : 'INTEGER',
    'real' : 'REAL',
    'string' : 'STRING',
    'boolean': 'BOOLEAN',
    'char' : 'CHAR',
    'array' : 'ARRAY',
    'absolute': 'ABSOLUTE',
    'set': 'SET',
    'end': 'END',
    'not': 'NOT',
    'shl': 'SHL',
    'file': 'file',
    'object': 'OBJECT' ,
    'for': 'FOR',
    'shr': 'SHR',
    'asm': 'ASM',
    'of' : 'OF',
    'begin': 'BEGIN',
    'function': 'FUNCTION',
    'on': 'ON',
    'then': 'THEN',
    'break': 'BREAK',
    'goto': 'GOTO',
    'operator': 'OPERATOR',
    'to': 'TO',
    'case': 'CASE',
    'or': 'OR',
    'type': 'TYPE',
    'const': 'CONST',
    'implementation': 'IMPLEMENTATION',
    'packed': 'PACKED',
    'unit': 'UNIT',
    'constructor': 'CONSTRUCTOR',
    'in': 'IN',
    'procedure': 'PROCEDURE',
    'until': 'UNTIL',
    'continue': 'CONTINUE',
    'inherited': 'INHERITED',
    'program': 'PROGRAM',
    'uses': 'USES',
    'destructor': 'DESTRUCTOR',
    'inline': 'INLINE',
    'record': 'RECORD',
    'var': 'VAR',
    'div': 'DIV',
    'interface': 'INTERFACE',
    'reintroduce': 'REINTRODUCE',
    'while': 'WHILE',
    'do': 'DO',
    'label': 'LABEL',
    'repeat': 'REPEAT',
    'with': 'WITH',
    'downto': 'DOWNTO',
    'mod': 'MOD',
    'self': 'SELF',
    'xor': 'XOR'
}

#Lista dos nomes dos tokens
tokens = [
    'PLUS', 'TIMES', 'MINUS', 'DIVIDE', 'EQUALS', 'ID', 'DDOT'
] + list(reserved.values())

t_ignore = ' \t'
t_ignore_SCOMMENT = r'//.* \\n'
t_ignore_MCOMMENT = r'{.*}' # '{' n words until find '}'
t_PLUS = r'\+'
t_TIMES = r'\*' #For simple tokens, strings are used
t_MINUS = r'-'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_DDOT = r':'


#r'\[\d\]
def t_ARRAY(t):
    #r'[\[\d..\d[\\]]'
    r'\[\d[.][.]\d\]'
    return t

def t_CHAR(t):
    r'[\'].[\']'
    return t

def t_BOOLEAN(t):
    r'(true|false)'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID') # Check for reserved words
    return t

def t_REAL(t):
    r'\d+[.]\d+'                
    t.value = float(t.value)
    return t
    
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'[\'].*[\']'
    return t
    
#r'[+-]?([0-9]*[.])?[0-9]+' 
#r'[0-9]*[.][0-9]+' 

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

lexer = lex.lex()
lex.input('[1..1] *  : procedure packed')

while True:
    tok = lexer.token()
    if not tok: break

    print(tok)