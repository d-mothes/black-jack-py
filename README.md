# 🎴 Blackjack en terminal – Python

## 📌 Présentation du projet

Ce projet est un **jeu de Blackjack en terminal** développé en **Python** dans le cadre de mes **études en informatique**.

Initialement conçu pour répondre à des exigences scolaires de base, j’ai volontairement **étendu et amélioré le projet** afin de :
- renforcer mes compétences en Python
- appliquer la **programmation orientée objet (POO)**
- gérer la **persistance des données** (JSON)
- expérimenter des **notions de base en cybersécurité**
- présenter mon travail sur GitHub dans le cadre de mon apprentissage en programmation

Ce dépôt est public à des fins **éducatives et démonstratives**.

---

## 🎮 Fonctionnalités

- Jeu de Blackjack simplifié jouable entièrement en terminal
- Gestion de plusieurs joueurs (création, suppression, sélection)
- Stockage persistant des joueurs, soldes et statistiques
- Système de session pour suivre le joueur actuellement sélectionné
- Affichage ASCII des cartes avec couleurs
- Classement des joueurs basé sur le ratio victoires/défaites
- Commande administrateur cachée pour la gestion avancée des données

---

## 🔐 Sécurité & apprentissage en cybersécurité

Ce projet utilise la bibliothèque **bcrypt** afin de **hach­er les mots de passe de manière sécurisée**.

Objectifs pédagogiques :
- ne jamais stocker de mots de passe en clair
- comprendre le fonctionnement du hachage
- utiliser une bibliothèque de sécurité standard
- appliquer des concepts de cybersécurité appris durant mes études

Tous les mots de passe des joueurs et de l’administrateur sont stockés **uniquement sous forme de hash**, jamais en clair.

---

## 🛠️ Installation

### 1️⃣ Cloner le dépôt

git clone https://github.com/d-mothes/black-jack-py.git  
cd black-jack-py

---

### 2️⃣ Créer un environnement virtuel

Linux / macOS :  
python3 -m venv venv  
source venv/bin/activate  

Windows :  
python -m venv venv  
venv\Scripts\activate  

---

### 3️⃣ Installer les dépendances

pip install -r requirements.txt  
ou  
pip3 install -r requirements.txt  

Dépendances utilisées :
- bcrypt
- colorama

---

## ▶️ Lancer le programme

python3 main.py  
ou  
python main.py  

---

## 👤 Accès administrateur (commande cachée)

Le programme inclut une **commande administrateur cachée** qui n’est pas affichée dans le menu principal.

Commande :  
admin  

Mot de passe administrateur par défaut :  
Admin1234  

Cette fonctionnalité est volontairement simple et destinée **uniquement à des fins pédagogiques**.

---

## 📂 Structure du projet

main.py  
lib/  
&nbsp;&nbsp;game.py  
&nbsp;&nbsp;players_manager.py  
&nbsp;&nbsp;admin.py  
&nbsp;&nbsp;texts.py  
&nbsp;&nbsp;data.json  
&nbsp;&nbsp;session.json  
requirements.txt  
README.txt  

---

## 🎓 Contexte académique

Ce projet a été développé dans un cadre scolaire, mais il va **au-delà des exigences initiales** afin de :
- consolider les bases de la programmation
- explorer des concepts plus avancés
- construire un projet de taille moyenne, propre et structuré

---

## 🚀 Améliorations possibles

- Graphismes ASCII des cartes plus avancés
- Historique des parties et statistiques détaillées
- Classement des joueurs plus élaboré
- Système d’accès basé sur des rôles
- Migration vers une base de données SQL

---

## 📜 Licence

Projet open-source à des fins **éducatives**.
