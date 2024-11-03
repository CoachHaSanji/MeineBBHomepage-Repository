from app import app, db

# Initialisiere die Datenbank und erstelle alle Tabellen
with app.app_context():
    db.create_all()
