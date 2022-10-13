import os
import platform
import random
from PIL import Image # Para que funcione el módulo PIL hay que hacer pip install pillow en la terminal o en el IDE
im = Image.open(r"C:\Users\santi\OneDrive\Escritorio\abd.jpg") # Poner el directorio donde se encuentra la imagen
random.seed()
#platform.system() This returns "Linux" "Darwin" "Java" or "Windows"

# Function to clean the console so its more comfortable to see
def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")

clear()

sintomas = [["dolor","leve"], ["dolor","moderadamente","intenso"], ["dolor","intenso"],
            ["dolor","insoportable"],["retortijones"],["dolor","colico"],
            ["dolor","punzante"],["quemazón"],["dolor","vago"],["dolor","comer"],["hambre"],
            ["distensión"],["náuseas"],["vómitos"],["malestar","estomacal"],["sudoración"],
            ["taquicardia"],["sangre","orina"],["ardor","orina"],["dolor","orina"],
            [["sensación","ganas","necesidad"],["imperiosa","imperiosas","constanstes"],["orinar","miccionar","mear"]],
            [["sagre","sangrado"],["heces","excremento","excrementos","oculta"]],
            [["dolor","dolores"],["evacuación","evacuar","evacuacion","excrección","excretar","excrecion","cagar"]],
            [["evacuación","evacuar","evacuacion","excrección","excretar","excrecion"],["incompleta","no completa","inacabada","no acabada"]],
            [["diarrea","descomposición","descomposicion","descompuesto"]],
            [["diarrea","descomposición","descomposicion","descompuesto"],["sangre","sangrado"]],
            [["bulto","protuberancia"],"indolora",["ingle","escroto"]],["fiebre"],[["piel amarilla","ictericia"]],
            ["estreñimiento"],[["pérdida","perder"],"peso"],[["cansancio","cansado","fatiga","fatigado","agotado","agotamiento"]],
            [["saciado","saciedad"]]]

wellRedactedSintomas = ["dolor leve", "dolor moderadamente intenso", "dolor intenso",
            "dolor insoportable","retortijones","dolor cólico",
            "dolor punzante","quemazón","dolor vago","dolor al comer","sensación de hambre",
            "distensión","náuseas","vómitos","malestar estomacal","sudoración",
            "taquicardia","sangre en la orina","ardor al orinar","dolor al orinar",
            "sensación imperiosa de orinar","sagre en las heces","dolor en la evacuación",
            "evacuación incompleta","diarrea","sangre en la diarrea",
            "protuberancia indolora en la ingle y en el escroto","fiebre","ictericia",
            "estreñimiento","pérdida de peso","cansancio","saciedad"]


userSymptoms = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
percentages = {}

enfermedades = {"Cálculos biliares1":[0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                 "Hepatitis1":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0],
                 "Pancreatitis1":[0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Úlcera duodenal1":[1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Cálculos biliares2":[0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Gastritis2":[0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Gastrointeritis2":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Hepatitis2":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0],
                 "Pancreatitis2":[0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Úcera estomacal2":[1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
                 "Pancreatitis3":[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Úcera duodenal3":[1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Cálculos biliares4":[0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Cálculos renales4":[0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                 "Estreñimiento4":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
                 "Gastrointeritis4":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Hepatitis4":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0],
                 "Apendicitis5":[1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Gastroenteritis5":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                  "Hernia umblical5":[0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  "Pancreatitis5":[0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                  "Úlcera estomacal5":[1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
                  "Cálculos renales6":[0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                 "Colitis6":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],
                 "Diverticulitis6":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                 "Fecaloma6":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
                 "Gastroenteritis6":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Apendicitis7":[0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Enfermedad Pelvica7":[0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Estreñimiento7":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
                 "Hernia inguinal7":[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                 "Apendicitis8":[0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Cálculos renales8":[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                 "Diverticulitis8":[1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0],
                 "Enfermedad Pelvica8":[0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Infección de orina8":[0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                 "Colitis9":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
                 "Diverticulitis9":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                 "Enfermedad Pelvica9":[0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                 "Fecaloma9":[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
                 "Gastroenteritis9":[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                 "Hernia inguinal9":[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]}

# Welcome message
print("Bienvenido a la consulta especializada en dolores abdominales!")

im.show()     
# We ask where the pain is
ubi = input("""Indique la zona del dolor\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")

ubications = []

# We add to the list (ubications) the zone(s) where the patient feels pain
while ubi != "" or len(ubications) == 0:
    if ubi.isnumeric() and (ubi not in ubications) and (1 <= int(ubi) <= 9):
        ubications.append(ubi)
    clear()
    ubi = input("""Si le duele en otra zona, indíquelo\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")

#We create a new dict where we only save the diseases that are possible on the zone the patient feels pain
newEnfermedades = {}
for i in enfermedades:
    if i[-1] in ubications:
        newEnfermedades[i] = enfermedades[i]
clear()


#We ask for specific symptoms
randomSympton = random.choice(wellRedactedSintomas)
answer = input(f"Escriba los síntomas que tenga\nComo por ejemplo: {randomSympton}\n").lower()
clear()
while answer != "":
    for i in range(len(sintomas)):
        counter = 0
        for j in range(len(sintomas[i])):
            if sintomas[i][j] in answer:
                counter += 1
        if counter == len(sintomas[i]):
            userSymptoms[i] = 1
    randomSympton = random.choice(wellRedactedSintomas)
    answer = input(f"Escriba los síntomas que tenga\nComo por ejemplo: {randomSympton}\n")
    clear()
    

#Calculates the percentage of each disease
for i in newEnfermedades:
    percentage = 0
    for j in range(len(userSymptoms)):
        if newEnfermedades[i][j] == userSymptoms[j]:
            percentage += 100/len(userSymptoms)
        percentages[i] = percentage

print(percentages)
