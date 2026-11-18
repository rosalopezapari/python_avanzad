# ejecicio para map()
## recuerde map sirve para transformar todo los elementos 
## Ejercicio 1: Tienes una lista de numeros y quieres obtener una nueva lista con el cubo (elevadoa 3 ) de cada uno 

numeros:list[int]=[1,2,3,4]
map(lambda e:e**3,nueros)

def cubo (e):
    return e**3
map(cubo,numeros)

 
#ejercicio para filter()
##ejercicio 2: Tiene unas lista de temperatura(algunas bajo cero).filtra la lista para quedarte solo con las temperaturaspositivas (mayores a 0 ).

tem:list[int/float]=[-2,10.0,-20,-1,-10,18,23.0]
nueva_temp =list(filter(lemdba t:t>=,temp))
print(f"las temperaturas mayores a cero son:{nueva_temp}")

#ejercicio combinado map() y filter()
## tienes iuna lista de numeros . primero filtra  para quedarte solo con los numetos pares. luego usa, map para multiplicar por 10los numeros pares. 

numero:list[int]=[2,4,6,7,9,12,15,17,18]   
numeros_pares:=list(filter(lambda n:n%2==0,)
       numeros_pares:=list(filter(lambda n:n%2==0,num)             
print(por_diez):list[int]=
print([n*10 for n in num if n%2==0])




