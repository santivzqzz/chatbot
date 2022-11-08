####################################### Imports #######################################
import os
import platform
import random
import csv
import time
import urllib.request
from PIL import Image # Para que funcione el módulo PIL hay que hacer pip install pillow en la terminal o en el IDE
urllib.request.urlretrieve(
  'https://i0.wp.com/prevencionsaludproactiv.com/wp-content/uploads/2021/09/desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png?w=509&ssl=1',
   "desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png")
  
img = Image.open("desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png")
random.seed()

####################################### Functions #######################################


def print2(text):
    for n,char in enumerate(text):
        if n == len(text)-1:
            print(char)
        else:
            print(char,end="")
        time.sleep(random.uniform(0.01,0))

def input2(text):
    for char in text:
        print(char,end="")
        time.sleep(random.uniform(0.01,0))
    return input()


# Función para limpiar la consola
def clear():
    #platform.system() This returns "Linux" "Darwin" "Java" or "Windows"
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")

# Pregunta por síntomas y calcula porcentajes
def addSymptons():
    
    # Le enseña al usuario los síntomas que puede añadir 
    def addableSymptons():
        print2("Puedes añadir los siguientes síntomas:")
        for i in range(len(wellRedactedSintomas)):
            if userSymptoms[i] == 0:
                time.sleep(0.1)
                print2(wellRedactedSintomas[i].capitalize())

    # Calcula el porcentaje de la posible enfermedad    
    def calculatepercentages():
        percentages = {}
        for i in newEnfermedades:
            percentage = 0
            for j in range(len(userSymptoms)):
                if newEnfermedades[i][j] == userSymptoms[j] and userSymptoms[j] == 1:
                    percentage += 85/(newEnfermedades[i]).count(1)
                elif newEnfermedades[i][j] == userSymptoms[j] and userSymptoms[j] == 0:
                    percentage += 10/(newEnfermedades[i]).count(0)
                percentages[i] = percentage
        return percentages

    randomSymptom = random.choice(wellRedactedSintomas)
    answer = input2(f"Escriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()

    while answer != "":
        symptomsAdded = [] #Lista para avisar al usuario el sintoma que ha introducido
        for v in answer.split():
            if v in restricted_words:
                clear()
                input2("Intente no hacer negaciones a la hora de introducir los síntomas.\nPulse enter para continuar...")
                clear()
                break
                
            for i in range(len(sintomas)):
                counter = 0
                for j in range(len(sintomas[i])):
                    for k in range(len(sintomas[i][j])):
                        if sintomas[i][j][k] in answer:
                            counter += 1
                            break
                if counter == len(sintomas[i]) and userSymptoms[i] == 0:
                    userSymptoms[i] = 1
                    symptomsAdded.append(wellRedactedSintomas[i])

            if len(symptomsAdded) == 0:
                option = input2("No sé detectó ningún síntoma no nombrado anteriormente\n¿Quiere ver todos los posibles síntomas para añadir? [Y] ")
                if option in ["y","Y"]:
                    addableSymptons()

            else:
                print2("Has añadido los siguientes síntomas:")
                for i in symptomsAdded:
                    print2(i.capitalize())
            input2("Pulse enter para continuar... ")
            clear()
            randomSymptom = random.choice(wellRedactedSintomas)
            break
        answer = input2(f"Escriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()
            
    # Calcula porcentajes
    newpercentages = {}
    percentages = calculatepercentages()    

    # Elimina las enfermedades que estén por debajo de un 20% de posibilidades
    for k,v in percentages.items():
        if v > 20:
            newpercentages[k] = v

    # Dar la opción de seguir preguntando si no encuentra ninguna enfermedad
    if len(newpercentages) <= 0:
        option = input2("Ninguna enfermedad se corresponde con los síntomas añadidos\n\
¿Quiere añadir más síntomas? [Y]")
        if option in ["y","Y"]:
                newpercentages = addSymptons()
    return newpercentages

####################################### Variables #######################################
restricted_words=["no", "ni", "carezco", "ausencia"]       
ubications = []
wellRedactedSintomas = []
enfermedades = {}
newEnfermedades = {}

with open("enfermedades.csv","r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    wellRedactedSintomas = reader.fieldnames[1:]    
    for row in reader:
        enfermedad = row["Enfermedad"]
        row.pop("Enfermedad")
        enfermedades[enfermedad] = list(row.values())

# Transforma todos los numeros a entero porque se leen como str desde el archivo csv
for disease in enfermedades:
    enfermedades[disease] = [int(x) for x in enfermedades[disease]]

userSymptoms = [0 for x in wellRedactedSintomas]

sintomas=[]
with open("sintomas.csv","r", encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        line = []
        for i in row:
            if ";" in i:
                line.append(i.split(";"))
            else:
                line.append([i])
        sintomas.append(line)

####################################### Main Program #######################################
clear()
# Mensaje bienvenida
print2("Bienvenido a la consulta especializada en dolores abdominales!")
   
# Pregunta la zona del dolor o molestia
print("""Indique la zona del dolor o pulse enter para salir\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 | 
""")
#img.show()
ubi=input("")
if ubi == "":
    clear()
    print2("Programa finalizado.")
    time.sleep(1.5)
    clear()
    exit()

# Añadimos a la lista (ubications) la(s) zona(s) donde el usario indica la molestia
while ubi != "" or len(ubications) == 0:
    if ubi.isnumeric() and (ubi not in ubications) and (1 <= int(ubi) <= 9):
        ubications.append(ubi)
    clear()
    ubi = input("""Si le duele en otra zona, indíquelo o pulse enter para salir\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")

# Crea un diccionario nuevo donde solo se almacenan las emfermedades posibles por cuadrante
for i in enfermedades:
    if i[-1] in ubications:
        newEnfermedades[i] = enfermedades[i]
clear()

# Eliminamos el diccionario porque ya no lo necesitamos
enfermedades.clear()

# Función principal del código
newpercentages = addSymptons()

# Muestra (o no) los porcentajes de cada enfermedad
if len(newpercentages) == 0:
    print2("No ha introducido ningún dato válido...\nPrograma finalizado.")

else:
    print2("Con los síntomas que tienes puede que tengas las siguientes enfermedades:")
    # Comprueba que no se repita la misma enfermedad más de una vez
    temp=[]
    res_final={}
    for i in newpercentages.keys():
        if f"{i[:-1]}" not in temp:
            temp.append(f"{i[:-1]}")
            res_final.update({i:newpercentages[i]})


    for i,j in res_final.items():
        print2(f"{i[:-1]:20}{j:4.02f}%")
