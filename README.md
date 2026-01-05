# 🎴 Terminal Blackjack – Python

## 📌 Project Overview

This project is a **terminal-based Blackjack game** developed in **Python** as part of my **computer science coursework**.

Originally designed to meet basic school requirements, I intentionally **extended and improved the project** to:
- strengthen my Python skills
- apply **object-oriented programming (OOP)**
- manage **persistent data storage** (JSON)
- experiment with **basic cybersecurity concepts**
- showcase my work on GitHub as part of my programming portfolio

This repository is public for **educational and demonstrative purposes**.

---

## 🎮 Features

- Simplified Blackjack game playable entirely in the terminal
- Multiple player management (create, delete, select)
- Persistent storage of players, balances, and statistics
- Session system to track the currently selected player
- ASCII card display with colors
- Player ranking based on win/loss ratio
- Hidden admin command for advanced data management

---

## 🔐 Security & Cybersecurity Learning

This project uses the **bcrypt** library to securely **hash passwords**.

Educational goals:
- never store passwords in plain text
- understand how hashing works
- use a standard security library
- apply cybersecurity concepts learned during my studies

All player and admin passwords are stored **only as hashes**, never in clear text.

---

## 🛠️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/d-mothes/black-jack-py.git
cd black-jack-py

---

### 2️⃣ Create a virtual environment

Linux / macOS:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

Dependencies used:
- bcrypt
- colorama

---

## ▶️ Run the program

python3 main.py
or
python main.py

---

## 👤 Admin Access (Hidden Command)

The program includes a **hidden admin command** that is not displayed in the main menu.

Command:
admin

Default admin password:
Admin1234

This feature is intentionally simple and is meant for **educational purposes only**.

---

## 📂 Project Structure

main.py
lib/
  game.py
  players_manager.py
  admin.py
  texts.py
  data.json
  session.json
requirements.txt
README.txt

---

## 🎓 Academic Context

This project was developed in a school context, but it goes **beyond the original requirements** in order to:
- consolidate programming fundamentals
- explore more advanced concepts
- build a clean and structured mid-sized project

---

## 🚀 Possible Improvements

- Enhanced ASCII card graphics
- Game history and statistics
- More advanced player rankings
- Role-based access system
- Migration to an SQL database

---

## 📜 License

Open-source project for **educational purposes**.
