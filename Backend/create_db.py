from app import app, db

# Setze den Anwendungs-Kontext
with app.app_context():
    db.create_all()  # Erstelle die Datenbank und Tabellen

print("Datenbank und Tabellen wurden erstellt.")
