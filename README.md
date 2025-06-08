# 🎮 Clavier Analogique vJoy – Contrôleur fait maison

Ce projet simule un **joystick analogique** à l’aide du **clavier**, en contrôlant un périphérique virtuel via **vJoy**. Il est parfait pour les jeux comme **Euro Truck Simulator 2**, où tu veux un **volant progressif**, contrôlable avec les flèches gauche/droite.

---

## 🚀 Fonctionnalités

- 🕹️ Axe X : contrôlé avec ← (gauche) et → (droite)
- 🕹️ Axe Y : contrôlé avec ↑ (accélérer) et ↓ (freiner)
- 🔁 Rappel automatique au centre (X) et au repos (Y)
- 🧠 Appui sur `Shift` → accélère les mouvements
- 💡 Compatible avec tous les jeux lisant les axes joystick (via vJoy)

---

## 📦 Prérequis

### Logiciels requis :
- [vJoy](https://sourceforge.net/projects/vjoystick/) — Crée un joystick virtuel.
- Python 3.7+

### Modules Python :
```bash
pip install pyvjoy pynput
```

---

## ▶️ Utilisation

1. Installer vJoy et activer l’**axe X** et **axe Y** dans `vJoyConf`.
2. Vérifier que le périphérique vJoy est visible :
   ```bash
   joy.cpl
   ```
3. Lancer le script :
   ```bash
   python controller.py
   ```
4. Démarrer votre jeu (ex : ETS2) et assigner les axes `Joy X` (direction) et `Joy Y` (accélérateur/frein).

---

## 📝 Fichier principal

- `controller.py` : le cœur du projet. Lit le clavier et contrôle vJoy.

---

## ✅ Todo / Idées futures

- [ ] Ajout d'une zone morte autour de la position centrale
- [ ] Interface graphique de configuration
- [ ] Portage en C natif
- [ ] Gestion des boutons (clavier → boutons joystick)
- [ ] Génération d’un `.exe` portable
- [ ] Support Linux via `uinput` (version avancée)

---

//## 📸 Capture d'écran ![Aperçu ETS2](img/apercu-ets2.png)--

## 🧑‍💻 Auteur

Lucas - 2025  
Projet expérimental pour un **volant maison**, fluide et sans manette physique.

---
