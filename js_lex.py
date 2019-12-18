import ply.lex as lexer

#ECMAScript 2018 (ES9)
#Fonte: https://www.ecma-international.org/ecma-262/9.0/#prod-ReservedWord
reserved = {
  'await': 'AWAIT'
  'break': 'BREAK',
  'case': 'CASE',
  'catch': 'CATCH',
  'class': 'CLASS',
  'const': 'CONST',
  'continue': 'CONTINUE',
  'debugger': 'DEBUGGER',
  'default': 'DEFAULT',
  'delete': 'DELETE',
  'do': 'DO',
  'else': 'ELSE',
  'export': 'EXPORT',
  'extends': 'EXTENDS',
  'finally': 'FINALLY',
  'for': 'FOR',
  'function': 'FUNCTION',
  'if': 'IF',
  'import': 'IMPORT',
  'in': 'IN',
  'instanceof': 'INSTANCEOF',
  'new': 'NEW',
  'return': 'RETURN',
  'super': 'SUPER',
  'switch': 'SWITCH',
  'this': 'THIS',
  'throw': 'THROW',
  'try': 'TRY',
  'typeof': 'TYPEOF',
  'var': 'VAR',
  'void' : 'VOID',
  'while': 'WHILE',
  'with': 'WITH',
  'yield': 'YIELD',
}
#Fonte: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Lexical_grammar
tokens = [
  'ID',
  #Delimitadores
  'LEFT_BRACKET', 
  'RIGHT_BRACKET', 
  'LEFT_BRACE', 
  'RIGHT_BRACE', 
  'LEFT_PAREN', 
  'RIGHT_PAREN',
  'SINGLE_QUOTE',
  'DOUBLE_QUOTES',
  'BACKSTICK',
  'ARROW_FUNCTION',
  #Literais
  'NULL',
  'BOOLEAN',
  'DECIMAL',
  'BINARY',
  'OCTAL',
  'HEXADECIMAL',
  'OBJECT',
  'ARRAY',
  'STRING',
  #Operadores Aritmeticos
  'PLUS',
  'MINUS',
  'INCREMENT', 
  'DECREMENT', 
  'TIMES', 
  'EXPO', 
  'DIVIDE',
  'MOD',
  #Operadores Logicos
  'AND',
  'OR',
  'NOT',
  #Operadores de Atribuicao
  'ASSING',
  'ADD_ASSIGN',
  'SUB_ASSIGN',
  'TIMES_ASSIGN',
  'DIVIDE_ASSIGN',
  'MOD_ASSIGN',
  'EXP_ASSIGN',
  #Mais Operadores de Atribuicao
  'BITLEFT_ASSIGN',
  'BITRIGHT_ASSIGN',
  'AND_ASSIGN',
  'XOR_ASSIGN',
  'OR_ASSIGN'
  #Operadores de comparacao 
  'EQUALS', 
  'NOT_EQUAL',
  'STRICTLY_EQUAL',
  'STRICTLY_NOT_EQUAL',
  'GREAT_THAN',
  'GREAT_EQUAL',
  'LESS_THAN',
  'LESS_EQUAL'
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
lexer.input('')

while True:
    tok = lexer.token()
    if not tok: break
    print(tok)