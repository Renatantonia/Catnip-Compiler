import ply.yacc as yacc
from lex import tokens

functions = []


# Regla para los parámetros dentro de la definición de la función
def p_parameters(p):
    '''
    parameters : parameter
               | parameter COMMA parameters
    '''
    if len(p) == 2:
        p[0] = [p[1]]  # Un solo parámetro
    else:
        p[0] = [p[1]] + p[3]  # Parámetros adicionales separados por coma


# Regla para un parámetro individual (en este caso, un ID)
def p_parameter(p):
    '''
    parameter : ID
    '''
    p[0] = p[1]  # El parámetro es simplemente el ID (nombre del parámetro)


def p_function_call(p):
    '''
    function_call : PSPS LPAREN_FUNC ID RPAREN_FUNC LBRACKET parameters RBRACKET
    '''
    func_name = p[3]
    parameters = p[6] #parameters

    for func in functions:
        if func ['name'] == func_name:
            print(f'llamando a la funcion: {func_name} con los parametros: {','.join(parameters)}')



#funcion sin retorno (procedimiento)
def function_definition_without_return(p):
    '''statement: PAWPRINT LPAREN_FUNC ID RPAREN_FUNC LBRACKET parameters RBRACKET block'''

    
    func_name = p[2] #function name
    parameters = p[5] #parameters
    body = p[7]

    functions.append({
        'name': func_name,
        'parameters': parameters,
        'body': body
    })

    print(f"Definición de función sin retorno: {func_name} ({', '.join(parameters)})")
    print(f"Funciones definidas: {[f['name'] for f in functions]}")



#funcion con retorno
def function_definition_with_return(p):

    '''
    statement: KIBBLE PAWPRINT LPAREN ID RPAREN LBRACKET parameters RBRACKET OPEN_BLOCK statements MEOW_RETURN CLOSE_BLOCK
             | MILK PAWPRINT LPAREN ID RPAREN LBRACKET parameters RBRACKET OPEN_BLOCK statements MEOW_RETURN CLOSE_BLOCK
             | TUNA PAWPRINT LPAREN ID RPAREN LBRACKET parameters RBRACKET OPEN_BLOCK statements MEOW_RETURN CLOSE_BLOCK
    '''
    if len(p) == 13:
        return_type = p[1] #KIBBLE,MILK,TUNA
        func_name = p[4] #function name
        parameters = p[7] #parameters
        statements = p[10] #body
        return_value = p[11] #return value

        functions.append({
            'name': func_name,
            'return_type': return_type,
            'parameters': parameters,
            'body': statements,
            'return_value': return_value
        })

        print(f"Definición de función con retorno: {func_name} ({', '.join(parameters)}) -> {return_value}")



def p_return_statement(p):
    '''
    return_statement : CARRYBACK expression
    '''
    p[0] = p[2]  # El valor que se devuelve es la expresión evaluada (p[2] es el valor de la expresión)

def p_statement_meow(p):
    '''
    statement : MEOW STRING
              | MEOW expression
    '''


    if len(p) == 3 and isinstance(p[2], str):  # Caso de cadena
        print(f'Print: {p[2]}')  # Elimina comillas
    else:  # Caso de expresión
        print(f"Print: {p[2]}")  # Imprime el resultado de la expresión


def p_program(p):
    '''
    program : statements
    '''
    p[0] = p[1]  # Asigna el valor de statements al resultado final

#REGLAS PARA OPERACIONES ARITMETICAS

# Definir precedencia
precedence = (
    ('right','UMINUS'), #operador unario con una mayor precedencia
    ('left', 'PURR', 'HISS'), # Suma y resta tienen la misma prioridad
    ('left', 'SCRATCH', 'PAW', 'NIBBLE'),  # Multiplicación, división, módulo
    ('left', 'GREATER','LESS', 'GREATER_EQ','LESS_EQ','MEOW_MATCH'), # comparaciones
    ('right','FEED_BOWL') # Asignacion
)

def type_personalized(valor):
    if isinstance(valor, int):
        return 'KIBBLE'
    elif isinstance(valor, float):
        return 'MILK'
    elif isinstance(valor, str):
        return 'TUNA'
    return '¿o.O?'

def p_expression_binop(p):
    '''expression : expression PURR expression
                  | expression HISS expression
                  | expression SCRATCH expression
                  | expression PAW expression
                  | expression NIBBLE expression'''
    
    # Valida que los operandos sean númericos y realiza la operación
    if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):

        if p[2] == 'PURR':
            p[0] = p[1] + p[3]

        elif p[2] == 'HISS':
            p[0] = p[1] - p[3]

        elif p[2] == 'SCRATCH':
            p[0] = p[1] * p[3]

        elif p[2] == 'PAW':
            if p[3] == 0:
                print("(=ＴωＴ=): PAW entre cero")
                p[0] = None
            else:
                p[0] = p[1] / p[3]

        elif p[2] == 'NIBBLE':
            if p[3] == 0:
                print("(=ＴωＴ=): PAW entre cero")
                p[0] = None
            else:
                p[0] = p[1] % p[3]
    else:
        type1 = type_personalized(p[1]) 
        type2 = type_personalized(p[3])
        print(f"(=ＴωＴ=): Operación aritmética no válida entre {type1} y {type2}")
        p[0] = None

def p_expression_number(p):
    '''expression : INTEGER
                  | FLOAT'''
    p[0] = p[1]

# Regla para el operador unario negativo
def p_expression_uminus(p):
    '''expression : MINUS expression %prec UMINUS'''
    p[0] = -p[2]


def p_statement_expression(p):
    '''
    statement : expression
    '''
    p[0] = p[1]
    print(f"Resultado: {p[1]}")


#REGLAS PARA COMPARADORES

def p_comparison(p):
    '''comparison : expression MEOW_MATCH expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression GREATER_EQ expression
                  | expression LESS_EQ expression'''
    
    if p[2] == '->':  # Igualdad
        p[0] = p[1] == p[3]
    elif p[2] == '>>~':  # Mayor que
        p[0] = p[1] > p[3]
    elif p[2] == '~<<':  # Menor que
        p[0] = p[1] < p[3]
    elif p[2] == '>>=':  # Mayor o igual que
        p[0] = p[1] >= p[3]
    elif p[2] == '<<=':  # Menor o igual que
        p[0] = p[1] <= p[3]



variables = {}  # Diccionario global para almacenar variables

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_statement_assignment(p):
    '''
    statement : ID FEED_BOWL expression
    '''
    global in_if_else

    if not in_if_else:
        variables[p[1]] = p[3]  # Asigna el valor de la expresión a la variable
        print(f"Asignación: {p[1]} = {p[3]}")

def p_expression_variable(p):

    '''expression : ID'''

    if p[1] in [f['name'] for f in functions]:
        print(f"(=ＴωＴ=): '{p[1]}' es una función.")
        # Aquí podrías manejar la llamada a la función, por ejemplo, llamando a `call_function(p[1])`
        p[0] = None  # Si es una función, no retorna un valor como variable

    # Si la variable está en el diccionario, asigna su valor, sino da error
    elif p[1] in variables:
        p[0] = variables[p[1]]  # Recupera el valor de la variable
    else:
        print(f"(=ＴωＴ=): Variable '{p[1]}' no definida.")
        p[0] = None  # En caso de error, puedes manejarlo así
        


def p_expression_string(p):
    '''expression : STRING'''
    p[0] = p[1]  # Asignar el valor de la cadena al resultado

def p_statement_declaration(p): #para evitar que se asigne algun tipo de dato a algo que no es.
    '''
    statement : KIBBLE LPAREN ID RPAREN FEED_BOWL expression
              | MILK LPAREN ID RPAREN FEED_BOWL expression
              | TUNA LPAREN ID RPAREN FEED_BOWL expression
    '''

    var_type = p[1]
    var_name = p[3]
    value = p[6]

    # Validación de tipo
    if var_type == 'KIBBLE' and not isinstance(value, int):
        print(f"(=ＴωＴ=): '{var_name}' debe ser KIBBLE.")
    elif var_type == 'MILK' and not isinstance(value, float):
        print(f"(=ＴωＴ=): '{var_name}' debe ser MILK.")
    elif var_type == 'TUNA' and not isinstance(value, str):
        print(f"(=ＴωＴ=): '{var_name}' debe ser TUNA.")
    else:
        variables[var_name] = value
        print(f"Declaración: {var_type} {var_name} = {value}")


#para bloques de código
def p_block(p):
    '''
    block : OPEN_BLOCK statements CLOSE_BLOCK
    '''
    if not p[2]: # si p[2] es none o está vacío
        print("(=ＴωＴ=): El bloque no puede estar vacío.")
        raise SyntaxError("Bloque vacío detectado.")
    else: #bloque con instrucciones
        p[0] = p[2]
        for statement in p[2]:
            if statement is not None:
                print(f"ejecutando instruccion: {statement}")
                

# Regla de statements que maneja un bloque de código vacío
def p_statements(p):
    '''
    statements : statement statements
               | 
    '''
    if len(p) == 1:
        p[0] = []  # Caso vacío
    else:
        p[0] = [p[1]] + p[2]

in_if_else = False # Variable global para controlar si estamos dentro de un if-else

# Regla para `if-else`
def p_statement_if_else(p):
    '''statement : IF_MEOW LPAREN comparison RPAREN block
                 | IF_MEOW LPAREN comparison RPAREN block ELSE_MEOW block'''
    
    # Evaluar la condición, p[3] debería ser un valor booleano (True/False)
    condition = p[3]

    # Verificamos que la condición sea un valor booleano
    if isinstance(condition, bool):  
        if condition:  # Si la condición es verdadera
            print(f"Evaluando condición: {condition}")
            print("Condición verdadera: Ejecutando bloque 'if'")
            # No modificamos p[5], simplemente ejecutamos las instrucciones del bloque
            for statement in p[5]:
                if statement is not None:
                    print(f"Ejecutando instrucción en IF: {statement}")
            # Bloque else no se ejecutará
            p[7] = []  # Vaciamos el bloque `else` si la condición del `if` se cumple

        else:  # Si la condición es falsa
            print(f"Evaluando condición: {condition}")
            print("Condición falsa: Ejecutando bloque 'if' (sin instrucciones)")
            p[5] = []  # Vaciar bloque `if` si la condición es falsa

            if len(p) == 8:  # Si existe un bloque `else`
                print("Ejecutando bloque 'else'")
                # Ejecutar el bloque `else`
                for statement in p[7]:
                    if statement is not None:
                        print(f"Ejecutando instrucción en ELSE: {statement}")
    else:
        print(f"(=ＴωＴ=): Error - La condición no es un valor booleano. Condición: {p[3]}")


# regla para errores de sintaxis
def p_error(p):
    if p:  # Si el token es válido y se detectó un error
        print(f"(=ＴωＴ=): Error de sintaxis cerca de '{p.value}'.")
    else:  # Si no hay token válido (EOF o vacío)
        print("(=ＴωＴ=): Error de sintaxis inesperado al final del archivo.")

    
parser = yacc.yacc(start='program')


data = '''
KIBBLE (x) ~> -6
KIBBLE (y) ~> 3
TUNA (z) ~> "hola"

x PURR y

'''


parser.parse(data)


