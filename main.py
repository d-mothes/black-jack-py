#!/bin/env python3

# =============== Bibliotheques ===============
import time
import os
import subprocess
import sys
import json
import bcrypt

# =============== Programmes ===============
from lib.texts import TEXTS # dictionnaire de textes
from lib.texts import TEXTS_RULES # dictionnaire pour le règlement


# =============== Data ===============
with open("lib/data.json", "r", encoding="utf-8") as f: # data.json (base de données)
    data = json.load(f) # data devient un dictionnaire python

with open("lib/session.json", "r", encoding="utf-8") as f:  # session.json
    session_data = json.load(f) # session_data devient un dictionnaire Python


# =============== Fonctions ===============
def clear(): # fonction pour clear le terminal
    # "cls" sur windows, "clear" sur linux et mac
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True) # exécute la commande dans le shell

def save_json(path, obj): # fonction pour enregistrer dans un fichier JSON
    # path : chemin du fichier
    # obj  : dictionnaire python à sauvegarder
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)

def create_first_player(): # fonction pour créer un premier joueur si la data est vide
    global data
    clear()
    print(TEXTS["intro"] + "\n" "Création d'un premier joueur :" + "\n")
    # récupération du username et mot de passe brut
    username = str(input("Username :")).strip()
    password_brut = str(input("Password :")).strip()
    # hash du mot de passe
    hashed_password = bcrypt.hashpw(password_brut.encode(), bcrypt.gensalt())
    password_brut = "" # on efface la variable en mémoire
    # construction du nouveau joueur sous forme de dictionnaire
    new_player = {
        "id": data["next_id"],
        "username": username,
        "password": hashed_password.decode(),
        "solde": 0,
        "wins": 0,
        "losses": 0
    }
    data["players"].append(new_player) # ajout du joueur dans data
    data["next_id"] += 1 # mise à jour de next_id pour le prochain joueur
    save_json("lib/data.json", data) # sauvegarde
    clear()
    print(TEXTS["intro"] + "\n" f"Joueur {username} créé avec succès !" + "\n")
    time.sleep(1.8)

def select_player(): # fonction pour sélectionner un joueur
    global session_data
    clear()
    print(TEXTS["intro"] + "\n" + "Joueur(s) disponible(s) :" + "\n")
    for i, player in enumerate(data["players"], start=1): # affichage des joueurs disponibles
        print(f"[{i}] {player['username']} (solde: {player['solde']} $)")
    print("")
    choice_player = int(input("Selectionnez un joueur (id) :"))
    joueur = data["players"][choice_player - 1] # on récupère le joueur correspondant
    tentative = 3 # sécurité de tentatives (3 essais)
    confirm = ""
    # tant que le mot de passe n'est pas bon, on redemande
    # bcrypt.checkpw() compare un mot de passe brut à un hash
    while not bcrypt.checkpw(confirm.encode(), joueur["password"].encode()):
        confirm = str(input(f"Pour confirmer, tapez le mot de passe de ({joueur['username']}) :")).strip()
        clear()
        print(TEXTS["intro"] + "\n")
        # si incorrect : on diminue les tentatives
        if not bcrypt.checkpw(confirm.encode(), joueur["password"].encode()):
            tentative -= 1
            print(f"Mot de passe incorrect, il vous reste {tentative} tentatives")
            time.sleep(1)
        # si correct : on écrit la session
        elif bcrypt.checkpw(confirm.encode(), joueur["password"].encode()):
            session_data = {
                "selected_player_id": joueur["id"] # on stocke l'id unique du joueur sélectionné
            }
            save_json("lib/session.json", session_data)
            clear()
            print(TEXTS["intro"] + "\n" f"Vous jouerez avec : {joueur['username']}" + "\n")
            time.sleep(0.4)
            return # on sort de la fonction après succès
        # si plus aucune tentative : on abandonne
        if tentative <= 0:
            print("erreur")
            return

def reset_session(): # reset du joueur sélectionné
    session_reset = {
        "selected_player_id": None
    }
    save_json("lib/session.json", session_reset)

def message_erreur(): # afficher un message erreur
    clear()
    print(TEXTS["message_erreur"] + "\n")
    time.sleep(0.9)
    clear()




# =============== Main ===============
clear()
while True: # boucle infinie : menu principal qui tourne tant que le programme n'est pas quitté
    print(TEXTS["intro"] + "\n" + TEXTS["menu"] + "\n")
    choice_menu = str(input("(menu)$:")).strip()

    # ----------- Jouer -----------
    if choice_menu == "1":
        if len(data["players"]) == 0: # si aucun joueur enregistré -> création du premier joueur
            create_first_player()
        elif len(data["players"]) > 0: # si au moins un joueur existe -> on doit s'assurer qu'un joueur est sélectionné
            if session_data["selected_player_id"] is None: # si aucun joueur dans la session -> sélectionner
                select_player()
            else: # si un joueur est déjà sélectionné, on demande si on garde le même
                clear()
                print(TEXTS["intro"] + "\n")
                reset_sess = str(input("Souhaitez vous jouer avec le meme joueur ? (o/n) : ")).strip().upper()
                if reset_sess == "N": # si non -> reset session + sélection d'un autre joueur
                    reset_session()
                    select_player()
                    os.system("python3 lib/game.py") # lancement du jeu
                elif reset_sess == "O":
                    os.system("python3 lib/game.py") # lancement du jeu
                else:
                    message_erreur()
                    


    # ----------- Solde -----------
    elif choice_menu == "2":
        clear()
        os.system("python3 lib/players_manager.py") # lancement du gestionnaire de joueurs
        with open("lib/data.json", "r", encoding="utf-8") as f: # mise à jour de la data après retour du manager
            data = json.load(f)


    # ----------- Règlement -----------
    elif choice_menu == "3":
        clear()
        # affiche le règlement puis attend une entrée
        print(TEXTS_RULES["intro"] + "\n" + TEXTS_RULES["rules"] + "\n")
        ext = input("Entrez pour continuez…")
        clear()


    # ----------- Quitter -----------
    elif choice_menu == "4":
        choice_exit = "a" # valeur impossible au départ
        while choice_exit != "n": # boucle de confirmation : on force l'utilisateur à répondre o/n
            clear()
            print(TEXTS["intro"] + "\n")
            choice_exit = str(input("Souhaitez vous vraiment quitter ? (o/n) : ")).strip()
            if choice_exit == "o":
                reset_session() # on reset la session avant de quitter pour les prochains lancements
                clear()
                print(TEXTS["exit"])
                time.sleep(1.8)
                clear()
                sys.exit() # sortie du programme
            elif choice_exit == "n": # annule quitter -> retour au menu principal
                clear()
            else: # mauvaise saisie -> message d'erreur
                message_erreur()


    # ----------- Admin -----------
    elif choice_menu == "admin":
        os.system("python3 lib/admin.py") # lance le panel admin
        # mise à jour de data et session
        with open("lib/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("lib/session.json", "r", encoding="utf-8") as f:
            session_data = json.load(f)

    # ----------- Erreur -----------
    else:
        message_erreur()

# =============== Fin du programme ===============
