# 4. Empaquetado posicional (*args)
def unir_frases(*args: str) -> str:
 )  return " ".join(args)

print(f"4. Frases: {unir_frases('Hola', 'Rosa,', 'es', 'su', 'Cumple')}")
