# 🐍 Guide d'installation de Python et de l'environnement virtuel

> **Cours :** Web Technologies  
> **Date :** 25 mars 2026

---

## 📋 Sommaire

1. [Vérifier si Python est installé](#1-vérifier-si-python-est-installé)
2. [Installer Python](#2-installer-python)
3. [Mettre à jour une installation existante](#3-mettre-à-jour-une-installation-existante)
4. [Créer un environnement virtuel (Virtual Environment)](#4-créer-un-environnement-virtuel-virtual-environment)
5. [Problèmes fréquents](#5-problèmes-fréquents)

---

## 1. Vérifier si Python est installé

### 🪟 Windows

Ouvrez l'**Invite de commandes** (cmd) ou **PowerShell** et exécutez :

```bash
python --version
```

Si vous obtenez quelque chose comme `Python 3.x.x` — Python est déjà installé. Si vous recevez l'erreur `'python' is not recognized...` — passez à l'[Étape 2](#2-installer-python).

> ⚠️ Sur certains systèmes Windows, la commande peut être `python3` au lieu de `python`. Essayez les deux.

### 🐧 Linux

Ouvrez un terminal et exécutez :

```bash
python3 --version
```

La plupart des distributions Linux sont livrées avec Python 3 préinstallé. Si la commande retourne une version `3.x.x` — vous êtes prêt. Sinon — passez à l'[Étape 2](#2-installer-python).

---

## 2. Installer Python

### 🪟 Windows

#### Étape 1 — Téléchargement

1. Rendez-vous sur le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Cliquez sur le bouton jaune **"Download Python 3.x.x"** (dernière version stable)
3. Un fichier `.exe` sera téléchargé

#### Étape 2 — Installation

1. Lancez le fichier `.exe` téléchargé
2. **⚠️ IMPORTANT :** Cochez la case **"Add python.exe to PATH"** (en bas de la fenêtre)
3. Cliquez sur **"Install Now"**
4. Attendez la fin de l'installation
5. Cliquez sur **"Close"**

```
┌─────────────────────────────────────────────┐
│  Install Python 3.x.x                      │
│                                             │
│  ☑ Install launcher for all users           │
│  ☑ Add python.exe to PATH  ← ICI !        │
│                                             │
│  [ Install Now ]                            │
└─────────────────────────────────────────────┘
```

#### Étape 3 — Vérification

Ouvrez une **nouvelle** Invite de commandes (obligatoirement nouvelle pour charger le PATH) et exécutez :

```bash
python --version
```

```bash
pip --version
```

Les deux commandes doivent retourner des informations sur les versions.

---

### 🐧 Linux

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

#### Fedora

```bash
sudo dnf install python3 python3-pip python3-virtualenv -y
```

#### Arch Linux

```bash
sudo pacman -S python python-pip
```

#### Vérification

```bash
python3 --version
pip3 --version
```

---

## 3. Mettre à jour une installation existante

### 🪟 Windows

Si vous avez déjà Python mais c'est une ancienne version (ex. 3.8, 3.9) :

1. Rendez-vous sur [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Téléchargez la dernière version
3. Lancez l'installateur
4. Choisissez **"Upgrade Now"** (l'installateur détecte automatiquement l'ancienne version)

> 💡 Si l'installateur ne propose pas "Upgrade", choisissez "Install Now" — la nouvelle version sera installée en parallèle et deviendra la version par défaut.

Pour mettre à jour `pip` :

```bash
python -m pip install --upgrade pip
```

---

### 🐧 Linux

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt upgrade python3 -y
```

Pour installer une version plus récente spécifique (ex. 3.12), si elle n'est pas disponible dans le dépôt standard :

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev -y
```

#### Fedora

```bash
sudo dnf upgrade python3 -y
```

#### Mettre à jour pip (toutes distributions)

```bash
python3 -m pip install --upgrade pip
```

---

## 4. Créer un environnement virtuel (Virtual Environment)

### Qu'est-ce qu'un environnement virtuel et pourquoi en avons-nous besoin ?

Un environnement virtuel (Virtual Environment) est un **environnement Python isolé** pour chaque projet. Cela signifie que :

- ✅ Chaque projet possède **ses propres bibliothèques** et versions
- ✅ Pas de conflits entre projets (Projet A utilise Flask 2.0, Projet B utilise Flask 3.0)
- ✅ Facile de partager la liste des dépendances via `requirements.txt`
- ✅ Vous ne polluez pas l'installation Python globale

```
Sans venv :                  Avec venv :
┌──────────────┐             ┌──────────────┐  ┌──────────────┐
│  Python      │             │  Projet A    │  │  Projet B    │
│  global      │             │  venv/       │  │  venv/       │
│              │             │  Flask 2.0   │  │  Flask 3.0   │
│  Flask ???   │             │  requests    │  │  Django 5.0  │
│  requests    │             └──────────────┘  └──────────────┘
│  Django ???  │             Isolés !           Isolés !
└──────────────┘
  Tout mélangé
```

---

### 🪟 Windows

#### Étape 1 — Créer un dossier pour le projet

```bash
mkdir my_web_project
cd my_web_project
```

#### Étape 2 — Créer l'environnement virtuel

```bash
python -m venv venv
```

> Cela crée un dossier `venv/` dans le répertoire courant avec un environnement Python isolé.

#### Étape 3 — Activer l'environnement virtuel

**Invite de commandes (cmd) :**

```bash
venv\Scripts\activate
```

**PowerShell :**

```powershell
venv\Scripts\Activate.ps1
```

> ⚠️ Si vous obtenez une erreur PowerShell concernant l'execution policy, exécutez d'abord :
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### Étape 4 — Vérification

Après l'activation, vous verrez `(venv)` devant l'invite de commandes :

```
(venv) C:\Users\etudiant\my_web_project>
```

Vérifiez que Python fonctionne depuis l'environnement virtuel :

```bash
where python
```

Cela devrait afficher le chemin vers `venv\Scripts\python.exe`.

#### Étape 5 — Installer des paquets (exemple)

```bash
pip install flask
```

#### Étape 6 — Sauvegarder les dépendances

```bash
pip freeze > requirements.txt
```

#### Étape 7 — Désactiver l'environnement virtuel

```bash
deactivate
```

---

### 🐧 Linux

#### Étape 1 — Vérifier que le module `venv` est installé

```bash
sudo apt install python3-venv -y    # Ubuntu/Debian
```

#### Étape 2 — Créer un dossier pour le projet

```bash
mkdir my_web_project
cd my_web_project
```

#### Étape 3 — Créer l'environnement virtuel

```bash
python3 -m venv venv
```

#### Étape 4 — Activer l'environnement virtuel

```bash
source venv/bin/activate
```

Après l'activation, vous verrez `(venv)` devant l'invite de commandes :

```
(venv) etudiant@ubuntu:~/my_web_project$
```

#### Étape 5 — Vérification

```bash
which python
```

Cela devrait afficher : `~/my_web_project/venv/bin/python`

```bash
which pip
```

Cela devrait afficher : `~/my_web_project/venv/bin/pip`

#### Étape 6 — Installer des paquets (exemple)

```bash
pip install flask
```

#### Étape 7 — Sauvegarder les dépendances

```bash
pip freeze > requirements.txt
```

#### Étape 8 — Désactiver l'environnement virtuel

```bash
deactivate
```

---

## 📌 Aide-mémoire (Cheat Sheet)

| Action | Windows (cmd) | Linux |
|---|---|---|
| Vérifier la version | `python --version` | `python3 --version` |
| Créer un venv | `python -m venv venv` | `python3 -m venv venv` |
| Activer le venv | `venv\Scripts\activate` | `source venv/bin/activate` |
| Désactiver le venv | `deactivate` | `deactivate` |
| Installer un paquet | `pip install <paquet>` | `pip install <paquet>` |
| Sauvegarder les dépendances | `pip freeze > requirements.txt` | `pip freeze > requirements.txt` |
| Installer depuis un fichier | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Mettre à jour pip | `python -m pip install --upgrade pip` | `python3 -m pip install --upgrade pip` |
| Supprimer le venv | Supprimez le dossier `venv/` | `rm -rf venv/` |

---

## 5. Problèmes fréquents

### ❌ `python` n'est pas reconnu (Windows)

**Problème :** `'python' is not recognized as an internal or external command`

**Solution :** Python n'a pas été ajouté au PATH. Réinstallez en cochant **"Add python.exe to PATH"** ou ajoutez-le manuellement :
1. Appuyez sur `Win + S`, recherchez "Environment Variables"
2. Dans la section "User variables" → sélectionnez `Path` → Edit
3. Ajoutez les chemins (par exemple) :
   - `C:\Users\<votre_nom>\AppData\Local\Programs\Python\Python3xx\`
   - `C:\Users\<votre_nom>\AppData\Local\Programs\Python\Python3xx\Scripts\`

### ❌ PowerShell bloque l'activation

**Problème :** `cannot be loaded because running scripts is disabled on this system`

**Solution :**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ `No module named venv` (Linux)

**Problème :** `The virtual environment was not created successfully because ensurepip is not available`

**Solution :**

```bash
sudo apt install python3-venv -y
```

### ❌ `pip` ne fonctionne pas dans le venv

**Problème :** `pip` installe les paquets globalement au lieu de dans le venv

**Solution :** Assurez-vous que l'environnement est activé — vous devez voir `(venv)` devant l'invite de commandes. Vérifiez avec :

```bash
# Windows
where pip

# Linux
which pip
```

Le chemin doit pointer vers le dossier `venv/`.

---

> 💡 **Conseil :** Ne versionnez jamais le dossier `venv/` dans Git. Ajoutez-le au `.gitignore` :
> ```
> venv/
> ```

---

*Bon codage ! 🚀*
