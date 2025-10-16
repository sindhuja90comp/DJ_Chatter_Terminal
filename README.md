# Django + ChatterBot: Terminal Client

A minimal starter to run a terminal chat client using **Python**, **Django (for project structure)**, and **ChatterBot**.

## Prereqs
- **Python 3.8.x** (ChatterBot is known to break on newer Python versions)
- pip

## Quickstart
```bash
# 1) Create & activate a venv (recommended)
python3.8 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install deps
pip install --upgrade pip
pip install -r requirements.txt

# 3) (First run) Train & chat in the terminal
python terminal_client.py
```

The first run may build a SQLite database (`db.sqlite3`) and train from a small English corpus.

## Run as a Django management command (optional)
```bash
python manage.py chatbot
```

## Repo structure
```
dj_chatter_terminal/
├─ manage.py
├─ requirements.txt
├─ terminal_client.py
├─ README.md
├─ db.sqlite3  # created after first run
├─ dj_chatter_terminal/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
└─ bot/
   ├─ __init__.py
   └─ management/
      └─ commands/
         └─ chatbot.py

