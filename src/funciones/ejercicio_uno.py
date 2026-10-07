# crear un programa que me permita desarrollar las 4 opoeraciones basica
# (suma, resta, division, multiplicacion)

def suma(a:int,b:int):
    return a + b

def resta(a:int,b:int):
    return a - b

def multiplicacion(a:int,b:int):
    return a * b

def division(a:int,b:int):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b

def calculadora():
    print("=== CALCULADORA PYTHON AVANZADO ===")
    try:
        numero1 = float(input("Ingresa el primer numero: "))
        numero2 = float(input("Ingresa el segundo numero: "))
        
        print(f"\nSuma: {numero1} + {numero2} = {suma(numero1, numero2)}")
        print(f"Resta: {numero1} - {numero2} = {resta(numero1, numero2)}")
        print(f"Multiplicacion: {numero1} * {numero2} = {multiplicacion(numero1, numero2)}")
        print(f"Division: {numero1} / {numero2} = {division(numero1, numero2)}")
    except ValueError:
        print("Error: ingresa solo numeros")

# Ejecutar
if __name__ == "__main__":
    calculadora()