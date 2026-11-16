# 7. Documentación (deocstring)
def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número.

    Esta función eleva la base a la potencia del exponente.

    Args:
        base (float): El número base que se va a elevar.
        exponente (float): El exponente al que se eleva la base.

    Returns:
        float: El resultado de base elevado a exponente.
    """
    return base**exponente

print(f"7. Potencia: {calcular_potencia(2, 3)}")