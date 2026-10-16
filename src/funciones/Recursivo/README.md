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