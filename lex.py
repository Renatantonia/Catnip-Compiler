import ply.lex as lex

reserved = {
    'MEOW': 'MEOW',
    'IF_MEOW': 'IF_MEOW',
    'ELSE_MEOW': 'ELSE_MEOW',
    'FOR_TWIRL': 'FOR_TWIRL',
    'WHILE_TWIRL': 'WHILE_TWIRL',
    'PURR_SYNC': 'PURR_SYNC',
    'PURR_OR_HISS': 'PURR_OR_HISS',
    'HISS_OFF': 'HISS_OFF',
    'KIBBLE': 'KIBBLE',
    'MILK': 'MILK',
    'TUNA': 'TUNA',
    'MEOW_MATCH' : 'MEOW_MATCH',
    'FEED BOWL' : 'FEED_BOWL',
    'PURR' : 'PURR',
    'HISS' : 'HISS',
    'SCRATCH' : 'SCRATCH',
    'PAW' : 'PAW',
    'NIBBLE' : 'NIBBLE',
    'GREATER' : 'GREATER',
    'GREATER_EQ' : 'GREATER_EQ',
    'LESS' : 'LESS',
    'LESS_EQ' : 'LESS_EQ',
    'OPEN_BLOCK' : 'OPEN_BLOCK',
    'CLOSE_BLOCK' : 'CLOSE_BLOCK',
    'PSPS' : 'PSPS',
    'PAWPRINT': 'PAWPRINT',
    'CARRYBACK': 'CARRYBACK',
    'LPAREN': 'LPAREN',
    'RPAREN': 'RPAREN'
}

# Tokens
tokens = ['INTEGER','FLOAT','STRING','ID','POINT','COMMA','MINUS','LBRACKET','RBRACKET','LPAREN_FUNC','RPAREN_FUNC'] + list(reserved.values())

'''
MEOW -> print, MEOW_FUNC -> funcion, MEOW_RETURN -> retorno, IF_MEOW -> if, 
ELSE_MEOW -> else, @TWIRL -> for,~TWIRL -> while, PURR -> +, HISS -> -,
SCRATCH -> *, PAW -> /, NIBBLE -> %,PURR_SYNC -> &&, PURR_OR_HISS -> ||,
HISS_OFF -> !, KIBBLE -> numeros enteros, MILK -> Flotantes, TUNA -> sTRING, ID -> identificador
'''
# Regular expressions for tokens

t_MEOW = r'MEOW'                  # Imprimir en pantalla
t_PAWPRINT = r'PAWPRINT'        # Definir una función
t_CARRYBACK = r'CARRYBACK'    # Retornar un valor
t_PSPS = r'PSPS' #para llamar una funcion
t_IF_MEOW = r'<MEOW>'              # Condicional if
t_ELSE_MEOW = r'>MEOW<'              # Condicional else
t_FOR_TWIRL = r'@TWIRL'              # Ciclo for
t_WHILE_TWIRL = r'~TWIRL'              # Ciclo while

#regular expression for arithmetic operations

t_PURR = r'PURR' # PLUS
t_HISS = r'HISS' # MINUS
t_SCRATCH = r'SCRATCH' # MULTIPLICATION
t_PAW = r'PAW' # DIVISION
t_NIBBLE = r'NIBBLE' # MODULO

t_FEED_BOWL = r'~>' # para asignar valores

t_MEOW_MATCH = r'->' # para comparar valores
t_GREATER = r'>>~' # mayor que
t_LESS = r'~<<' # menor que
t_GREATER_EQ = r'>>=' #mayor o igual
t_LESS_EQ = r'<<=' #menor o igual

t_OPEN_BLOCK = r'<\.<' #delimitador de apertura
t_CLOSE_BLOCK = r'>\.>' #delimitador de cierre

#parentesis
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t


t_LPAREN_FUNC = r'\<\<'
t_RPAREN_FUNC = r'\>\>'


#regular expression for logical operators

t_PURR_SYNC = r'PURR_SYNC' # AND(&&)
t_PURR_OR_HISS = r'PURR_OR_HISS' # OR(||)
t_HISS_OFF = r'!~' # NOT(!)

#Regular expression for variable type

t_MILK = r'MILK' # Flotantes
def t_FLOAT(t):
    r'\d+\.\d+' 
    t.value = float(t.value) # convert to float
    return t

t_KIBBLE = r'KIBBLE' # numeros enteros para asignar a alguna variable
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value) #convert to integer
    return t



t_TUNA = r'TUNA' # STRING
def t_STRING(t):
    r'"([^"\\]|\\.)*"'  # Maneja cadenas entre comillas dobles
    t.value = t.value[1:-1]  # Eliminar las comillas de la cadena
    return t

t_MINUS = '-' #signo negativo

t_COMMA = r','

# Ignored characters
t_ignore =' \t\n'

# manejo de errores de tokens

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer   
lexer = lex.lex()

# Test the lexer function

data = '''
KIBBLE (x) ~> -6
KIBBLE (y) ~> 3
TUNA (z) ~> "hola"

PAWPRINT >> sumar << [y] 
<.<
>.>
'''
lexer.input(data)


# obtener tokens reconocidos
"""
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
 """
