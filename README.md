# CatNip-Compiler
## **(=^-^=) Bienvenido a CatNip (=^-^=)**

CatNip es un lenguaje de programación inspirado en los adorables movimientos y sonidos de los gatos. Este repositorio contiene un compilador para CatLang, creado con Python utilizando las bibliotecas Ply.

***Si amas a los gatos y la programación, ¡este lenguaje está hecho para ti! (=^-^=)***

 ## **🐾 Características principales**

- *Sintaxis amigable:* Comandos que evocan sonidos y acciones de gatos, como ***MEOW, PURR, y PAWPRINT.***

### **Tipos de datos con temática felina:**

- *KIBBLE:* Para enteros.

- *MILK:* Para flotantes.

- *TUNA:* Para cadenas de texto.

- *Estructuras lógicas:* Condicionales, ciclos, y funciones.
  - IF: ```<MEOW>```
  - Else: ```>MEOW<```
  - For: ```@TWIRL```
  - While: ```~TWIRL```
  - Funciones: ```PAWPRINT```

### **Funciones Diversas:**
- Funciones con retorno y sin retorno, ideales para estructurar tu código.
- Soporte para imprimir mensajes usando ```MEOW.```

### **Operadores definidos:**
- Tokens para operadores lógicos (PURR_SYNC, PURR_OR_HISS, HISS_OFF) aunque aún no implementados en el parser.

***¡Mensajes de error temáticos!:*** Respuestas adorables (pero claras) cuando algo no sale bien.

### 🍣 Tabla de contenidos
1. [Requisitos](#Requisitos)
2. [Instalación](#Instalación)
3. [Ejemplo de código](#Ejemplo)
4. [Documentación del lenguaje:](#Documentación)
   - [Tipos de datos](#Tipos)
   - [Variables y como declararlas](#Variables)
   - [Operadores Aritméticos](#Operadores)
   - [Operadores Relacionales](#Operadoresrelacionales)
   - [Operadores Lógicos](#OperadoresLogicos)
   - [Estructuras de control](#Estructuras)
   - [Mensajes de error](#Mensajes)
6. [Creditos](#Creditos)
### Requisitos:

- python 3.8 o superior
- Biblioteca ply (Python Lex-Yacc) Puedes instalarla con:
  ```pip install ply```

### Instalación:

- clona este repositorio: ```git clona "aqui repositorio"```

- navega al directorio: ```cd catnip-compiler```
- Asegurate de tener ply instalado correctamente

### Ejemplo de código:

```
KIBBLE (x) ~> 7
KIBBLE (y) ~> 3
TUNA (saludo) ~> "Hola, CatNip!"

x PURR Y

MEOW (=^-^=) 
```

### **Documentación del lenguaje:**

### *Tipos de datos:*

- `KIBBLE` Enteros
- `MILK` Flotantes
- `TUNA` Cadenas de texto

### *Variables y como declararlas:*
Para declarar una variable se hacer lo siguiente:
1. Colocar el tipo de datos que almacenará la variable.
2. entre parentesis "( )" escoger el nombre para la variable.
3. luego con la sintaxis de asignación ```~>``` asignarle un valor.
```
KIBBLE (variable1) ~> 1
```

### Operadores Aritméticos:

| Operador  | Símbolo   | Descripción               |
|-----------|-----------|---------------------------|
| Suma      | `PURR`    | Suma de dos números.      |
| Resta     | `HISS`    | Resta de dos números.     |
| Multiplicación | `SCRATCH` | Multiplicación de dos números. |
| División | `PAW` | División de dos números. |
| Módulo | `NIBBLE` | Resto de una división. |

### Operadores relacionales:

| Operador  | Símbolo   | Descripción               |
|-----------|-----------|---------------------------|
| Mayor que     | `>>~`  | compara dos números, si uno es mayor que el otro     |
| Menor que     | `~<<`  | compara dos números,si uno es menor que el otro    |
| Mayor o igual | `>>=` | compara dos números, si uno es mayor o igual que el otro |
| Menor o igual | `<<=` | compara dos números, si uno es menor o igual que el otro |
| igual  | `->` | compara si dos números son iguales|

### Operadores Lógicos:

| Operador  | Símbolo   | Descripción               |
|-----------|-----------|---------------------------|
| AND      | `PURR_SYNC`    | Realiza una conjunción lógica: devuelve verdadero solo si ambas expresiones son verdaderas. |
| OR     | `PURR_OR_HISS`   | Realiza una disyunción lógica: devuelve verdadero si al menos una expresión es verdadera.   |
| NOT | `!~` | Realiza una negación lógica: invierte el valor de una expresión booleana. |

** Cabe destacar que también, tiene soporte para realizar operaciones combinadas y que además las resuelva por orden de procedencia **

Ejemplo:
```
4 PURR 5 SCRATCH 3 HISS 1
```
Salida por consola:
```
Resultado: 18
```

### Estructuras de control:

- **Condicionales:**
```
<MEOW> (x -> 7) <.<
    MEOW "x es igual a 7!"
>.>
>MEOW<
    MEOW "x es distinto de 7!"
```
- **Ciclos:**
```
@TWIRL (i ~<< 10) <.<
    MEOW i
>.>
```
### **Funciones:**
Las funciones pueden aceptar distintos parámetros.

- Definir una función:
  ```
  PAWPRINT >> miFuncion << [param1, param2] <.<
    MEOW param1 PURR param2
  >.>
  ```
- LLamar una función:
  ```
  PSPS >> miFuncion << [3, 4]
  ```
- Para retornar algo desde una función con ```CARRYBACK```:
  ```
  CARRYBACK a PURR b
  ```
### **Impresión por consola:**

Usa ```MEOW``` cuando quieras mostrar algún mensaje por consola

- Ejemplo:
  ```MEOW "Bienvenido a CATNIP!!"```

## **Mensajes de error:**

Este compilador ofrece mensajes claros y adorables para ayudar en la depuración:

- *Error sintáctico:* ```(=ＴωＴ=): Error de sintaxis cerca de 'token'.```

- *Operaciones no permitidas:* ```(=ＴωＴ=): Operación no válida entre KIBBLE y TUNA.```

- *Variable no definida:* ```(=ＴωＴ=): Variable 'x' no definida.```

- Validaciones:
  1. Division entre 0:
     ```
     x PAW 0
     (=ＴωＴ=): PAW entre cero no permitido.
     ```
  2. Uso de variables no declaradas:
     ```
     MEOW y
     (=ＴωＴ=): Variable 'y' no definida.

     ```

**Importante** -> Para probar algun código en el compilador se debe ejecutar el archivo yacc.py y colocar primero el codigo en la sección del final en la variable 
```data = ''' (aqui un codigo) ''' ```

  ### 💖CREDITOS:
  Este proyecto fue realizado con cariño por:
  - **Renata Cuello Caquisani.** ```20.949.079-k```
  - Vicente Sánchez. ```19.770.928-6```
  - Diego Castro. ```18.633.660-7```

