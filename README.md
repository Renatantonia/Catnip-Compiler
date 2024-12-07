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

- *Estructuras lógicas:* Condicionales **(<MEOW>,>MEOW<)**, ciclos **(FOR_TWIRL, WHILE_TWIRL)**, y funciones **(PAWPRINT)**.

***¡Mensajes de error temáticos!:*** Respuestas adorables (pero claras) cuando algo no sale bien.

### 🍣 Tabla de contenidos

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

### Operadores Aritmeticos:

| Operador  | Símbolo   | Descripción               |
|-----------|-----------|---------------------------|
| Suma      | `PURR`    | Suma de dos números.      |
| Resta     | `HISS`    | Resta de dos números.     |
| Multiplicación | `SCRATCH` | Multiplicación de dos números. |
| División | `PAW` | División de dos números. |
| Módulo | `NIBBLE` | Resto de una división. |

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
  PSPS << miFuncion >> [3, 4]
  ```
  
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

  ### 💖CREDITOS:
  Este proyecto fue realizado con cariño por ```Renata Cuello Caquisani```, Vicente Sanchéz, Diego Castro.

