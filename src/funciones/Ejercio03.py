# 3. Type-hints (Anotaciones de tipo)
def obtener_promedio(numeros: list[int]) -> float:
    return sum(numeros) / len(numeros) if numeros else 0.0

print(f"3. Promedio: {obtener_promedio([10, 20, 30])}")

