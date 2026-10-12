# funciones en python 
necesario .
``` python 
# ejemplo deseamos un programa en python quenos permite sumar dos numeros 
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma :int=numero_uno+numero_dos
suma :int=numero_tres+numero_cuatro
print(suma_dos)

como hacemos reutilizable el ejercicio anterior

para eso utilizaremos funciones .
la caracteristica de una funcion en python es la siguente :
1. debe comenzar con la palabra reservada
`def`.
2. debe tener un nombre que de a entender que realizara la funcion.
3. debera tener parametros y estos estaran encerrados rn parentesis `()`.no todas las funciones resibiran parametros aun asi debera tener los `()`
4. las funciones deberan retornar datos a travez de la palabra reservada `return`

```python 
# crear un programa que me permite sumar dos numeros
def sumar (a:int,b:int):
    return a+b
    
    print(sumar (78,56))
    print(sumar(45,5))



 ```
 # funciones avanzadas 
 **Argumento**
 es el datos
 **nota**
  en ambos casos tenemos posicionales/nominales
  ```python 
  # parametros 
  def suma(a,b):#en este caso tenemos una funcion suma que recibe dos parametros a,b 
  suma (34,45)
  # ene ste caso estpy llamndo a la funcion pasandple como argimentos los datos .
  #  en este caso caso en concreto podemos decir que estamos frente a una funciopn que tiene parametros posicionales , eso significa que cada valor remplaza en el orden  que le pasemos a lñas variables, 34->an , 45->b

  def login(usuario="",password=""):
    return "acceso correcto"
    login(password=12345678",usuario="tupapo")

# esta fincion e as una fincion nominalporque  para pasar los valores tengo que indicar la variable 

  ```
