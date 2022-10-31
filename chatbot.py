####################################### Imports #######################################
import os
import platform
import random
import urllib.request
from PIL import Image # Para que funcione el módulo PIL hay que hacer pip install pillow en la terminal o en el IDE
urllib.request.urlretrieve(
  'https://i0.wp.com/prevencionsaludproactiv.com/wp-content/uploads/2021/09/desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png?w=509&ssl=1',
   "desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png")
  
img = Image.open("desktop_6637c766-e294-44ce-a7d8-21cb75a04014.png")
random.seed()

####################################### Functions #######################################

# Function to clean the console so its more comfortable to see
def clear():
    #platform.system() This returns "Linux" "Darwin" "Java" or "Windows"
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")

# Asks for specific symptoms and calculates percentages
def addSymptons():
    
    # Function to show the user which symptons he can still add 
    def addableSymptons():
        print("Puedes añadir los siguientes síntomas:")
        for i in range(len(wellRedactedSintomas)):
            if userSymptoms[i] == 0:
                print(wellRedactedSintomas[i].capitalize())

    #Calculates the percentage of each disease    
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
    answer = input(f"Escriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()

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
        answer = input(f"Escriba los síntomas que tenga o pulse enter para salir\nComo por ejemplo: {randomSymptom}\n").lower()

    #Calculates the percentage of each disease
    newpercentages = {}
    percentages = calculatepercentages()

    #Deletes percentages lower than 20%
    for k,v in percentages.items():
        if v > 20:
            newpercentages[k] = v

    # No diseases detected
    if len(newpercentages) <= 0:
        option = input("Ninguna enfermedad se corresponde con los síntomas añadidos\n\
¿Quiere añadir más síntomas? [Y]")
        if option in ["y","Y"]:
                newpercentages = addSymptons()
    return newpercentages

####################################### Variables #######################################

sintomas = [[["dolor"],["leve"]], [["dolor",],["moderadamente"],["intenso"]], [["dolor"],["intenso"]],
            [["dolor"],["insoportable"]],[["retortijones"]],[["dolor"],["colico"]],
            [["dolor"],["punzante"]],[["quemazón"]],[["dolor"],["vago"]],[["dolor"],["comer"]],[["hambre"]],
            [["distensión"]],[["náuseas"]],[["vómitos"]],[["malestar"],["estomacal"]],[["sudoración"]],
            [["taquicardia"]],[["sangre"],["orina"]],[["ardor"],["orina"]],[["dolor"],["orina"]],
            [["sensación","ganas","necesidad"],["imperiosa","imperiosas","constanstes"],["orinar","miccionar","mear"]],
            [["sagre","sangrado"],["heces","excremento","excrementos","oculta"]],
            [["dolor","dolores"],["evacuación","evacuar","evacuacion","excrección","excretar","excrecion","cagar"]],
            [["evacuación","evacuar","evacuacion","excrección","excretar","excrecion"],["incompleta","no completa","inacabada","no acabada"]],
            [["diarrea","descomposición","descomposicion","descompuesto"]],
            [["diarrea","descomposición","descomposicion","descompuesto"],["sangre","sangrado"]],
            [["bulto","protuberancia"],"indolora",["ingle","escroto"]],[["fiebre"]],[["piel amarilla","ictericia"]],
            [["estreñimiento"]],[["pérdida","perder"],["peso"]],[["cansancio","cansado","fatiga","fatigado","agotado","agotamiento"]],
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

ubications = []
newEnfermedades = {}
userSymptoms = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

####################################### Main Program #######################################

# Welcome message
print("Bienvenido a la consulta especializada en dolores abdominales!")

img.show()     
# We ask where the pain is
ubi = input("""Indique la zona del dolor o pulse enter para salir\n
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |\n 
""")


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
print("Con los síntomas que tienes puede que tengas las siguientes enfermedades:")
for i,j in newpercentages.items():
    print(f"{i[:-1]:20}{j:4.02f}%")
