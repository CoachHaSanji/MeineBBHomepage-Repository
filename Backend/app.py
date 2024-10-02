from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# Aktiviere CORS für alle Routen
CORS(app)

# Konfiguration für SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Beispiel für SQLite-Datenbank
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Überprüfen, ob der Benutzername bereits existiert
    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'message': 'Benutzername bereits vergeben.'}), 400

    # Neuen Benutzer erstellen
    new_user = User(username=username, password=password)  # Passwort sollte gehasht werden
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Benutzer erfolgreich registriert!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Überprüfen, ob der Benutzer existiert und das Passwort korrekt ist
    user = User.query.filter_by(username=username, password=password).first()  # Passwort sollte gehasht werden

    if user:
        return jsonify({'success': True, 'message': 'Login erfolgreich!'})
    else:
        return jsonify({'success': False, 'message': 'Ungültiger Benutzername oder Passwort.'}), 401

if __name__ == '__main__':
    with app.app_context():  # Anwendungskontext aktivieren
        db.create_all()  # Erstelle die Datenbanktabellen, falls sie nicht existieren
    app.run(port=5000)  # Stelle sicher, dass der Server auf Port 5000 läuft
