# 9. Programacio funcional (map())
precios: list[float] = [10.5, 20.0, 50.0, 5.99]
precios_incrementados = list(map(lambda p: p * 1.10, precios))
print(f"9. Precios +10%: {precios_incrementados}")