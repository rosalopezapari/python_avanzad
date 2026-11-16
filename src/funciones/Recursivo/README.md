### Recursividad en python
La recursividad en Python es una técnica de programación en la que una función se llama a sí misma para resolver un problema, dividiéndolo en problemas más pequeños.
# definicion 
Una función recursiva tiene dos partes fundamentales:

Caso base: condición que detiene las llamadas recursivas.

Caso recursivo: parte donde la función se llama a sí misma.
# ejemplos en codigo
```python
def funcion_recursiva(n)
    if n== 0:       Caso base
   return
    else: Caso recursivo
    funcion_recursiva(n - 1)

    2.
    def cuenta_regresiva(n):
    if n == 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(5)
```

```python

## conociendo mas sobre funciones parametros y argumentos
sobre los parametros/ argumentos nominales es ampliamente usuando para distints configuraciones y que se puede pasar solo los argumentos que se usaran y dejar los parametros por defecto si no se va a modificar 

# tenemos un programa que me permite acceder a internet que tiene parmitir por defecto, sin embargo si se actualiza uno de los 
# primer caso accesos por defecto  
def config(a:int ,b,h)

def config(user="admin",pass="1234",port="80808",BSSID="wifi"):
    return "conectado a la red" 

    config (BSSID="LABORATORIO1")

    ## reyner desea conectar al wifi de ana luz , entos reyner le pregunta como se llama tu wifi y cual es la contraseña. respuesta le dice  el wifi es A56  Y SU CONTRASEÑA ES 12345678

    def config(user="admin",pass="1234",port="80808",BSSID="wifi"):
    return "conectado a la red" 

    config(BSSID="A56",pass="12345678")
```


### conociendo **kargs (empaquetado y desempaquetado de argumentos posicionales)
esta tecnica mnos permite empaquetas nuestros argumentos cuando no sabemos la cantidad de dastos que vamos a pasar . imaginemos que nos pide una funcion dentro de los parametros debemos usar el operador `*` delante  del nombre del parametro posicional esto hara que todod los argumentos se almacen en una tupla (lista)esto  nos permite recorer dentro de sus elementos para poder desempleo y realizar las operciones necesarias.

```python
# deseams crear una funcion que nos permita sumar n cantidad de numeros 
# n es un numero variable puede ser 3, 7, 8, ........n
def suma(*args):
    #*args = (2,5,7,8,9)
    acumulado=0
    for i in args:
        acumulado =+ i
        return acumulado
        print (suma(2,5,7,8,9))


      
```

#### desempaquetando argumentos nominales 
en es caso como en el anterio utilizaremos el operador  `*`

```python
#debems crear unas funcion que me permita saber encontrar la persona conn mayor calificacion.
def mejor_alumnos (**kwargs):
    #**kwargs={clave:valor}
    for alumnom,nota in kwargs.items():
        if nota > nota_maxima:
            nota_alumno = alumno 
            return mejor_alumno
            mejor_alumno(noemi=20,eduardo=18,david=19)



```

        ## Porgramacion funcional 
        python en su lenguaje de programacion multiparadigmas que mejor funcion tiene es la 'funcional'.
        python uas tres 'map()','filter()','reduce()', pero nosotros solousaremos 'map()','filter()'. esats funciones integradas de python sirven para procesar y tranformar collecciones de datos (listas,diccionarios) de manera muy eficiente: 
        [!tip] Importante: 
        las funciones 'map()','filter()' resiven dos parametros primer laa funcion a ejecutar y un segundo el iterable en que va ejecutar. la funcion que recive como parametro puede ser normal ('def') o puede ser anonima 'lambda'

        ### 1. map()
        map aplica una funcion especifica cada uno de ls elementos de una colleccion(iterable) y devuelve un nuevo iterable con los resultados. 


```python

de una lista de numeros enteros deseamos calcular la potencia 2 de cada numero
numero:list[int]=[2,4,6,8,7]
## cuando queremos trabajar con una funcion anonima tenemos que declarar primero la funcion antes de pasarla por parametro 
def  f(x):
    return x**2,
    ## cuando desseamos trtabajr con funciones anonimas usamos lambda dentro del parametro 
    map(lambda x:x**2,numeros)

```
### 2. filter()
Filter pasa cada elemento de una coleccion por una funcion y solo se queda con aquellos elementos donde la funcion devuelve True (es decir, filtrar los datos segun una condicion).

```python
## imag que tienes una lista de numeros y solo quioeres quedarte con los numeros pares.
numeros:list[int]=[2,7,20,4,3,9,11,16,17]
filter(Lamdba n:n % 2 ==0,numeros)

```
> [WARNING] Nota importante 
> Tanto 'map()'como 'filter()' no devuelven listas directamente listas directamente ,sino iteradores. Esto es para ahorrarmemoria(evaluacion perezosaao lazy evaluation). si quieres  ver el resultado como una ista tradicional siempre debes envolver en 'lñist()'.

