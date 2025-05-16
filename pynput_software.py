import utils


spam = True

while spam:
    print("-------------------------------Start-------------------------------\n")
    todo = input("Que veux-tu faire petit farfadet malicieux ? \n 1. Spam un message \n 2. Déblatérer un texte  \n 3. Quitter \nTon choix : ")

    if todo == "1":
        utils.spam()
    elif todo == "2":
        utils.texte()
    else:
        break
    
    print("\nHihihihi c'est fait !")
    spam = input("\nOn respam autre chose ? (Y/N) \n").lower() == "y"

print("A la prochaine mon minot;)\n")