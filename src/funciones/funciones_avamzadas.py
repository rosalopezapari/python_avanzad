### 


def num_pares(a: int, b: int, c: int, d: int, e: int) -> list[int]:
    numeros = [a, b, c, d, e]
    numeros_pares = []
    for i in numeros:
        if i % 2 == 0:
            numeros_pares.append(i)
    return numeros_pares

def suma(a: int, b: int) -> int:
    return a + b

print(suma(3, 4))
print(num_pares(1, 2, 3, 4, 5))

def login(user="",passw=""):
    return "bienvenid l sistema"
print(login(passw="11111", user="hol"))


