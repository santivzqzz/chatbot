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
        print("Puedes añadir los siguientes síntomas:")
        for i in range(len(wellRedactedSintomas)):
            if userSymptoms[i] == 0:
                time.sleep(0.1)
                print(wellRedactedSintomas[i].capitalize())

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
    answer = input(f"\nEscriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()

    while answer != "":
        symptomsAdded = [] #Lista para avisar al usuario el sintoma que ha introducido
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
            option = input("No sé detectó ningún síntoma no nombrado anteriormente\n¿Quiere ver todos los posibles síntomas para añadir? [Y] ")
            if option in ["y","Y"]:
                addableSymptons()

        else:
            print("Has añadido los siguientes síntomas:")
            for i in symptomsAdded:
                print(i.capitalize())
        input("Pulse enter para continuar... ")
        clear()
        randomSymptom = random.choice(wellRedactedSintomas)
        answer = input(f"\nEscriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()
    
    # Calcula porcentajes
    newpercentages = {}
    percentages = calculatepercentages()    

    # Elimina las enfermedades que estén por debajo de un 20% de posibilidades
    for k,v in percentages.items():
        if v > 20:
            newpercentages[k] = v

    # Dar la opción de seguir preguntando si no encuentra ninguna enfermedad
    if len(newpercentages) <= 0:
        option = input("Ninguna enfermedad se corresponde con los síntomas añadidos\n\
¿Quiere añadir más síntomas? [Y]")
        if option in ["y","Y"]:
                newpercentages = addSymptons()
    return newpercentages

####################################### Variables #######################################
        
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

# This transforms all number into integers because they were strings coming from the file
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
print("Bienvenido a la consulta especializada en dolores abdominales!")
print("A continuación le haremos unas preguntas para hacer una evalución de las posibles enfermedades que podría presentar")
time.sleep(3)


#Simple questions about the desease
tiempo_enf=input("Cuanto tiempo lleva padeciendo el dolor?\n")


while tiempo_enf=="":
   tiempo_enf=input("Tiempo no valido porfavor intoduzca el tiempo que lleva padeciendo el dolor nuevamente\n ")
else:
    time.sleep(1)
evolucion=input("Han empeorado los sintomas desde hace "+tiempo_enf+"?\n")
while evolucion=="":
        print("Porfavor responda la pregunta con un si o un no")
        evolucion=input("Han empeorado los sintomas desde hace "+ tiempo_enf +"?\n")
else:
    if evolucion=="si" or evolucion=="Si":
        print("Si su dolor empeora rápidamente debe visitar un médico con urgencia")
        
    if evolucion=="no" or evolucion=="No":
              print("Si sus sintomas son constantes y no cesan debería pedir una cita médica")

time.sleep(3)

   
# Pregunta la zona del dolor o molestia
print("""Indique la zona del dolor o pulse enter para salir\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 | 
""")
img.show()
ubi=input("")
if ubi == "":
    clear()
    print("Programa finalizado.")
    time.sleep(1.5)
    clear()
    exit()

# We add to the list (ubications) the zone(s) where the patient feels pain
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

#We create a new dict where we only save the diseases that are possible on the zone the patient feels pain
for i in enfermedades:
    if i[-1] in ubications:
        newEnfermedades[i] = enfermedades[i]
clear()

#We erase the dictionary because we don't need it anymore
enfermedades.clear()

# Main function
newpercentages = addSymptons()

#Shows the percentage
if len(newpercentages) == 0:
    print("No ha introducido ningún dato válido...\nPrograma finalizado.")

else:
    print("Con los síntomas que tienes puede que tengas las siguientes enfermedades:")
    # Comprueba que no se repita la misma enfermedad más de una vez
    temp=[]
    res_final={}
    for i in newpercentages.keys():
        if f"{i[:-1]}" not in temp:
            temp.append(f"{i[:-1]}")
            res_final.update({i:newpercentages[i]})


    for i,j in res_final.items():
        print(f"{i[:-1]:20}{j:4.02f}%")
        
