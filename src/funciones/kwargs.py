# crear una funcion que me permita saner de una lista de ingredientes cual es el de mayor precio 
# ejemplo:
# entrada: ajo=2, papa=3, aceite=8
# salida: el ingrediente de mayor precio es aceite 

# Debemos crear una función que permita encontrar el ingrediente con mayor precio.

def ingrediente_mayor_precio(**kwargs):
    # **kwargs = {clave: valor}

    precio_maximo = 0

    for ingrediente, precio in kwargs.items():
        if precio > precio_maximo:
            precio_maximo = precio
            ingrediente_mayor = ingrediente

    return f"El ingrediente de mayor precio es {ingrediente_mayor}"

print(ingrediente_mayor_precio(ajo=2, papa=3, aceite=8))   
.