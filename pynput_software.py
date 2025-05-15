from pynput.keyboard import Key, Controller
from time import sleep

print("Salut petit farfadet malicieux voulant spam \n")

spam = True

while spam:
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
    
    print("\nHihihihi c'est fait !")
    spam = input("\nOn respam autre chose ? (Y/N) \n").lower() == "y"
