# 2 Parametros nominales y por defecto

def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
    return precio * (1 + impuesto - descuento)

# Uso con argumento nominal: solo descuento 5%, impuesto por defecto 18%
precio_final = calcular_precio_final(100, descuento=0.05)
print(f"2. Precio final con 5% dscto: {precio_final}"