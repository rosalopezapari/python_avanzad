# Modularidad
la ´modularidad´  consiste en divir un programa grande en archivo pequeños  y reutilizables llamados ´modulos´. Cada modulo es simplemente un archivo ´.py´ 
**ventajas:**  
-´reutilizacion:´ escribe  el codigo una vez y lo usas en muchos programas .
´mantenimiento:´ es mas facil encontar y corregir errores.
- ´trabajo en equipo:´cada persona puede desarrollara su propio mudulo .

## 1. crear un modulo 
Basta con crear un archivo con la extencion con la eextencion ´.py´ por ejemplo ´matematicas.py´. 
##2. importar un modulo  completo 
la manera de como reutilazremos los modulos es haciendo de la palabra reservada ´import´ esto se debera declarar en el archivo don de reutilazremos ciertas funciones o variables de un modulo para importar un modulo completo usamos n´impo0rt´ 
´nombre_archivo´.

´matematicas.py´

```python 
def suma(a,b)
return a+b 
def resta (a,b)
return  a-b

```
´´main.py
```python
import matematicaas 
## para hacetr uso de las funciones tengo que acceder al archivo luego un punto y el nhombre del dato, funcion que der 
matematicas.re4sta(5,8)
```
