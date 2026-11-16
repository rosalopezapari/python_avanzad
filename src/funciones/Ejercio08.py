
# 8. Closure (Clausura)
def crear_validador_limite(limite_maximo: int):
    def validador(numero: int) -> bool:
        return numero <= limite_maximo
    return validador

validador_100 = crear_validador_limite(100)
print(f"8. 50 <= 100 {validador_100(50)}")
print(f"8. 150 <= 100 {validador_100(150)}")