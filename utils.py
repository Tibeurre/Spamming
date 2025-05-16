from pynput.keyboard import Key, Controller
from time import sleep 
import os

def spam():
    message = input("Quel message veux-tu spammer ? \n")
    amount = int(input("\nCombien de fois veux-tu spammer ? \n"))
    preparation = int(input("\nCombien de secondes veux-tu avant de commencer à spammer ? (attention, dès que tu appuyes sur Entrée c'est parti mon coquin) \n"))

    print("LETS GOOOOOOOOOO")

    keyboard = Controller()

    sleep(preparation)

    for _ in range(amount):
        sleep(0.5)
        keyboard.type(message)
        keyboard.press(Key.enter)

    return

def texte():

    #List the files in the scripts directory and attribut them indexes
    index = 0
    files = {}
    print("\nLes scripts suivants sont disponibles :")
    for fichier in os.listdir("./scripts"):
        if fichier.endswith(".txt"):
            files[index] = fichier
            index += 1
            print(f"{index}. {fichier}")
    
    #access the file
    while True:
        script = int(input("\nLequel veux-tu déblatérer ? (juste le numéro) \nTa réponse : "))
        script = "./scripts/"+files[script-1]
        if os.path.isfile(script):
            break
        else:
            print("\nIl existe pas ce fichier frérot, fais un effort ! (CTRL+C pour quitter si tu t'es plantatouillé)")

    #getting the waiting time
    preparation = int(input("\nCombien de secondes veux-tu avant de commencer à spammer ? (attention, dès que tu appuyes sur Entrée c'est parti mon coquin) \n"))

    print("\nLETS GOOOOOOOOOO")

    sleep(preparation)

    #opening the file and typing it
    keyboard = Controller()

    with open(script, "r", encoding="utf-8") as fichier:
        for line in fichier:
            sleep(0.5)
            keyboard.type(line.strip())
            keyboard.press(Key.enter)