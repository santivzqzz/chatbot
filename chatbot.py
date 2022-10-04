# Crear disccionarios, listas, funciones según se vayan necesitando


# Bienvenida
print("Bienvenido a la consulta especializada en dolores abdominales!"
      
# Preguntamos género del paciente
x = input("Para empezar indique si usted es hombre o mujer: ").lower() # <-- lo ponemos en minúsculas por si el usuario lo escribe mal y que no haya problemas en el programa.

# Preguntamos ubicación del dolor

ubi = input("""Indique la zona del dolor\n
| ai | am | ad |
----------------
| mi | mm | md |
----------------
| ai | am | ad |\n 
""")
      
# A partir de aqui comprobamos en que zona es el dolor o molestia para descartar cosas
