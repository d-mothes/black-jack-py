# =============== Bibliotheques ===============
import json
import os
import random
import time
import subprocess

from colorama import Fore, Style, init


# =============== Programmes ===============
DATA_PATH = "lib/data.json" # chemin vers la data des joueurs
SESSION_PATH = "lib/session.json" # chemin vers la session

from texts import TEXTS # textes d'affichage


# =============== Fonctions ===============
def clear(): # fonction pour clear le terminal
    # "cls" sur windows, "clear" sur linux et mac
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True) # exécute la commande dans le shell

def load_json(path): # fonction pour charger un fichier json
    # path : chemin du fichier
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)  # retourne un dictionnaire python

def save_json(path, obj): # fonction pour enregistrer dans un fichier JSON
    # path : chemin du fichier
    # obj  : dictionnaire python à sauvegarder
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)


# ==================== Cartes (OOP) ====================
SUITS = ["♠", "♥", "♦", "♣"] # symboles possibles des cartes

# valeurs possibles des cartes
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card: # représente une carte unique (valeur + symbole)
    def __init__(self, rank: str, suit: str):
        self.rank = rank # valeur de la carte
        self.suit = suit # symbole

    def value(self) -> int: # valeur numérique de la carte pour le blackjack
        if self.rank in ["J", "Q", "K"]:
            return 10
        if self.rank == "A":
            return 11
        return int(self.rank)

    def colored_suit(self) -> str: # coloration du symbole :
        # ♥ ♦ en rouge, ♠ ♣ en couleur par défaut
        if self.suit in ["♥", "♦"]:
            return Fore.RED + self.suit + Style.RESET_ALL
        return self.suit

    def render(self, hidden: bool = False) -> list[str]:
        # représentation ASCII de la carte
        # hidden=True -> carte cachée (pour le croupier)
        if hidden:
            return [
                "┌─────────┐",
                "│░░░░░░░░░│",
                "│░░░░░░░░░│",
                "│░░░ ?? ░░│",
                "│░░░░░░░░░│",
                "│░░░░░░░░░│",
                "└─────────┘",
            ]
        rank = self.rank
        # alignement du texte :
        # "10" prend 2 caractères, les autres 1
        left = rank + (" " if len(rank) == 1 else "")
        right = (" " if len(rank) == 1 else "") + rank
        suit = self.colored_suit()
        # carte visible ASCII
        return [
            "┌─────────┐",
            f"│ {left}      │",
            "│         │",
            f"│    {suit}    │",
            "│         │",
            f"│      {right} │",
            "└─────────┘",
        ]


class Deck: # représente un paquet de cartes
    def __init__(self): # création d'un deck complet (52 cartes)
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards) # mélange aléatoire

    def draw(self) -> Card: # pioche une carte du paquet
        if len(self.cards) == 0:
            # sécurité : si le paquet est vide, on le recrée
            self.__init__()
        return self.cards.pop()


class Hand: # représente une main (joueur ou croupier)
    def __init__(self):
        self.cards: list[Card] = [] # liste des cartes dans la main

    def add(self, card: Card): # ajoute une carte à la main
        self.cards.append(card)

    def total(self) -> int: # calcule le total de la main
        total = sum(c.value() for c in self.cards)
        aces = sum(1 for c in self.cards if c.rank == "A")
        while total > 21 and aces > 0: # si on dépasse 21, on transforme des As de 11 -> 1
            total -= 10
            aces -= 1
        return total

    def is_bust(self) -> bool: # retourne True si le total dépasse 21
        return self.total() > 21

    def render(self, hide_first: bool = False) -> str: # affiche la main en ASCII
        if len(self.cards) == 0:
            return ""
        rendered_cards = []
        for i, card in enumerate(self.cards):
            # cache la première carte si nécessaire (croupier)
            hidden = (hide_first and i == 0)
            rendered_cards.append(card.render(hidden=hidden))
        lines = []
        for line_idx in range(len(rendered_cards[0])):
            lines.append("  ".join(c[line_idx] for c in rendered_cards))
        return "\n".join(lines)


class Player: # représente un joueur (ou le croupier)
    def __init__(self, username: str):
        self.username = username # nom affiché
        self.hand = Hand() # main du joueur




# ==================== Jeux ====================
class Game: # classe principale qui gère une partie de blackjack
    def __init__(self, player_record: dict, data_obj: dict):
        self.data = data_obj # base de données complète
        self.player_record = player_record # joueur sélectionné
        self.player = Player(player_record["username"])
        self.dealer = Player("Croupier")
        self.deck = Deck() # paquet de cartes
        self.bet = 0 # mise du joueur

    def add_start_bonus(self): # ajoute +5$ au solde à chaque début de partie
        self.player_record["solde"] += 5

    def ask_bet(self): # demande la mise au joueur
        solde = self.player_record["solde"]
        while True:
            try:
                bet_str = input(f"Mise (0 à {solde}) : ").strip()
                bet = int(bet_str)
                if 0 <= bet <= solde: #si mise invalide
                    self.bet = bet
                    return
                clear()
                print(TEXTS["intro"] + "\n")
                print("Mise invalide.")
            except ValueError: # si erreur
                clear()
                print(TEXTS["intro"] + "\n")
                print("Entrez un nombre.")

    def deal_initial(self): # distribution initiale : 2 cartes joueur / 2 cartes croupier
        self.player.hand.add(self.deck.draw())
        self.dealer.hand.add(self.deck.draw())
        self.player.hand.add(self.deck.draw())
        self.dealer.hand.add(self.deck.draw())

    def show_table(self, hide_dealer: bool): # affiche l'état actuel de la table
        clear()
        print("=========== BLACKJACK ===========\n")
        print(f"JOUEUR : {self.player.username}")
        print(self.player.hand.render())
        print(f"Total joueur : {self.player.hand.total()}\n")
        print("CROUPIER :")
        print(self.dealer.hand.render(hide_first=hide_dealer))
        if hide_dealer: # affiche seulement la valeur de la carte visible
            visible_total = self.dealer.hand.cards[1].value()
            print(f"Total croupier (partiel) : {visible_total}\n")
        else:
            print(f"Total croupier : {self.dealer.hand.total()}\n")
        print(f"Solde: {self.player_record['solde']} $ | Mise: {self.bet} $\n")

    def player_turn(self) -> bool: # tour du joueur
        # retourne False si le joueur dépasse 21 (bust)
        while True:
            self.show_table(hide_dealer=True)
            if self.player.hand.is_bust():
                return False
            choice = input("[T]irer / [R]ester : ").strip().upper()
            if choice == "T":
                self.player.hand.add(self.deck.draw())
            elif choice == "R":
                return True
            else:
                print("Choix invalide.")
                time.sleep(1)

    def dealer_turn(self) -> bool: # tour du croupier (pioche jusqu'à 17)
        # retourne False si le croupier bust
        while self.dealer.hand.total() < 17:
            self.show_table(hide_dealer=False)
            time.sleep(1.2)
            self.dealer.hand.add(self.deck.draw())
        self.show_table(hide_dealer=False)
        return not self.dealer.hand.is_bust()

    def apply_result(self, result: str): # applique le résultat de la partie
        if result == "win":
            self.player_record["solde"] += self.bet
            self.player_record["wins"] += 1
        elif result == "lose":
            self.player_record["solde"] -= self.bet
            self.player_record["losses"] += 1
        else: # égalité : rien ne change
            pass

    def save(self): # sauvegarde la data
        save_json(DATA_PATH, self.data)

    def play_round(self): # déroulement complet d'une partie
        self.add_start_bonus()
        self.ask_bet()
        self.deal_initial()
        still_in = self.player_turn()
        if not still_in:
            self.show_table(hide_dealer=False)
            print("BUST ! Tu dépasses 21. Défaite.")
            self.apply_result("lose")
            self.save()
            input("\nEntrée pour continuer...")
            return
        dealer_ok = self.dealer_turn()
        if not dealer_ok:
            print("Le croupier dépasse 21. Victoire !")
            self.apply_result("win")
            self.save()
            input("\nEntrée pour continuer...")
            return
        p_total = self.player.hand.total()
        d_total = self.dealer.hand.total()
        if p_total > d_total:
            print("Victoire ! Tu es plus proche de 21.")
            self.apply_result("win")
        elif p_total < d_total:
            print("Défaite... Le croupier est plus proche de 21.")
            self.apply_result("lose")
        else:
            print("Égalité (push).")
        self.save()
        input("\nEntrée pour continuer...")




# ==================== Main ====================
def find_player_by_id(data_obj: dict, pid: int): # recherche un joueur par son id
    for p in data_obj["players"]:
        if p.get("id") == pid:
            return p
    return None

exit = "a"
while exit != "n" : # boucle tant qu'on ne quitte pas o/n
    clear()
    print(TEXTS["intro"] + "\n")
    # mise à jour de la data
    data = load_json(DATA_PATH)
    session = load_json(SESSION_PATH)
    selected_id = session.get("selected_player_id")
    if selected_id is None:
        print("Aucun joueur sélectionné (session.json vide).")
        input("\nEntrée pour revenir...")
    # récupération du joueur sélectionné
    player_record = find_player_by_id(data, selected_id)
    if player_record is None:
        print("Le joueur sélectionné n'existe plus dans data.json.")
        input("\nEntrée pour revenir...")
    game = Game(player_record, data) # lancement du jeu
    game.play_round()
    exit = str(input("Souhaitez vous rejouer ? (o/n) : "))
    clear()