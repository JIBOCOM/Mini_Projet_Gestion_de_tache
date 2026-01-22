import sqlite3

def init_db():
    # 1. Connexion (le fichier sera créé s'il n'existe pas)
    connection = sqlite3.connect('database.db')

    # 2. Exécuter le script SQL pour créer les tables
    with open('schema.sql', encoding='utf-8') as f:
        connection.executescript(f.read())

    # 3. Insérer quelques tâches de test
    cur = connection.cursor()

    sample_tasks = [
        ("Réviser le cours de réseau", "Chapitre TCP/IP + routage", "2026-01-25", 0),
        ("Préparer le mini-projet", "Coder la gestion des tâches et tester", "2026-01-28", 0),
        ("Envoyer le lien Alwaysdata", "Vérifier que le site est en ligne", "2026-01-30", 0),
    ]

    cur.executemany(
        "INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)",
        sample_tasks
    )

    connection.commit()
    connection.close()
    print("Base de données initialisée avec des tâches de test.")

if __name__ == "__main__":
    init_db()
