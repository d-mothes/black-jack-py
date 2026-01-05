INTRO = r"""
 _______   __                      __                 _____                      __       
/       \ /  |                    /  |               /     |                    /  |      
$$$$$$$  |$$ |  ______    _______ $$ |   __          $$$$$ |  ______    _______ $$ |   __ 
$$ |__$$ |$$ | /      \  /       |$$ |  /  |            $$ | /      \  /       |$$ |  /  |
$$    $$< $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/        __   $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$$$$$$  |$$ | /    $$ |$$ |      $$   $$<        /  |  $$ | /    $$ |$$ |      $$   $$<  
$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \       $$ \__$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ 
$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |      $$    $$/ $$    $$ |$$       |$$ | $$  |
$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/        $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ 
 """


MENU = r"""
[ 1 • Lancer une partie ]   [ 2 • Solde ]   [ 3 • Règles ]   [ 4 • Quitter ]"""


EXIT = r"""
 __       __                                __        __ 
/  \     /  |                              /  |      /  |
$$  \   /$$ |  ______    ______    _______ $$/       $$ |
$$$  \ /$$$ | /      \  /      \  /       |/  |      $$ |
$$$$  /$$$$ |/$$$$$$  |/$$$$$$  |/$$$$$$$/ $$ |      $$ |
$$ $$ $$/$$ |$$    $$ |$$ |  $$/ $$ |      $$ |      $$/ 
$$ |$$$/ $$ |$$$$$$$$/ $$ |      $$ \_____ $$ |       __ 
$$ | $/  $$ |$$       |$$ |      $$       |$$ |      /  |
$$/      $$/  $$$$$$$/ $$/        $$$$$$$/ $$/       $$/ """


MESSAGE_ERREUR = r"""
 ________                                                   
/        |                                                  
$$$$$$$$/   ______    ______    ______   __    __   ______  
$$ |__     /      \  /      \  /      \ /  |  /  | /      \ 
$$    |   /$$$$$$  |/$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$  |
$$$$$/    $$ |  $$/ $$ |  $$/ $$    $$ |$$ |  $$ |$$ |  $$/ 
$$ |_____ $$ |      $$ |      $$$$$$$$/ $$ \__$$ |$$ |      
$$       |$$ |      $$ |      $$       |$$    $$/ $$ |      
$$$$$$$$/ $$/       $$/        $$$$$$$/  $$$$$$/  $$/"""


INTRO_SOLDE = r"""
  ______             __        __           
 /      \           /  |      /  |          
/$$$$$$  |  ______  $$ |  ____$$ |  ______  
$$ \__$$/  /      \ $$ | /    $$ | /      \ 
$$      \ /$$$$$$  |$$ |/$$$$$$$ |/$$$$$$  |
 $$$$$$  |$$ |  $$ |$$ |$$ |  $$ |$$    $$ |
/  \__$$ |$$ \__$$ |$$ |$$ \__$$ |$$$$$$$$/ 
$$    $$/ $$    $$/ $$ |$$    $$ |$$       |
 $$$$$$/   $$$$$$/  $$/  $$$$$$$/  $$$$$$$/ 
 """


MENU_SOLDE = r"""
[ 1 • Ajouter joueur ]   [ 2 • Supprimer joueur ]   [ 3 • Classement ]   [ 4 • Quitter ]"""


TEXTS = {
    "intro": INTRO,
    "menu": MENU,
    "exit": EXIT,
    "message_erreur": MESSAGE_ERREUR,
    "intro_solde": INTRO_SOLDE,
    "menu_solde": MENU_SOLDE
}


INTRO_RULES = r"""
 _______             __                     
/       \           /  |                    
$$$$$$$  | __    __ $$ |  ______    _______ 
$$ |__$$ |/  |  /  |$$ | /      \  /       |
$$    $$< $$ |  $$ |$$ |/$$$$$$  |/$$$$$$$/ 
$$$$$$$  |$$ |  $$ |$$ |$$    $$ |$$      \ 
$$ |  $$ |$$ \__$$ |$$ |$$$$$$$$/  $$$$$$  |
$$ |  $$ |$$    $$/ $$ |$$       |/     $$/ 
$$/   $$/  $$$$$$/  $$/  $$$$$$$/ $$$$$$$/  
"""


RULES = r"""
================= REGLES DU BLACKJACK =================

OBJECTIF :
Se rapprocher le plus possible de 21 points sans dépasser 21 et faire un meilleur score que le croupier.

ARGENT :
- Au début de chaque partie, le joueur reçoit automatiquement +5$ ajoutés à son solde.
- Le joueur peut ensuite miser une partie de son argent.
- En cas de victoire, la mise est gagnée.
- En cas de défaite, la mise est perdue.
- En cas d'égalité, la mise est rendue.

DEROULEMENT D'UNE PARTIE :
1) Le joueur et le croupier reçoivent 2 cartes chacun.
2) Le joueur peut :
   - Piocher une carte
   - Rester avec son score actuel
3) Si le joueur dépasse 21, il perd immédiatement.

CROUPIER :
- Le croupier pioche automatiquement tant que son score est inférieur à 17.
- Il s'arrête dès que son score atteint 17 ou plus.

VICTOIRE / DEFAITE :
- Joueur > 21        -> Défaite
- Croupier > 21      -> Victoire du joueur
- Score le plus proche de 21 gagne
- Egalité            -> Egalité (aucune perte)

STATISTIQUES :
- Les victoires et les défaites sont enregistrées.
- Le solde du joueur est mis à jour automatiquement.

======================================================="""


TEXTS_RULES = {
    "intro": INTRO_RULES,
    "rules": RULES
}