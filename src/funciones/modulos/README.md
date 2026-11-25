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
## 3.importar solo lo necesario (from ... import )
aveces es necesario  importar  solo una partes especificadas de un modulo. para esto usamos ´from nombre_modulo import parte_especifica´

´matematicas.py´

```python 
def resta (a,b):
    returna-*b
    def suma(a,b)
    return a+b
    PI=3.1415

```
´main.py´
```python 
from matematicas import PI

```

## PANQUETES (Carpetas de modulos)
cuando el proyecto empieza a crecer los modulos de ordenan en carpeta  