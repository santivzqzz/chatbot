# Crear diccionarios, listas, funciones según se vayan necesitando
enfermedades = {"Cálculos biliares":[1,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0]}
# Bienvenida
print("Bienvenido a la consulta especializada en dolores abdominales!")
      

# Preguntamos ubicación del dolor

ubi = input("""Indique la zona del dolor\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")
      
# Con esto descartamos todas las enfermedades que no son:
newEnfermedades = enfermedades.copy()
for enfermedad in enfermedades:
    if ubi != str(enfermedades[enfermedad][0]):
        del newEnfermedades[enfermedad]

print(newEnfermedades)
