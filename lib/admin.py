import os
import subprocess
import json

with open("lib/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
with open("lib/session.json", "r", encoding="utf-8") as f:
    session_data = json.load(f)

def save_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)

def reset_session():
    session_reset = {
        "selected_player_id": None
    }
    save_json("lib/session.json", session_reset)

def reset_data():
    data_reset = {
  "players": [],
  "next_id": 1
}
    save_json("lib/data.json", data_reset)

def delete_player(): #fonction pour supprimer un joueur
    global data
    for i, player in enumerate(data["players"], start=1):  # affichage des joueurs
        print(f"[{i}] {player['username']} (solde: {player['solde']} $)")
    choice_delete = int(input("\n" + "id du joueur à supprimer :"))
    choice_delete -= 1
    joueur = data["players"][choice_delete]
    print("Joueur(s) enregisté(s) :" + "\n")  # menu
    del data["players"][choice_delete]  # suppresion du joueur
    save_json("lib/data.json", data)  # enregistrement
    print(f"\nLe joueur '{joueur['username']}' a été supprimé.")


mdp = str(input("mot de passe admin :"))
if mdp == "Admin1234" :
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)
    choice = "a"
    while choice != "4" :
        print("(1)reset session     (2)reset data      (3)delete player     (4)exit")
        choice = str(input("choice:")).strip()
        if choice == "1":
            reset_session()
        elif choice == "2":
            reset_data()
        elif choice == "3":
            delete_player()
        elif choice == "4":
            pass


else:
    pass