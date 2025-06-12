from pynput.keyboard import Key, Controller, KeyCode
from pynput import keyboard
from time import sleep 
import os
from copy import deepcopy
import customtkinter as ctk
from PIL import Image
import win32clipboard
from io import BytesIO

def start_spam(preparation, amount, message, app):
    global label_countdown
    amount, preparation = int(amount), int(preparation)

    frame_decompte = ctk.CTkFrame(app)
    frame_decompte.pack(pady=20, padx=20, fill="both", expand=True)

    label_countdown = ctk.CTkLabel(frame_decompte, text=f"{preparation}", font=ctk.CTkFont(size=50, weight="bold"))
    label_countdown.pack(pady=20)

    frame_decompte.pack(fill="both", expand=True)

    countdown(preparation, amount, message, app, frame_decompte)


def countdown(preparation, amount, message, app, frame_decompte):
    if preparation > 0:
        label_countdown.configure(text=f"{preparation} ...")
        app.after(1000, countdown, preparation - 1, amount, message, app, frame_decompte)
    else:
        label_countdown.configure(text="On spammmm ! 🚀")
        # laisse le texte s'afficher pendant 1s avant de spammer
        app.after(1000, lambda: start_spam_after_message(message, amount, app, frame_decompte))


def start_spam_after_message(message, amount, app, frame_decompte):
    frame_decompte.pack_forget()
    spam(message, amount, app)
    

def spam(message=None, amount=None, app=None):
    # message = input("\nQuel message veux-tu spammer ? \n")
    # amount = int(input("\nCombien de fois veux-tu spammer ? \n"))
    # preparation = int(input("\nCombien de secondes veux-tu avant de commencer à spammer ? (attention, dès que tu appuyes sur Entrée c'est parti mon coquin) \n"))

    # print("LETS GOOOOOOOOOO"))

    keyboard = Controller()

    for _ in range(amount):
        ecriture(keyboard, message, app)
    return

def ecriture(keyboard, message, app):
    app.after(500, lambda: (
        keyboard.type(message),
        keyboard.press(Key.enter)
    ))

def start_txt(filename, preparation, app):
    global label_countdown
    preparation = int(preparation)

    frame_decompte = ctk.CTkFrame(app)
    frame_decompte.pack(pady=20, padx=20, fill="both", expand=True)

    label_countdown = ctk.CTkLabel(frame_decompte, text=f"{preparation}", font=ctk.CTkFont(size=50, weight="bold"))
    label_countdown.pack(pady=20)

    frame_decompte.pack(fill="both", expand=True)

    countdown_txt(filename, preparation, app, frame_decompte)

def countdown_txt(filename, preparation, app, frame_decompte):
    if preparation > 0:
        label_countdown.configure(text=f"{preparation} ...")
        app.after(1000, countdown_txt, filename, preparation-1, app, frame_decompte)
    else:
        label_countdown.configure(text="On spammmm ! 🚀")
        # laisse le texte s'afficher pendant 1s avant de spammer
        app.after(1000, lambda: start_txt_after_message(filename, app, frame_decompte))

def start_txt_after_message(filename, app, frame_decompte):
    frame_decompte.pack_forget()  # ou .destroy() si tu veux vraiment le supprimer
    from_txt(filename, app)

def from_txt(filename, app):
    keyboard = Controller()
    
    with open(filename, "r", encoding="utf-8") as fichier:
        lines = [line.strip() for line in fichier]

    def typer_ligne(index=0):
        if index < len(lines):
            keyboard.type(lines[index])
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            app.after(500, typer_ligne, index + 1)

    # On attend 'preparation' secondes (converties en ms) avant de commencer
    app.after(1000, typer_ligne)

def start_img(filename, preparation, amount, app):
    global label_countdown
    preparation = int(preparation)

    frame_decompte = ctk.CTkFrame(app)
    frame_decompte.pack(pady=20, padx=20, fill="both", expand=True)

    label_countdown = ctk.CTkLabel(frame_decompte, text=f"{preparation}", font=ctk.CTkFont(size=50, weight="bold"))
    label_countdown.pack(pady=20)

    frame_decompte.pack(fill="both", expand=True)

    countdown_img(filename, preparation, amount, app, frame_decompte)

def countdown_img(filename, preparation,  amount, app, frame_decompte):
    if preparation > 0:
        label_countdown.configure(text=f"{preparation} ...")
        app.after(1000, countdown_img, filename, preparation-1, amount, app, frame_decompte)
    else:
        label_countdown.configure(text="On spammmm ! 🚀")
        # laisse le texte s'afficher pendant 1s avant de spammer
        app.after(1000, lambda: start_img_after_message(filename,  amount, app, frame_decompte))

def start_img_after_message(filename, amount, app, frame_decompte):
    frame_decompte.pack_forget()  # ou .destroy() si tu veux vraiment le supprimer
    from_img(filename, amount, app)

def from_img(filename, amount, app):
    keyboard = Controller()
    image_to_clipboard(filename)

    def spam_loop(index=0):
        if index < amount:
            keyboard.press(Key.ctrl)
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release(Key.ctrl)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            app.after(500, spam_loop, index + 1)
        else:
            # ✅ Ceci est exécuté APRÈS la boucle
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    # Lancement de la boucle
    spam_loop()
    

def image_to_clipboard(image_path):
    image = Image.open(image_path)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # skip BMP header
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

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

# Variables globales
buffer = []
touches_actives = set()
groupe_actif = set()
rac_shortcut = {Key.alt_l, KeyCode.from_char('s')}

def listen():
    print("\nActuellement à l'écoute hehe\n")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def on_press(key):
    global groupe_actif, touches_actives, buffer

    touches_actives.add(key)
    groupe_actif.add(key)

    if rac_shortcut.issubset(touches_actives):
        buffer_tmp = deepcopy(buffer)  # Sauvegarde
        sleep(1)

        clavier = Controller()

        for _ in range(5):
            for grp in buffer_tmp:
                # Ignore raccourci ou groupe contenant Entrée
                if set(grp).issubset(rac_shortcut) or any(str(k) == 'Key.enter' for k in grp):
                    continue

                for touche in grp:
                    clavier.press(touche)
                for touche in reversed(grp):
                    clavier.release(touche)

                sleep(0.1)  # Pause entre groupes

            clavier.press(Key.enter)
            clavier.release(Key.enter)
            sleep(0.1)

        # Nettoyage et restauration
        touches_actives.clear()
        groupe_actif.clear()
        buffer = deepcopy(buffer_tmp)  # Restauration
        print(buffer)


def on_release(key):
    global buffer, groupe_actif, touches_actives

    if key in touches_actives:
        touches_actives.remove(key)

    # Enregistrement du groupe actif
    if groupe_actif:
        groupe = list(groupe_actif)
        buffer.append(groupe)
        groupe_actif.clear()

    # Espace → reset buffer
    if key == Key.space:
        print("Buffer complet avant reset :", buffer)
        buffer.clear()

    # Échap → quitter
    if key == Key.esc:
        return False

