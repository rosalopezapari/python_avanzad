# 5. Empaquetado Nominal (**kwargs)
def generar_perfil_usuario(**kwargs) -> str:
    perfil = "Perfil de usuario:\n"
    for clave, valor in kwargs.items():
        perfil += f"- {clave}: {valor}\n"
    return perfil

print("5.", generar_perfil_usuario(nombre="Rosa", edad=19 , pais="Perú", profesion="Estudiante"))