# =============== Bibliotheques ===============
import time
import os
import subprocess
import sys
import json
import bcrypt


# =============== Programmes ===============
from texts import TEXTS   # dictionnaire de textes


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

def message_erreur(): # afficher un message erreur
    clear()
    print(TEXTS["message_erreur"] + "\n")
    time.sleep(0.9)
    clear()

def save_json(path, obj): # fonction pour enregistrer dans un fichier JSON
    # path : chemin du fichier
    # obj  : dictionnaire python à sauvegarder
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)

def create_player(): # fonction pour créer un joueur
    global data
    clear()
    print(TEXTS["intro_solde"] + "\n")
    username = str(input("Username :")).strip()
    # liste des pseudos déjà existants pour éviter les doublons
    existing_usernames = [player["username"] for player in data["players"]]
    # si le username existe déjà, on ajoute 1, 2, 3 etc. à la fin
    if username in existing_usernames: # si doublon
        n = 1
        new_name = username + str(n)
        while new_name in existing_usernames:
            n += 1
            new_name = username + str(n)
        username = new_name # username final unique
    # saisie mot de passe brut puis hash
    password_brut = str(input("Password :")).strip()
    hashed_password = bcrypt.hashpw(password_brut.encode(), bcrypt.gensalt())
    password_brut = ""  # on efface la variable en mémoire
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
    save_json("lib/data.json", data) #enregistrement
    clear()
    print(TEXTS["intro_solde"] + "\n" f"Joueur {username} créé avec succès !" + "\n")
    time.sleep(1.8)

def delete_player(): # fonction pour supprimer un joueur
    global data
    # on demande le numéro (affiché) du joueur à supprimer
    choice_delete = int(input("\n" + "id du joueur à supprimer :"))
    choice_delete -= 1 # passage en index Python
    joueur = data["players"][choice_delete] # on récupère le joueur correspondant
    clear()
    print(TEXTS["intro_solde"] + "\n" + "Joueur(s) enregisté(s) :" + "\n")  # menu
    for i, player in enumerate(data["players"], start=1):  # affichage des joueurs
        print(f"[{i}] {player['username']} (solde: {player['solde']} $)")
    print("")
    tentative = 3 # sécurité de tentatives (3 essais)
    confirm = ""
    # tant que le mot de passe n'est pas bon, on redemande
    # bcrypt.checkpw() compare un mot de passe brut à un hash
    while not bcrypt.checkpw(confirm.encode(), joueur["password"].encode()) :
        confirm = str(input(f"Pour confirmer, tapez le mot de passe de ({joueur['username']}) :")).strip()
        clear()
        print(TEXTS["intro_solde"] + "\n")
        # si incorrect : on diminue les tentatives
        if not bcrypt.checkpw(confirm.encode(), joueur["password"].encode()):
            tentative -= 1
            print(f"Mot de passe incorrect, il vous reste {tentative} tentatives")
            time.sleep(1)
        # si correct : on supprime le joueur
        elif bcrypt.checkpw(confirm.encode(), joueur["password"].encode()):
            del data["players"][choice_delete] #suppresion du joueur
            save_json("lib/data.json", data) #enregistrement
            print(f"\nLe joueur '{joueur['username']}' a été supprimé.")
            time.sleep(1.5)
            return
        # si plus de tentatives : on annule
        if tentative <= 0:
            print("erreur")
            return

def classement(): # fonction pour classer les joueurs
    global data
    players = data["players"]
    if len(players) == 0: #si pas de joueur erreur
        print("Aucun joueur enregistré")
        time.sleep(1.8)
        return
    # construction d'une liste (ratio, joueur) pour pouvoir trier ensuite
    classement_list = []
    for p in players:
        wins = p["wins"]
        losses = p["losses"]
        # calcul du ratio (wins / losses)
        # cas spécial : 0 défaites -> on évite division par 0
        if losses == 0:
            ratio = wins
        else:
            ratio = wins / losses
        # on stocke le ratio + le dictionnaire joueur
        classement_list.append((ratio, p))
    for i in range(len(classement_list)): # tri par sélection du meilleur au moins bon
        max_index = i
        for j in range(i + 1, len(classement_list)):
            # on compare les ratios
            if classement_list[j][0] > classement_list[max_index][0]:
                max_index = j
        if i != max_index:
            # swap des éléments
            temp = classement_list[i]
            classement_list[i] = classement_list[max_index]
            classement_list[max_index] = temp
    # affichage final du classement
    clear()
    print(TEXTS["intro_solde"])
    print("\n===== CLASSEMENT (ratio victoires/défaites) =====\n") #affichage
    for i, (ratio, p) in enumerate(classement_list, start=1):
        print(f"{i}. {p['username']} | ratio:{ratio:.2f} | Wins:{p['wins']} Losses:{p['losses']} | solde:{p['solde']}")




# =============== Main ===============
choice_solde = "n" # valeur impossible pour forcer la boucle
while choice_solde != "4" : # boucle tant que l'utilisateur n'a pas choisi "4" (quitter)
    clear()
    print(TEXTS["intro_solde"] + "\n" + "Joueur(s) enregisté(s) :" + "\n") # menu
    if len(data["players"]) == 0: # si pas de joueur erreur
        print("Aucun joueur enregistré")
    for i, player in enumerate(data["players"], start=1): # affichage des joueurs
        print(f"[{i}] {player['username']} (solde: {player['solde']} $)")
    print(TEXTS["menu_solde"] + "\n")
    choice_solde = str(input("(solde)$:")).strip()

    # ----------- Ajouter joueur -----------
    if choice_solde == "1" :
        create_player() # création d'un joueur


    # ----------- Supprimer joueur -----------
    elif choice_solde == "2" :
        clear()
        print(TEXTS["intro_solde"] + "\n")
        if len(data["players"]) == 0: # si pas de joueur erreur
            print("Aucun joueur enregistré")
            time.sleep(1.8)
        else:
            print("Joueur(s) enregisté(s) :" + "\n")
            for i, player in enumerate(data["players"], start=1): # affichage des joueurs
                print(f"[{i}] {player['username']} (solde: {player['solde']} $)")
            # lance la procédure de suppression avec mot de passe
            delete_player()


    # ----------- Classement -----------
    elif choice_solde == "3" :
        # affiche le classement par ratio wins/losses
        classement()
        print("")
        ctn = input("Entrez pour continuer…")
        clear()


    # ----------- Quitter -----------
    elif choice_solde == "4" :
        # quitter le manager, retour au main
        clear()


    # ----------- Erreur -----------
    else :
        message_erreur() # entrée invalide -> message d'erreur


# =============== Fin du programme ===============