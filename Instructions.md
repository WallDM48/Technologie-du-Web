# 🐍 Ръководство за инсталиране на Python и Virtual Environment

> **Лекция:** Web Technologies  
> **Дата:** 25 март 2026 г.

---

## 📋 Съдържание

1. [Проверка дали Python е инсталиран](#1-проверка-дали-python-е-инсталиран)
2. [Инсталиране на Python](#2-инсталиране-на-python)
3. [Обновяване на съществуваща инсталация](#3-обновяване-на-съществуваща-инсталация)
4. [Създаване на Virtual Environment](#4-създаване-на-virtual-environment)
5. [Често срещани проблеми](#5-често-срещани-проблеми)

---

## 1. Проверка дали Python е инсталиран

### 🪟 Windows

Отворете **Command Prompt** (cmd) или **PowerShell** и изпълнете:

```bash
python --version
```

Ако получите нещо от рода на `Python 3.x.x` — Python вече е инсталиран. Ако получите грешка `'python' is not recognized...` — преминете към [Стъпка 2](#2-инсталиране-на-python).

> ⚠️ На някои Windows системи командата може да бъде `python3` вместо `python`. Опитайте и двете.

### 🐧 Linux

Отворете терминал и изпълнете:

```bash
python3 --version
```

Повечето Linux дистрибуции идват с предварително инсталиран Python 3. Ако командата върне версия `3.x.x` — готови сте. Ако не — преминете към [Стъпка 2](#2-инсталиране-на-python).

---

## 2. Инсталиране на Python

### 🪟 Windows

#### Стъпка 1 — Изтегляне

1. Отидете на официалния сайт: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Кликнете върху жълтия бутон **"Download Python 3.x.x"** (последна стабилна версия)
3. Ще се изтегли `.exe` файл

#### Стъпка 2 — Инсталиране

1. Стартирайте изтегления `.exe` файл
2. **⚠️ ВАЖНО:** Поставете отметка на **"Add python.exe to PATH"** (в долната част на прозореца)
3. Кликнете **"Install Now"**
4. Изчакайте инсталацията да завърши
5. Кликнете **"Close"**

```
┌─────────────────────────────────────────────┐
│  Install Python 3.x.x                      │
│                                             │
│  ☑ Install launcher for all users           │
│  ☑ Add python.exe to PATH  ← ТУК!         │
│                                             │
│  [ Install Now ]                            │
└─────────────────────────────────────────────┘
```

#### Стъпка 3 — Проверка

Отворете **нов** Command Prompt (задължително нов, за да се зареди PATH) и изпълнете:

```bash
python --version
```

```bash
pip --version
```

И двете команди трябва да върнат информация за версиите.

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

#### Проверка

```bash
python3 --version
pip3 --version
```

---

## 3. Обновяване на съществуваща инсталация

### 🪟 Windows

Ако вече имате Python, но е стара версия (напр. 3.8, 3.9):

1. Отидете на [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Изтеглете последната версия
3. Стартирайте инсталатора
4. Изберете **"Upgrade Now"** (инсталаторът автоматично разпознава старата версия)

> 💡 Ако инсталаторът не предложи "Upgrade", изберете "Install Now" — новата версия ще се инсталира паралелно и ще стане версия по подразбиране.

За обновяване на `pip`:

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

За инсталиране на конкретна по-нова версия (напр. 3.12), ако не е налична в стандартното хранилище:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev -y
```

#### Fedora

```bash
sudo dnf upgrade python3 -y
```

#### Обновяване на pip (всички дистрибуции)

```bash
python3 -m pip install --upgrade pip
```

---

## 4. Създаване на Virtual Environment

### Какво е Virtual Environment и защо ни трябва?

Virtual Environment (виртуална среда) е **изолирана Python среда** за всеки проект. Това означава, че:

- ✅ Всеки проект има **собствени библиотеки** и версии
- ✅ Няма конфликти между проекти (Проект A ползва Flask 2.0, Проект B ползва Flask 3.0)
- ✅ Лесно се споделя списък с зависимости чрез `requirements.txt`
- ✅ Не замърсявате глобалната Python инсталация

```
Без venv:                    С venv:
┌──────────────┐             ┌──────────────┐  ┌──────────────┐
│  Глобален    │             │  Проект A    │  │  Проект B    │
│  Python      │             │  venv/       │  │  venv/       │
│              │             │  Flask 2.0   │  │  Flask 3.0   │
│  Flask ???   │             │  requests    │  │  Django 5.0  │
│  requests    │             └──────────────┘  └──────────────┘
│  Django ???  │             Изолирани!         Изолирани!
└──────────────┘
  Всичко смесено
```

---

### 🪟 Windows

#### Стъпка 1 — Създаване на папка за проекта

```bash
mkdir my_web_project
cd my_web_project
```

#### Стъпка 2 — Създаване на виртуална среда

```bash
python -m venv venv
```

> Това създава папка `venv/` в текущата директория с изолирана Python среда.

#### Стъпка 3 — Активиране на виртуалната среда

**Command Prompt (cmd):**

```bash
venv\Scripts\activate
```

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

> ⚠️ Ако получите грешка в PowerShell за execution policy, изпълнете първо:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### Стъпка 4 — Проверка

След активиране, ще видите `(venv)` пред командния ред:

```
(venv) C:\Users\student\my_web_project>
```

Проверете, че Python работи от виртуалната среда:

```bash
where python
```

Трябва да покаже път до `venv\Scripts\python.exe`.

#### Стъпка 5 — Инсталиране на пакети (пример)

```bash
pip install flask
```

#### Стъпка 6 — Запазване на зависимостите

```bash
pip freeze > requirements.txt
```

#### Стъпка 7 — Деактивиране на виртуалната среда

```bash
deactivate
```

---

### 🐧 Linux

#### Стъпка 1 — Уверете се, че `venv` модулът е инсталиран

```bash
sudo apt install python3-venv -y    # Ubuntu/Debian
```

#### Стъпка 2 — Създаване на папка за проекта

```bash
mkdir my_web_project
cd my_web_project
```

#### Стъпка 3 — Създаване на виртуална среда

```bash
python3 -m venv venv
```

#### Стъпка 4 — Активиране на виртуалната среда

```bash
source venv/bin/activate
```

След активиране ще видите `(venv)` пред командния ред:

```
(venv) student@ubuntu:~/my_web_project$
```

#### Стъпка 5 — Проверка

```bash
which python
```

Трябва да покаже: `~/my_web_project/venv/bin/python`

```bash
which pip
```

Трябва да покаже: `~/my_web_project/venv/bin/pip`

#### Стъпка 6 — Инсталиране на пакети (пример)

```bash
pip install flask
```

#### Стъпка 7 — Запазване на зависимостите

```bash
pip freeze > requirements.txt
```

#### Стъпка 8 — Деактивиране на виртуалната среда

```bash
deactivate
```

---

## 📌 Бърза справка (Cheat Sheet)

| Действие | Windows (cmd) | Linux |
|---|---|---|
| Проверка на версия | `python --version` | `python3 --version` |
| Създаване на venv | `python -m venv venv` | `python3 -m venv venv` |
| Активиране на venv | `venv\Scripts\activate` | `source venv/bin/activate` |
| Деактивиране на venv | `deactivate` | `deactivate` |
| Инсталиране на пакет | `pip install <пакет>` | `pip install <пакет>` |
| Запазване на зависимости | `pip freeze > requirements.txt` | `pip freeze > requirements.txt` |
| Инсталиране от файл | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Обновяване на pip | `python -m pip install --upgrade pip` | `python3 -m pip install --upgrade pip` |
| Изтриване на venv | Изтрийте папката `venv/` | `rm -rf venv/` |

---

## 5. Често срещани проблеми

### ❌ `python` не се разпознава (Windows)

**Проблем:** `'python' is not recognized as an internal or external command`

**Решение:** Python не е добавен в PATH. Преинсталирайте с отметка **"Add python.exe to PATH"** или добавете ръчно:
1. Натиснете `Win + S`, потърсете "Environment Variables"
2. В секция "User variables" → изберете `Path` → Edit
3. Добавете пътищата (примерно):
   - `C:\Users\<вашето_име>\AppData\Local\Programs\Python\Python3xx\`
   - `C:\Users\<вашето_име>\AppData\Local\Programs\Python\Python3xx\Scripts\`

### ❌ PowerShell блокира активирането

**Проблем:** `cannot be loaded because running scripts is disabled on this system`

**Решение:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ `No module named venv` (Linux)

**Проблем:** `The virtual environment was not created successfully because ensurepip is not available`

**Решение:**

```bash
sudo apt install python3-venv -y
```

### ❌ `pip` не работи във venv

**Проблем:** `pip` инсталира пакети глобално вместо във venv

**Решение:** Уверете се, че средата е активирана — трябва да виждате `(venv)` пред командния ред. Проверете с:

```bash
# Windows
where pip

# Linux
which pip
```

Пътят трябва да сочи към `venv/` папката.

---

> 💡 **Съвет:** Никога не качвайте папката `venv/` в Git. Добавете я в `.gitignore`:
> ```
> venv/
> ```

---

*Приятно програмиране! 🚀*
