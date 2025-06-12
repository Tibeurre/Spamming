import utils as u
import customtkinter as ctk
import os
from PIL import Image

def switch_to_classic_spam_from_main():
    frame_accueil.pack_forget()  # Masquer le cadre d'accueil
    frame_classique.pack(pady=20, padx=20, fill="both", expand=True)  # Afficher le cadre classique

def switch_to_main_from_classic():
    frame_classique.pack_forget()  # Masquer le cadre classique
    frame_accueil.pack(pady=20, padx=20, fill="both", expand=True)  # Afficher le cadre d'accueil

def switch_to_main_from_texte():
    frame_texte.pack_forget()  # Masquer le cadre texte
    frame_accueil.pack(pady=20, padx=20, fill="both", expand=True)  # Afficher le cadre d'accueil

def switch_to_texte_from_main():
    frame_accueil.pack_forget()  # Masquer le cadre d'accueil
    frame_texte.pack(pady=20, padx=20, fill="both", expand=True)  # Afficher le cadre texte

# spam = True

# while spam:
#     print("-------------------------------Start-------------------------------\n")
#     todo = input("Que veux-tu faire petit farfadet malicieux ? \n 1. Spam un message \n 2. Déblatérer un texte  \n 3. Clavier à l'écoute \n 4. Quitter \nTon choix : ")

#     if todo == "1":
#         utils.spam()
#     elif todo == "2":
#         utils.texte()
#     elif todo == "3":
#         utils.listen()
#     else:
#         break
    
#     print("\nHihihihi c'est fait !")
#     spam = input("\nOn respam autre chose ? (Y/N) \n").lower() == "y"

# print("A la prochaine mon minot;)\n")

# Configuration de l'apparence globale
ctk.set_appearance_mode("System")  # Options: "System" | "Dark" | "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue" 

# Fenêtre principale
app = ctk.CTk()
app.geometry("800x550")
app.title("Logiciel du Farfadet Malicieux")



##FRAME D'ACCUEIL

frame_accueil = ctk.CTkFrame(app)
frame_accueil.pack(pady=20, padx=20, fill="both", expand=True)

# Configuration du layout 3 colonnes
frame_accueil.grid_columnconfigure(0, weight=1)  # marge gauche
frame_accueil.grid_columnconfigure(1, weight=3)  # contenu (centré)
frame_accueil.grid_columnconfigure(2, weight=1)  # marge droite
# Configurer la colonne pour qu'elle soit redimensionnable
frame_accueil.grid_columnconfigure(0, weight=1)

# Widgets
label = ctk.CTkLabel(frame_accueil, text="Quelle malicerie aujourd'hui ?", font=ctk.CTkFont(size=20, weight="bold"))
label.grid(row=0, column=1, padx=20, pady=20, sticky="n")

button = ctk.CTkButton(frame_accueil, text="Spam classique", command=switch_to_classic_spam_from_main)
button.grid(row=4, column=1, padx=20, pady=20)

button = ctk.CTkButton(frame_accueil, text="Spam depuis script", command=switch_to_texte_from_main)
button.grid(row=6, column=1, padx=20, pady=20)

# Charge l'image depuis le fichier
image_path = "image/farfadet.png"  # 🔁 Remplace avec le chemin correct
image = Image.open(image_path)

# Crée un CTkImage
ctk_img = ctk.CTkImage(light_image=image, dark_image=image, size=(200, 300))  # ajuste la taille si besoin

# Ajoute l'image dans un label
image_label = ctk.CTkLabel(frame_accueil, image=ctk_img, text="")  # text="" pour ne pas afficher le texte par défaut
image_label.grid(row=10, column=1, padx=20, pady=20)

## FRAME POUR SPAM CLASSIQUE

# Création d’un cadre (frame)
frame_classique = ctk.CTkFrame(app)
frame_classique.pack(pady=20, padx=20, fill="both", expand=True)

# Configuration du layout 3 colonnes
frame_classique.grid_columnconfigure(0, weight=1)  # marge gauche
frame_classique.grid_columnconfigure(1, weight=3)  # contenu (centré)
frame_classique.grid_columnconfigure(2, weight=1)  # marge droite

# Configurer la colonne pour qu'elle soit redimensionnable
frame_classique.grid_columnconfigure(0, weight=1)

# Widgets
label = ctk.CTkLabel(frame_classique, text="- C'est quoi un spamming classique ?\n- C'est un spamming mais classique en fait", font=ctk.CTkFont(size=20, weight="bold"))
label.grid(row=0, column=1, padx=20, pady=20, sticky="n")

entry_spam = ctk.CTkEntry(frame_classique, placeholder_text="Quel message spam ?")
entry_spam.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

entry_amount = ctk.CTkEntry(frame_classique, placeholder_text="Combien de fois ?")
entry_amount.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

entry_preparation = ctk.CTkEntry(frame_classique, placeholder_text="Combien de secondes avant de commencer ?")
entry_preparation.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

button = ctk.CTkButton(frame_classique, text="Lancer le spam", command=lambda: u.start_spam(entry_preparation.get(),
                                                                                          entry_amount.get(),
                                                                                          entry_spam.get(),
                                                                                          app=app))
button.grid(row=4, column=1, padx=20, pady=20)

button = ctk.CTkButton(frame_classique, text="Retour à l'accueil", command=switch_to_main_from_classic)
button.grid(row=6, column=1, padx=20, pady=20)

frame_classique.pack_forget()



## FRAME POUR SPAM DEPUIS TEXTE

# Frame principale
frame_texte = ctk.CTkFrame(app)
frame_texte.pack(pady=20, padx=20, fill="both", expand=True)

# Config layout 3 colonnes
frame_texte.grid_columnconfigure(0, weight=1)  # marge gauche
frame_texte.grid_columnconfigure(1, weight=3)  # contenu
frame_texte.grid_columnconfigure(2, weight=1)  # marge droite

frame_texte.label = ctk.CTkLabel(frame_texte, text="Spamming depuis un script txt", font=ctk.CTkFont(size=20, weight="bold"))
frame_texte.label.grid(row=0, column=1, padx=20, pady=20, sticky="n")

frame_tools = ctk.CTkFrame(frame_texte)
frame_tools.grid(row=1, column=1, sticky="nsew", pady=10)

FILEPATH = "./scripts"
entry_path = ctk.CTkEntry(frame_tools, placeholder_text="Chemin du dossier si différent de './scripts'", width=250)
entry_path.grid(row=2, column=1, padx=20, pady=10, sticky="e")

def update_filepath():
    global FILEPATH
    FILEPATH = entry_path.get()
    list_files(FILEPATH)

btn_update_path = ctk.CTkButton(frame_tools, text="Update le chemin", command=lambda: update_filepath())
btn_update_path.grid(row=2,column=2, padx=20, pady=10, sticky="e")

prepa_time = ctk.CTkEntry(frame_tools, placeholder_text="Temps avant lancement", width=250)
prepa_time.grid(row=2, column=0, padx=20, pady=10, sticky="w")

button = ctk.CTkButton(frame_texte, text="Retour à l'accueil", command=switch_to_main_from_texte)
button.grid(row=5, column=1, padx=20, pady=20, sticky="w")

# Frame centrale pour fichiers (grid 4x3)
frame_fichiers = ctk.CTkFrame(frame_texte)
frame_fichiers.grid(row=3, column=1, sticky="nsew", pady=10)

# Configuration des colonnes
for col in range(3):  # 3 colonnes
    frame_fichiers.grid_columnconfigure(col, weight=1)

# Configuration des lignes
for row in range(4):  # 4 lignes
    frame_fichiers.grid_rowconfigure(row, weight=1)

# Fichiers & pagination
FILES_PER_PAGE = 12
GRID_ROWS, GRID_COLS = 4, 3

current_page = 0
all_files = []
buttons = []

def list_files(path):
    global all_files
    all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    show_page(0)

def show_page(page_num):
    global current_page
    current_page = page_num

    # Supprimer anciens widgets
    for b in buttons:
        b.destroy()
    buttons.clear()

    start = page_num * FILES_PER_PAGE
    end = start + FILES_PER_PAGE
    files_to_show = all_files[start:end]

    for idx, filename in enumerate(files_to_show):
        row = idx // GRID_COLS
        col = idx % GRID_COLS

        btn = ctk.CTkButton(frame_fichiers, text=filename, command=lambda f=filename: on_file_click(f))
        btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        buttons.append(btn)

    update_nav_buttons()

def update_nav_buttons():
    total_pages = (len(all_files) - 1) // FILES_PER_PAGE
    btn_prev.configure(state="normal" if current_page > 0 else "disabled")
    btn_next.configure(state="normal" if current_page < total_pages else "disabled")

def on_file_click(filename):
    u.start_txt(os.path.join(FILEPATH, filename), int(prepa_time.get()), app)

def next_page():
    show_page(current_page + 1)

def prev_page():
    show_page(current_page - 1)

# Boutons de navigation
nav_frame = ctk.CTkFrame(frame_texte)
nav_frame.grid(row=4, column=1, pady=10)

btn_prev = ctk.CTkButton(nav_frame, text="←", command=prev_page)
btn_prev.pack(side="left", padx=10)

btn_next = ctk.CTkButton(nav_frame, text="→", command=next_page)
btn_next.pack(side="right", padx=10)

# Chargement des fichiers
list_files(FILEPATH)  # ← remplace par ton chemin

frame_texte.pack_forget()  # Masquer le cadre texte au démarrage

# Lancer l'application
app.mainloop()

